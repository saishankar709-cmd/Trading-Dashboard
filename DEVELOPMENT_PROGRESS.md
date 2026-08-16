ersion 1 — Stable Baseline and Performance Optimization Roadmap



Version 1 — Stable Baseline and Performance Optimization Roadmap
1. Version 1 Status
Version 1 of the Trading Dashboard has been completed and is now considered the stable baseline version of the application.

The current Version 1 should be preserved as a reference implementation before any major performance optimization or architectural changes are introduced.

The primary objective of Version 1 was to establish a functional multi-chart trading dashboard with synchronized charts, multiple layouts, drawing tools, timeframe support, popup charts, and Excel-based market-data loading.

Version 1 is now feature-complete for the current development scope and should be treated as a locked baseline.

2. What We Achieved in Version 1
2.1 Desktop Trading Dashboard
Built a desktop trading dashboard using:

Python
PySide6
Qt WebEngine
JavaScript
Lightweight Charts
Pandas
Excel market-data files
The application provides a multi-chart workspace designed for intraday market analysis.

2.2 Multi-Chart Layout System
Implemented multiple chart layouts supporting different numbers and arrangements of charts.

The dashboard can display multiple chart slots simultaneously and dynamically change between supported layouts.

The chart-slot architecture allows each chart to maintain its own:

Symbol / worksheet
Timeframe
Chart state
Drawing state
WebEngine instance
2.3 Excel Market Data Integration
Implemented Excel-based market-data loading.

The application reads market data containing:

Date
Time
Open
High
Low
Close
The Excel loader:

Combines Date and Time into a timestamp
Validates required columns
Removes invalid timestamp/OHLC rows
Sorts the data chronologically
Provides normalized Pandas DataFrames to the application
The application supports the current market-data file structure used by the project.

2.4 Timeframe Support
Implemented timeframe processing for:

1 Minute
3 Minutes
5 Minutes
10 Minutes
15 Minutes
30 Minutes
1 Hour
1 Day
Intraday aggregation uses the trading-session start time of 09:15.

OHLC aggregation follows standard candle construction:

Open = first value
High = maximum value
Low = minimum value
Close = last value
2.5 Candlestick Charting
Integrated Lightweight Charts into the Qt desktop application using QWebEngineView.

The application displays market data as interactive candlestick charts.

The chart layer supports:

Candlestick rendering
Zooming
Scrolling
Crosshair
Time scale
Price scale
Chart resizing
Multiple independent chart instances
2.6 Crosshair Synchronization
Implemented synchronized crosshair functionality between charts.

The synchronization is based on market timestamp, not price.

The architecture is:

Source Chart
    ↓
Market Timestamp
    ↓
Python synchronization layer
    ↓
Destination Chart
    ↓
Nearest available candle
    ↓
Destination chart's own price

This allows charts containing different instruments and different price ranges to remain correctly synchronized in time.

The synchronization architecture also supports the main dashboard and popup chart windows.

2.7 Crosshair Error Handling
Handled cases where a destination chart cannot immediately convert a timestamp into a valid screen coordinate.

The JavaScript layer validates the calculated coordinate before calling the Lightweight Charts crosshair API.

Invalid values such as:

null
undefined
non-finite coordinates
are rejected safely.

This prevents errors such as:

Value is null

from interrupting chart interaction.

2.8 Drawing Tools
Implemented chart drawing functionality using a separate HTML Canvas overlay.

Current drawing tools include:

Trend Line
Horizontal Line
Vertical Line
Rectangle
Drawing coordinates are stored using market information such as:

Time
Price
rather than permanently storing screen/pixel coordinates.

This allows drawings to remain aligned with the chart during:

Zoom
Scroll
Resize
Chart updates
Timeframe changes
2.9 Drawing Interaction
Implemented interaction with drawings, including:

Selecting drawings
Moving drawings
Resizing supported drawings
Deleting drawings
Redrawing drawings when the chart viewport changes
Drawing interaction uses hit testing and market-to-screen coordinate conversion.

2.10 Popup Charts
Implemented popup chart windows.

A chart can be opened into a separate popup window while maintaining its own chart workspace.

Popup windows support their own:

Layout
Chart slots
Symbol
Timeframe
Drawing state
Mouse synchronization state
Multiple popup windows can be managed by the main dashboard.

2.11 Main Dashboard ↔ Popup Synchronization
Implemented crosshair synchronization between:

Charts in the main dashboard
Charts in popup windows
Multiple popup windows
The synchronization system is designed around market timestamp synchronization so that charts continue to show their own instrument prices while sharing the same time position.

2.12 Mouse Synchronization Controls
Implemented global mouse/crosshair synchronization controls.

The dashboard can enable or disable synchronized mouse behavior.

Layout-level synchronization control is also available, allowing synchronization behavior to be controlled for individual layouts.

When synchronization is disabled, synchronized crosshairs can be cleared appropriately.

2.13 Chart Resizing
Implemented chart resizing support using browser-side resize detection.

The chart responds to changes in its available window/container size so that popup windows and layout changes can resize correctly.

2.14 Data Folder Selection
Implemented the ability to select/change the market-data folder rather than permanently relying only on the initial configured data directory.

This provides flexibility when moving the application between different local data locations.

3. Version 1 Architecture
The current architecture can be summarized as:

Excel Market Data
        ↓
excel_loader.py
        ↓
Pandas DataFrame
        ↓
main.py
        ↓
    ChartSlot
        ↓
   QWebEngineView
        ↓
  QWebChannel
        ↓
 chart_test.html
        ↓
Lightweight Charts
        +
   Drawing Canvas

The Python layer is primarily responsible for:

Data loading
Data validation
Timeframe aggregation
Application state
Layout management
Chart coordination
Main/popup synchronization
The JavaScript layer is primarily responsible for:

Chart rendering
Crosshair rendering
Market-to-screen coordinate conversion
Drawing rendering
Drawing interaction
Chart-side coordinate calculations
This separation should be preserved during future optimization unless a measured performance bottleneck requires architectural changes.

4. Version 1 Backup / Locking Policy
Version 1 is now considered a stable reference point.

Before beginning performance optimization:

Create a complete local ZIP backup.
Preserve the Version 1 source code in a separate private GitHub repository.
Preserve the current project documentation.
Preserve the Python dependency information.
Preserve important market-data files separately if required.
Do not modify the Version 1 backup while performing future development.
The private backup repository should be treated as a read-only historical baseline.

5. Next Major Goal — Performance Optimization
The next development phase will focus on improving the application's performance without changing the existing Version 1 functionality.

The goal is to make the dashboard faster and smoother, particularly when:

Multiple charts are visible
Six to eight charts are active
Multiple popup windows are open
Mouse/crosshair synchronization is enabled
Large market-data files are loaded
Large historical datasets are displayed
Users frequently switch symbols and timeframes
The performance work should be incremental and measurable.

No major rewrite should be performed before identifying and measuring the actual bottlenecks.

6. Performance Optimization Priorities
Priority 1 — Crosshair Synchronization
The current crosshair synchronization can generate frequent communication between Python and the individual QWebEngine/JavaScript chart instances.

Future optimization should:

Throttle high-frequency mouse events
Process the latest mouse position instead of queuing obsolete positions
Minimize unnecessary Python-to-JavaScript calls
Avoid redundant synchronization when the timestamp has not changed
Preserve the current timestamp-based synchronization behavior
Priority 2 — Faster Nearest-Candle Search
The current JavaScript nearest-candle lookup can scan the candle dataset linearly.

Future optimization should replace the O(N) search with a binary-search-based lookup.

Current concept:

Target Timestamp
      ↓
Scan candle array
      ↓
Find nearest candle

Target concept:

Target Timestamp
      ↓
Binary Search
      ↓
Find nearest candle

Expected complexity:

Current: O(N)
Target:  O(log N)

This should significantly reduce the cost of crosshair synchronization on large datasets.

Priority 3 — Market Data Caching
Introduce a centralized data-management/cache layer.

The objective is to prevent the same Excel worksheet from being loaded repeatedly when multiple charts use the same instrument.

Target architecture:

Excel File
    ↓
Data Manager
    ↓
Raw Data Cache
    ↓
Timeframe Cache
    ↓
Chart Slots

Potential cache structure:

Symbol
    ├── 1m
    ├── 3m
    ├── 5m
    ├── 10m
    ├── 15m
    ├── 30m
    ├── 1H
    └── 1D

This should reduce repeated Excel I/O and repeated timeframe aggregation.

Priority 4 — Reduce Repeated Pandas Processing
The Excel loader already normalizes timestamps, validates data, and sorts the dataset.

Future optimization should avoid repeating the same operations inside the timeframe-processing pipeline.

Potential improvements include:

Avoid unnecessary DataFrame copies
Avoid repeated timestamp conversion
Avoid repeated sorting
Reuse normalized data
Cache aggregated results
Priority 5 — Optimize Python → JavaScript Data Transfer
The current implementation serializes candle data into JSON before passing it into the WebEngine.

Future optimization should investigate:

Reducing unnecessary serialization
Avoiding repeated full dataset transfers
Reusing already loaded chart data where possible
Incremental data updates where practical
Binary or alternative transport mechanisms should only be considered if normal JSON transfer becomes a measured bottleneck.

Priority 6 — Optimize Candle Conversion
The current Python implementation converts Pandas rows into individual candle dictionaries.

Future optimization should reduce the overhead of row-by-row processing, particularly for large datasets.

Vectorized Pandas operations or more efficient record conversion should be evaluated.

Priority 7 — Reduce Unnecessary Chart Operations
Investigate repeated operations such as:

fitContent()
price-scale auto-scaling
repeated chart refreshes
redundant chart updates
These operations should only occur when actually required.

Existing behavior must be tested before removing any duplicate-looking operations because some may have been added to resolve rendering timing issues.

Priority 8 — Drawing Performance
Drawing performance should be evaluated after the higher-priority data and synchronization optimizations.

Potential future improvements include:

Reducing unnecessary canvas redraws
Redrawing only when required
Optimizing drawing hit testing
Reducing repeated coordinate calculations
This is currently a lower priority because the number of drawings per chart is expected to be relatively small.

7. Future Performance Architecture
The preferred future architecture is:

Trading Dashboard
        ↓
   Data Manager
        ↓
┌───────┴────────┐
↓                ↓

Raw Data Cache Timeframe Cache
│ │
└───────┬────────┘
↓
Chart Slots
↓
QWebEngine
↓
JavaScript Chart
↓
Lightweight Charts
+
Drawing Canvas

Crosshair synchronization should eventually aim for:

Mouse Movement
      ↓
   Throttle
      ↓
Timestamp Only
      ↓
Fast Lookup
      ↓
Destination Charts

For charts inside the same WebEngine context, JavaScript-side synchronization may be evaluated later to reduce Python/Chromium communication.

Python should remain the bridge for synchronization between separate popup windows where required.

8. Performance Optimization Rules
The following rules should be followed during Version 2 development:

Do not change working Version 1 behavior unnecessarily.
Do not rewrite the complete application.
Optimize one subsystem at a time.
Measure performance before and after major changes.
Keep changes reversible.
Preserve timestamp-based crosshair synchronization.
Preserve independent chart prices during synchronization.
Preserve drawing behavior.
Test both main dashboard and popup charts after synchronization changes.
Test 1-chart, 4-chart, 8-chart and popup scenarios.
Test small and large datasets.
Avoid premature optimization.
Do not introduce complex binary transport unless profiling demonstrates that it is necessary.
Maintain a stable backup of Version 1 throughout the optimization phase.
9. Version 2 Objective
The primary objective of Version 2 is:

Improve performance and responsiveness while maintaining all functional capabilities of Version 1.

Version 2 should provide:

Faster chart loading
Faster timeframe switching
Faster symbol switching
Smoother crosshair synchronization
Better performance with 6–8 charts
Better performance with popup windows
Lower CPU usage where practical
Reduced repeated Excel/Pandas processing
Improved scalability for larger datasets
Functionality should remain consistent with Version 1 unless a change is explicitly approved as a new feature.

10. Long-Term Development Direction
After performance optimization, future development can focus on additional trading-dashboard capabilities.

Potential future areas include:

Improved chart drawing tools
Persistent drawing storage
More advanced chart annotations
Indicators
Additional data sources
Improved symbol management
Workspace persistence
User preferences/settings
More scalable data storage
Application packaging/distribution
Additional performance profiling and monitoring
These features should be considered only after the Version 1 baseline has been successfully optimized and stabilized.

11. Versioning Strategy
Version 1:

Stable baseline
Feature-complete current scope
Locked before performance optimization

Version 2:

Performance optimization
Same core functionality
Improved scalability and responsiveness

Future versions:

New functionality
New trading tools
Additional data capabilities

The Version 1 backup must remain unchanged and available as the historical reference implementation.

