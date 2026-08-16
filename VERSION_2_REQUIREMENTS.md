Trading Dashboard — Version 2 Development Requirements
1. Version 2 Objective
Version 1 is locked, backed up, and must not be modified.

Version 2 will be a performance and memory optimization release.

The primary objective is:

Make the Trading Dashboard substantially faster, smoother, and more memory-efficient on a laptop with limited RAM, while preserving all Version 1 functionality.

We are not starting a feature-development phase.

We are not doing a complete rewrite for the sake of rewriting.

We will redesign only the parts that create measurable performance, CPU, I/O, or memory problems.

2. Non-Negotiable Requirements
These requirements apply to every Version 2 change.

2.1 Preserve Version 1 functionality
The following must continue working:

Multi-chart layouts
Symbol selection
Timeframe selection
Excel data loading
Candlestick charts
Crosshair
Crosshair synchronization
Mouse synchronization
Trend line
Horizontal line
Vertical line
Rectangle
Drawing selection
Drawing movement
Drawing resizing
Drawing deletion
Chart resizing
Popup charts
Popup layouts
Main dashboard ↔ popup synchronization
Multiple popup windows
Data-folder selection
2.2 RAM is a critical constraint
We must not solve performance problems by consuming substantially more RAM.

Avoid unnecessary copies of:

Pandas DataFrames
OHLC data
timeframe DataFrames
Python lists
JSON strings
JavaScript arrays
chart datasets
2.3 No unlimited caching
Caching everything is not acceptable.

Caches must have controlled lifetimes and must be capable of releasing unused data.

2.4 No unnecessary rewrites
Do not rewrite working code unless the rewrite provides a measurable architectural/performance benefit.

2.5 Measure before optimizing
For major changes:

V1 baseline
    ↓
Implement optimization
    ↓
Measure V2
    ↓
Compare
    ↓
Keep or revert

3. Target Architecture
The existing V1 architecture will be improved toward this design:

                    Trading Dashboard
                           │
                           ▼
                     Data Manager
                           │
             ┌─────────────┴─────────────┐
             │                           │
       Raw Data Cache              Timeframe Cache
             │                           │
             └─────────────┬─────────────┘
                           │
                           ▼
                       ChartSlot
                           │
                           ▼
                     QWebEngineView
                           │
                           ▼
                  HTML / JavaScript
                           │
             ┌─────────────┴─────────────┐
             │                           │
      Lightweight Charts          Drawing Canvas

The important architectural change is:

Chart slots should not independently perform expensive data loading and processing.

A centralized data layer should manage data reuse.

4. Optimization Priority
We will work in this exact order.

Priority 1 — Crosshair performance
Priority 2 — Data loading and caching
Priority 3 — Pandas/timeframe processing
Priority 4 — Memory reduction
Priority 5 — Python ↔ JavaScript communication
Priority 6 — QWebEngine/chart rendering
Priority 7 — Drawing performance
We will not jump randomly between areas.

5. Crosshair Optimization
This is the first code optimization we will implement.

5.1 Mouse-event throttling
Current problem:

Mouse movement
    ↓
Many events
    ↓
Many synchronization calls
    ↓
Multiple charts

Target:

Mouse movement
    ↓
Throttle
    ↓
Latest event
    ↓
One synchronization cycle

We should not process obsolete mouse positions.

The synchronization system should process the latest relevant mouse position.

5.2 Avoid duplicate timestamp synchronization
If the timestamp has not changed:

Previous timestamp = 10:31:25
New timestamp      = 10:31:25

Do nothing.

This eliminates unnecessary JavaScript calls.

5.3 Replace linear nearest-candle search
Current conceptual approach:

Target timestamp
       ↓
Scan candle array
       ↓
Find nearest candle

Replace with:

Target timestamp
       ↓
Binary search
       ↓
Nearest candle

Target complexity:

O(N) → O(log N)

The existing chronological timestamp data should be reused rather than creating unnecessary duplicate arrays.

5.4 Minimize runJavaScript() calls
We will reduce:

Number of calls
Duplicate calls
Unnecessary callbacks
Repeated data transfer
Where appropriate, related operations should be combined.

6. Data Manager
We will introduce a centralized data-management component.

Instead of:

Chart 1 → Excel
Chart 2 → Excel
Chart 3 → Excel
Chart 4 → Excel

we want:

                 Excel
                   ↓
              DataManager
                   ↓
              Shared Cache
                   ↓
        ┌──────────┼──────────┐
        ↓          ↓          ↓
     Chart 1    Chart 2    Chart 3

The DataManager becomes responsible for:

Loading data
Normalizing data
Validating data
Reusing data
Timeframe processing
Cache management
Releasing unused data
7. Raw Data Loading
Raw market data should be normalized once.

The pipeline should become:

Excel
  ↓
Load
  ↓
Validate
  ↓
Timestamp creation
  ↓
Sort
  ↓
Normalized raw data
  ↓
Cache

Do not repeat these operations every time another chart requests the same data.

8. Timeframe Processing
Supported Version 1 timeframes remain unchanged:

1m
3m
5m
10m
15m
30m
1H
1D
Timeframe aggregation should reuse normalized raw data.

Do not repeatedly:

Convert timestamps
Sort data
Validate the same data
Create unnecessary DataFrame copies
9. Timeframe Cache
We may cache processed timeframes:

Symbol
 ├── 1m
 ├── 3m
 ├── 5m
 ├── 10m
 ├── 15m
 ├── 30m
 ├── 1H
 └── 1D

However:

Do not automatically cache every symbol × timeframe combination forever.

The cache must be memory-aware.

10. Memory-Aware Cache
The cache should eventually support:

Maximum cache entries
Recently-used tracking
Removal of unused datasets
Cache clearing
Memory-conscious retention
Preferred approach:

Frequently used
      ↓
Keep

Not used recently
      ↓
Eligible for removal

We should favor LRU-style behavior rather than unlimited caching.

11. Reduce DataFrame Copies
This is a major requirement.

We must identify every location where we unnecessarily do:

df.copy()

or create intermediate DataFrames.

Copies should only be made when required for correctness.

The objective is:

One normalized dataset
        ↓
Reuse

rather than:

DataFrame
   ↓ copy
DataFrame
   ↓ copy
DataFrame
   ↓ copy
DataFrame

12. Optimize Pandas Processing
We will review:

iterrows()
apply()
repeated sorting
repeated timestamp conversion
unnecessary DataFrame copies
unnecessary temporary columns
repeated filtering
repeated aggregation
Where practical, replace expensive row-by-row processing with vectorized operations.

13. Candle Conversion
The conversion:

Pandas DataFrame
       ↓
Python candle dictionaries
       ↓
JSON

must be reviewed for memory and CPU cost.

We should avoid creating unnecessary intermediate structures.

We will use the most efficient representation that remains maintainable and compatible with the current chart implementation.

14. Excel Optimization
Excel should not be read repeatedly when the same data is already available.

Requirements:

Read only required worksheet/data
Avoid unnecessary workbook loading
Reuse loaded normalized data
Avoid duplicate reads
Release unused data when appropriate
15. Python → JavaScript Data Transfer
Current conceptual flow:

Pandas
  ↓
Python dictionaries
  ↓
JSON serialization
  ↓
QWebEngine
  ↓
JavaScript parsing
  ↓
Chart

This transfer must be optimized.

We should:

Avoid repeated full dataset transfers
Avoid sending unchanged data
Avoid repeated JSON generation
Reuse chart data where possible
Transfer only what is required
We will not implement binary transport unless profiling proves JSON is a significant bottleneck.

16. QWebEngine Optimization
QWebEngine is potentially one of the largest memory consumers.

We will investigate:

Number of QWebEngine instances
Memory per chart
Popup memory
Hidden chart instances
Unused WebEngine instances
Repeated page reloads
Duplicate chart data
We will not create additional WebEngine instances unless required.

17. Popup Resource Management
Popup functionality must remain unchanged.

When a popup is closed:

Popup closed
     ↓
Release chart resources
     ↓
Remove references
     ↓
Allow unused data/resources to be released

We must investigate references that could unintentionally keep closed popup objects alive.

18. Chart Rendering
Review and optimize unnecessary calls to:

fitContent()
setData()
auto-scale
chart refresh
crosshair updates
resize operations
A chart should only perform expensive work when something actually changed.

19. Drawing Performance
Drawing tools remain fully supported.

Optimization will focus on:

Reducing unnecessary canvas redraws
Reducing coordinate recalculation
Efficient hit testing
Avoiding redraws when nothing changed
Drawing optimization is lower priority than data and crosshair optimization.

20. Debug Logging
High-frequency logging must not remain enabled during normal use.

Especially avoid logging every:

Mouse movement
Crosshair event
Chart synchronization event
Debug logging should be controllable and disabled during normal operation.

21. Performance Baseline
Before major optimization, we will measure Version 1.

Minimum measurements:

Startup
Application startup time

Data
Excel loading time
Timeframe processing time

Charts
1 chart
4 charts
6 charts
8 charts

Popup
1 popup
Multiple popups

Interaction
Crosshair
Scrolling
Zooming
Timeframe switching
Symbol switching
Layout switching

Resources
RAM usage
CPU usage

22. Memory Test Scenarios
These tests are mandatory.

Test 1
1 chart
1 symbol
1 timeframe

Test 2
4 charts
4 symbols/timeframes

Test 3
8 charts
Different symbols/timeframes

Test 4
8 charts
+ 1 popup

Test 5
8 charts
+ multiple popups

Test 6
Large dataset
+ 8 charts
+ crosshair synchronization

We will monitor whether memory keeps increasing when charts/popups are repeatedly opened and closed.

23. CPU Test Scenarios
Measure CPU usage during:

Crosshair movement
Scrolling
Zooming
Timeframe switching
Symbol switching
Layout changes
Popup creation
Drawing
The goal is to eliminate unnecessary CPU spikes.

24. No Feature Expansion
During the initial Version 2 optimization phase, do not add new trading features.

Do not add:

New indicators
New drawing tools
New chart types
New data sources
New UI features
until the performance optimization phase is complete.

25. No Unnecessary Dependencies
Do not introduce additional libraries unless they provide a clear and measurable benefit.

The preferred Version 2 solution is to improve the existing architecture using the current technology stack.

26. Code Quality Requirements
While rewriting/optimizing code:

Keep responsibilities separated
Avoid giant functions
Avoid duplicated logic
Use clear class responsibilities
Use meaningful names
Keep data flow explicit
Avoid hidden global state
Avoid unnecessary object references
Properly clean up resources
The performance rewrite should also make the code easier to maintain.

27. Proposed V2 Components
Where appropriate, the codebase should evolve toward components such as:

main.py
    │
    ├── DataManager
    │      ├── RawDataCache
    │      └── TimeframeCache
    │
    ├── ChartSlot
    │
    ├── PopupChartWindow
    │
    └── SynchronizationManager

The exact class names can change if the existing code suggests a better design, but the responsibilities should remain separated.

28. Synchronization Manager
Crosshair/mouse synchronization should be centralized rather than scattered across unrelated chart/UI code.

Responsibilities:

Receive mouse position
Throttle events
Determine timestamp
Avoid duplicate timestamps
Synchronize charts
Synchronize popup charts
Clear synchronization when required
Target:

Mouse
  ↓
SynchronizationManager
  ↓
Timestamp
  ↓
Destination Charts

29. DataManager Responsibilities
The DataManager should eventually own:

load raw data
normalize data
validate data
cache raw data
aggregate timeframe
cache timeframe
release unused data

ChartSlot should request data from DataManager instead of independently managing expensive data-loading logic.

30. Resource Lifecycle
Every major resource should have a clear lifecycle.

For example:

Create
  ↓
Use
  ↓
Reuse if appropriate
  ↓
Release when no longer needed

This applies to:

DataFrames
Cache entries
Chart objects
QWebEngineViews
Popup windows
JavaScript objects
Signal connections
Callbacks
31. Optimization Order for Tomorrow
Tomorrow, development should begin in this exact order:

Step 1 — Read V1 source
Review:

main.py
excel_loader.py
chart_test.html

and understand the current execution/data flow.

Step 2 — Establish baseline
Measure:

startup
Excel load
timeframe processing
RAM
CPU
crosshair responsiveness

Step 3 — Refactor data loading
Create the centralized DataManager architecture.

Step 4 — Implement controlled caching
Implement raw-data reuse and carefully controlled timeframe caching.

Step 5 — Optimize Pandas processing
Remove redundant copies and repeated processing.

Step 6 — Optimize crosshair
Implement:

throttling
+
duplicate timestamp prevention
+
binary search
+
reduced JavaScript calls

Step 7 — Optimize Python ↔ JavaScript data transfer
Reduce unnecessary JSON serialization and full dataset transfers.

Step 8 — Optimize QWebEngine/chart lifecycle
Investigate memory usage and unnecessary chart operations.

Step 9 — Optimize drawings
Only after the above areas are stable.

Step 10 — Full regression testing
Compare Version 2 against the locked V1 behavior.

32. Definition of Success
Version 2 is successful only if we achieve measurable improvement, not merely cleaner code.

The target is:

                    VERSION 1
                       │
                       ▼
              ┌─────────────────┐
              │ Performance     │
              │ Baseline        │
              └────────┬────────┘
                       │
                       ▼
                 V2 Optimization
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
        Lower        Lower        Faster
         RAM          CPU        Response
          │            │            │
          └────────────┼────────────┘
                       ▼
                 VERSION 2

Specifically:

Lower RAM usage
Lower CPU usage
Faster chart loading
Faster timeframe switching
Faster symbol switching
Smoother crosshair
Less lag with 6–8 charts
Less lag with popup windows
Less repeated Excel processing
Less repeated Pandas processing
Less Python ↔ JavaScript communication
No memory growth caused by repeatedly opening/closing popups
No functional regression
33. Final Decision — Locked for Version 2
The following decisions are now considered approved and should not be revisited tomorrow unless the actual V1 code proves that an assumption is incorrect:

Area	Decision
Main objective	Performance + memory optimization
RAM	Critical constraint
CPU	Reduce unnecessary CPU usage
Architecture	Incremental improvement, not blind rewrite
Data loading	Centralized DataManager
Raw data	Controlled caching
Timeframes	Controlled caching
Cache	Memory-aware / bounded
Pandas	Remove redundant processing/copies
Crosshair	Throttled
Timestamp lookup	Binary search
Duplicate updates	Prevent
JS calls	Minimize
JSON transfer	Reduce
QWebEngine	Reduce unnecessary instances/work
Popups	Proper resource cleanup
Drawing	Optimize after core performance
Logging	Disable high-frequency logging
New features	Not during optimization phase
Binary transport	Only if profiling proves necessary
Version 1	Never modify
Testing	Measure before/after
Rollback	Always possible

Final development instruction
Tomorrow we start with the existing V1 code.

We should not spend the first part of the session redesigning requirements.

The first task is to inspect the actual V1 implementation against this specification, establish the baseline measurements, and then begin the optimization in the priority order above.

If the existing code reveals that one of our assumptions is technically incorrect, we should adapt the implementation — but the goals remain fixed: significantly lower resource consumption, better responsiveness, and preservation of V1 functionality.
