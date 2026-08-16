Trading Dashboard — Version 2 Performance Optimization Requirements

Version 2 Purpose Version 1 of the Trading Dashboard has been completed, tested, backed up, and locked as the stable baseline.
Version 2 will focus primarily on performance optimization, memory efficiency, responsiveness, and scalability.

The objective is not to rewrite the application unnecessarily.

The objective is to take the existing Version 1 architecture and systematically optimize the areas that consume the most:

RAM CPU Python processing time JavaScript processing time QWebEngine resources Excel I/O Python ↔ JavaScript communication Chart rendering resources Version 2 must maintain the existing Version 1 functionality unless a change is explicitly approved.

Primary Version 2 Goal The primary goal is:
Make the Trading Dashboard significantly faster and more memory-efficient while maintaining the existing Version 1 functionality.

The application should remain responsive when:

Multiple charts are open Six to eight charts are displayed Multiple popup windows are open Crosshair synchronization is enabled Large Excel datasets are loaded Timeframes are changed Symbols are changed Charts are resized Drawings are used Multiple chart layouts are switched The application must be designed specifically for a limited-RAM / limited-resource laptop environment.

Critical Resource Constraint The development environment has limited RAM and system resources.
Therefore, memory efficiency is a first-class requirement.

The application must avoid unnecessary duplication of:

Pandas DataFrames OHLC datasets JSON strings JavaScript candle arrays Chart data Excel workbook contents Popup chart data Cached timeframe data Performance improvements must not simply trade CPU usage for excessive RAM usage.

Likewise, reducing RAM usage must not result in excessive CPU consumption.

The goal is a balanced architecture suitable for a resource-constrained laptop.

Version 2 Design Principles All optimization work should follow these principles:
Preserve Version 1 functionality. Optimize before rewriting. Measure before and after major changes. Avoid unnecessary memory duplication. Avoid loading data that is not currently required. Avoid recalculating data that has already been calculated. Avoid sending the same data repeatedly between Python and JavaScript. Avoid unnecessary Python ↔ Chromium communication. Avoid unnecessary chart redraws. Avoid unnecessary Excel file reads. Avoid unnecessary Pandas copies. Avoid unbounded caches. Release unused data when appropriate. Prefer simple solutions over complex infrastructure. Keep every optimization reversible. 5. Current Version 1 Performance Bottlenecks The current Version 1 architecture has several areas that may consume significant resources.

The major areas identified for optimization are:

5.1 Crosshair Synchronization Current general architecture:

Mouse Movement ↓ Python callback ↓ Dashboard synchronization ↓ Multiple runJavaScript() calls ↓ Multiple chart instances ↓ JavaScript nearest-candle search

This can generate a high number of operations when several charts are visible.

5.2 Nearest-Candle Search The current JavaScript implementation can perform a linear search through candle timestamps when synchronizing crosshairs.

Conceptually:

Target Timestamp ↓ Scan candle array ↓ Find nearest candle

For large datasets this becomes increasingly expensive.

Target:

Target Timestamp ↓ Binary Search ↓ Nearest Candle

Complexity:

Current: O(N) Target: O(log N)

This is expected to significantly reduce CPU consumption during crosshair synchronization.

5.3 Repeated Excel Loading Multiple charts may request the same worksheet/data.

Without effective caching, the same Excel data may be loaded and processed repeatedly.

This creates unnecessary:

Disk I/O Excel parsing Pandas DataFrame creation RAM usage CPU usage Version 2 must introduce controlled data caching.

5.4 Repeated Timeframe Aggregation Changing timeframes may repeatedly process the same raw market data.

Version 2 should avoid recalculating identical timeframe datasets unnecessarily.

5.5 Repeated Pandas Processing Version 1 performs operations such as:

DataFrame copying Timestamp conversion Sorting Aggregation Row-by-row candle conversion Some of these operations may already have been performed earlier in the pipeline.

Version 2 should eliminate redundant work.

5.6 Python → JavaScript Data Transfer The current implementation serializes candle data to JSON and transfers it into QWebEngine.

Large datasets can therefore create:

JSON serialization cost temporary Python memory usage JavaScript parsing cost temporary JavaScript memory usage QWebEngine communication overhead Version 2 should reduce unnecessary full-data transfers.

5.7 Multiple QWebEngine Instances Every chart slot uses a QWebEngine-based chart environment.

Eight charts therefore represent multiple browser/chart contexts.

Popup windows add additional chart instances.

Because QWebEngine can consume significant memory, Version 2 must minimize unnecessary chart instances and unnecessary data duplication.

Performance Optimization Phase 1 — Crosshair System The first optimization phase will focus on crosshair synchronization.
6.1 Mouse Event Throttling Mouse movement events should not result in unlimited synchronization operations.

Current conceptual flow:

Mouse Event ↓ Immediate Synchronization ↓ Multiple Charts

Target:

Mouse Events ↓ Throttle ↓ Latest Position ↓ Synchronization

Only the latest relevant mouse position should be processed.

Old queued mouse positions should not be processed after they become obsolete.

6.2 Avoid Redundant Crosshair Updates If the new timestamp is identical to the timestamp already synchronized, no new synchronization operation should be performed.

Example:

Current synchronized timestamp: 10:31:25

New event: 10:31:25

Result:

Do nothing.

This reduces unnecessary JavaScript calls.

6.3 Binary Search Replace linear nearest-candle lookup with binary search.

The existing chronological candle timestamp array should be reused.

No duplicate timestamp array should be created unnecessarily.

6.4 Minimize Python ↔ JavaScript Calls The number of runJavaScript() calls should be minimized.

Where possible:

Combine operations Avoid repeated calls Avoid sending unchanged values Avoid unnecessary callbacks 7. Performance Optimization Phase 2 — Data Manager and Cache Version 2 should introduce a centralized data-management layer.

Target architecture:

ChartSlot ↓ DataManager ↓ Cache ↓ Excel / Pandas

Chart slots should not independently perform expensive data-loading operations whenever possible.

Raw Data Cache The application should cache normalized raw market data in memory where appropriate.
Conceptually:

Data Source ↓ Normalized Data ↓ Raw Data Cache ↓ Multiple Chart Slots

If multiple charts use the same instrument/data source, the data should be reused rather than loaded repeatedly.

Timeframe Cache Timeframe results should be cached carefully.
Conceptually:

Symbol ├── 1m ├── 3m ├── 5m ├── 10m ├── 15m ├── 30m ├── 1H └── 1D

However, the cache must have a memory policy.

The application must NOT blindly retain every possible dataset indefinitely.

Memory-Aware Cache Policy Because the laptop has limited RAM, Version 2 must avoid unlimited caching.
The cache should eventually support policies such as:

Maximum number of cached datasets Maximum approximate cache size Least-recently-used removal Removal of unused timeframe datasets Explicit cache clearing The exact cache policy should be determined after measuring actual memory usage.

Avoid Duplicate Data Copies A major Version 2 objective is to identify where the same market data exists multiple times.
Potential duplication includes:

Excel ↓ Pandas DataFrame ↓ Aggregated DataFrame ↓ Python list of dictionaries ↓ JSON string ↓ JavaScript array ↓ Lightweight Charts internal data

This can consume significantly more RAM than the original dataset.

Version 2 should reduce unnecessary intermediate copies.

Timeframe Processing Optimization The data pipeline should be changed so that expensive normalization operations occur only when necessary.
If the Excel loader has already:

Created timestamps Validated data Removed invalid rows Sorted data the timeframe engine should not repeat those operations unnecessarily.

The target architecture is:

Excel ↓ Normalize Once ↓ Cache ↓ Timeframe Aggregation ↓ Cache if appropriate ↓ Chart

Pandas Optimization Version 2 should investigate and optimize:
DataFrame copies Repeated sorting Repeated timestamp conversion Unnecessary temporary columns Row-by-row iteration Unnecessary intermediate DataFrames Where appropriate, vectorized operations should replace slower row-by-row operations.

iterrows() should be avoided for high-volume candle conversion where a more efficient approach is available.

Memory-Efficient Data Types Version 2 should investigate whether Pandas columns can use more memory-efficient data types.
Potential areas:

Float columns Integer columns Timestamp representation Symbol identifiers Repeated categorical values However, data-type changes must only be introduced after confirming that they do not reduce numerical accuracy required for trading data.

Price accuracy is more important than small memory savings.

Excel I/O Optimization Excel files should not be reread unnecessarily.
Version 2 should:

Load only the required worksheet Reuse already loaded data where possible Avoid duplicate workbook reads Cache normalized data where beneficial Release unused data when appropriate The application should not keep entire workbooks in memory if only individual worksheets are required.

Python → JavaScript Data Transfer Optimization The application should minimize the amount of data transferred into QWebEngine.
Potential future improvements:

Avoid transferring unchanged datasets Reuse already loaded chart data Transfer only required data Avoid unnecessary JSON reconstruction Investigate incremental updates Measure JSON serialization time Binary transfer should NOT be implemented automatically.

It should only be considered if profiling shows that JSON transfer is a significant bottleneck.

Chart Data Management Each chart should maintain only the data it actually needs.
The application should avoid unnecessary duplication of the same large dataset across chart instances.

Where multiple charts display the same data:

Reuse Python-side data Avoid unnecessary reloads Avoid unnecessary transformations The JavaScript side should only maintain the data necessary for chart rendering and interaction.

QWebEngine Memory Optimization QWebEngine instances can consume significant memory.
Version 2 should investigate:

Number of active QWebEngine instances Memory consumption per chart Popup chart memory usage Unused popup windows Hidden chart instances Duplicate chart data Unnecessary WebEngine reloads The application should avoid creating browser/chart instances unnecessarily.

Popup Optimization Popup functionality must remain fully supported.
However, popup creation and destruction should be reviewed for resource usage.

When a popup is closed:

Its resources should be released where appropriate. References should be removed. Unnecessary chart data should not remain cached solely because the popup once existed. The popup registry should not retain objects unnecessarily.

Drawing Performance Drawing functionality must remain unchanged.
However, Version 2 should optimize:

Canvas redraw frequency Coordinate conversion Drawing hit testing Redundant redraws Unnecessary redraws during chart updates Drawing optimization is lower priority than crosshair/data optimization.

Chart Rendering Optimization Investigate unnecessary calls to:
fitContent() Auto-scale operations Chart data updates Canvas redraw Crosshair positioning The application should avoid performing the same rendering operation multiple times when one operation is sufficient.

Any removal of existing calls must be tested carefully because some may exist to handle WebEngine rendering timing.

Debug and Logging Optimization High-frequency debug output must not remain enabled during normal operation.
Examples include debug output generated during:

Crosshair movement Mouse synchronization Chart synchronization Debug logging should be:

Disabled by default Enabled only when troubleshooting Avoided inside high-frequency loops unless explicitly required Console output must not become a performance bottleneck.

Performance Measurement Framework Version 2 should establish basic performance measurements.
Before and after important changes, measure:

Application startup time Initial chart loading time Excel loading time Timeframe switching time Symbol switching time Crosshair responsiveness CPU usage RAM usage Popup opening time Layout switching time Chart refresh time Testing should be performed with:

1 chart 4 charts 6 charts 8 charts 1 popup Multiple popups Where possible, test both small and large datasets.

Memory Testing Memory usage is a critical Version 2 metric.
The following scenarios should be tested:

Test A 1 chart 1 symbol 1 timeframe

Test B 4 charts Different symbols Different timeframes

Test C 8 charts Different symbols/timeframes

Test D 8 charts

1 popup
Test E 8 charts

multiple popups
Test F Large historical dataset

crosshair synchronization
The goal is to identify memory growth and determine whether memory is being released correctly.

CPU Testing CPU usage should be monitored during:
Crosshair movement Chart scrolling Chart zooming Timeframe switching Symbol switching Layout switching Popup creation Drawing operations The primary objective is to reduce CPU spikes caused by repeated operations.

Avoiding Memory Leaks Version 2 must specifically investigate possible memory retention involving:
QWebEngineView PopupChartWindow ChartSlot references JavaScript chart objects Python callbacks QWebChannel objects Cached DataFrames Cached timeframe datasets Closing a popup should eventually release resources associated with that popup when no other object needs them.

Cache Lifetime Rules No cache should remain unlimited.
Every cached object should have a clear reason to remain in memory.

Potential cache lifecycle:

Requested ↓ Loaded ↓ Used ↓ Reused ↓ No longer needed ↓ Eligible for removal

The application should prioritize active charts and recently used datasets.

Performance vs Memory Trade-Off Version 2 must not blindly cache everything.
Example:

Caching every symbol and every timeframe:

Faster + Very high RAM usage

Loading everything every time:

Low cache memory + Very high CPU/I/O usage

The target is:

Controlled Cache + Low Duplication + Efficient Reuse + Predictable RAM Usage

This balance is a major Version 2 requirement.

Proposed Optimization Order Optimization should be implemented in this order:
Phase 1 Crosshair optimization:

Remove high-frequency debug output Add throttling Avoid duplicate timestamp updates Implement binary-search candle lookup Reduce redundant JavaScript calls Phase 2 Data optimization:

Create DataManager Normalize market data once Introduce raw-data caching Introduce controlled timeframe caching Eliminate repeated Pandas operations Phase 3 Memory optimization:

Identify duplicate datasets Reduce DataFrame copies Optimize data structures Add cache eviction Release unused popup/chart resources Phase 4 Data-transfer optimization:

Reduce JSON serialization Avoid repeated full dataset transfers Reuse existing chart data Evaluate incremental updates Phase 5 Rendering optimization:

Optimize chart refreshes Optimize fitContent/auto-scale operations Optimize canvas redraws Optimize drawing hit testing Phase 6 Advanced optimization only if required:

JavaScript-side synchronization for charts within the same WebEngine context Advanced memory optimization Binary/compact data transfer if profiling proves it necessary 30. Important Architectural Decision Version 2 should NOT immediately rewrite the entire application.

The existing architecture is considered functional and should be preserved.

Optimization should be incremental:

Version 1 ↓ Measure ↓ Optimize One Area ↓ Test ↓ Measure Again ↓ Keep / Revert ↓ Next Optimization

This makes it possible to identify which changes actually improve performance.

Functional Regression Requirements After every major optimization, the following Version 1 functionality must continue working:
Multi-chart layouts Symbol selection Timeframe selection Candlestick rendering Crosshair Crosshair synchronization Mouse synchronization Drawing tools Drawing movement Drawing resizing Drawing deletion Chart resizing Popup charts Popup layouts Main ↔ popup synchronization Multiple popup windows Data folder selection Excel loading Timeframe aggregation Performance optimization must not silently remove existing functionality.

Success Criteria Version 2 will be considered successful when the application demonstrates measurable improvement compared with Version 1.
The desired outcomes are:

Lower RAM usage Lower CPU usage during normal interaction Faster chart loading Faster timeframe switching Faster symbol switching Smoother crosshair movement Reduced lag with 6–8 charts Reduced lag with popup windows Reduced repeated Excel processing Reduced repeated Pandas processing Reduced Python ↔ JavaScript communication Stable behavior with larger datasets No significant functional regression Exact performance targets should be established after collecting Version 1 baseline measurements.

Version 2 Development Philosophy Version 2 is a performance engineering phase.
The objective is not to add as many features as possible.

The objective is to make the existing Trading Dashboard:

Faster More responsive More memory efficient More CPU efficient More scalable More stable

while keeping the Version 1 functionality intact.

Baseline and Rollback Version 1 has been backed up separately and must remain untouched.
If a Version 2 optimization causes:

Functional regression Increased memory usage Increased CPU usage Chart instability Synchronization problems Data corruption Unexpected behavior the change must be reverted or redesigned.

Version 1 remains the definitive reference implementation.

Final Version 2 Objective The final Version 2 target is:
A significantly faster and more resource-efficient Trading Dashboard that can comfortably operate multiple synchronized charts and popup windows on a laptop with limited RAM and system resources, while maintaining the functionality and behavior established in Version 1.

Performance improvement must be achieved through:

Reduced repeated computation Reduced unnecessary memory allocation Controlled caching Efficient data structures Faster lookup algorithms Reduced communication overhead Reduced chart rendering overhead Better resource lifecycle management The optimization process must remain measurable, incremental, reversible, and focused on real bottlenecks.

One important note for tomorrow When we continue from this document, I will treat these requirements as the Version 2 specification. The key priorities I would keep in mind are:

RAM efficiency first + CPU efficiency + crosshair responsiveness + large-data handling.

And I would not start by rewriting main.py. We'll first establish a V1 performance baseline, identify the biggest actual resource consumers, and then optimize them one at a time. This is especially important on your limited-RAM laptop because an optimization that makes something faster but doubles memory consumption would be a bad optimization for your environment.
