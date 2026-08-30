Trading Dashboard — V2 Updated Performance Development Checkpoint
Date: 30-Aug-2026
Version: V2 — Updated Performance
Status: FUNCTIONALLY STABLE
Next Development Session: Continue from this checkpoint; do not restart previous debugging.

1. Current V2 Status
The Trading Dashboard is currently in a stable working state after resolving the major chart, popup, drawing-layer, symbol-switching, and crosshair synchronization problems.

Confirmed working
Main dashboard loads correctly.
Popup chart windows load correctly.
Candlesticks are visible in the main dashboard.
Candlesticks are visible in popup windows.
Popup scripts/symbols can be changed.
NIFTY / SENSEX / option scripts can be selected.
Timeframe switching works.
Mouse interaction works.
Crosshair works.
Crosshair synchronization between charts works.
Drawing canvas is present and drawings remain functional.
Drawing canvas no longer hides the candlestick chart.
Popup charts receive candle data from Python.
JavaScript chart initialization works.
Lightweight Charts candlestick series initializes correctly.
Popup chart refresh works.
Popup resizing works.
Main dashboard functionality remains intact after the popup fixes.
The application should now be treated as a known-good functional baseline.

2. Files Involved
Existing application files modified
src/main.py
This remains the primary Python application file.

Changes made during V2 development include fixes/updates related to:

ChartSlot
PopupChartWindow
popup chart initialization
popup slot state
popup symbol/script selection
popup timeframe handling
chart refresh
Python → JavaScript chart data submission
crosshair synchronization
popup refresh handling
symbol list synchronization
chart-ready handling
performance diagnostics
Important classes/functions involved include:

ChartSlot
PopupChartWindow
refresh_slot()
refresh_all_slots()
symbol_changed()
change_timeframe()
update_symbol_list()
update_header()

There were multiple refresh_slot() implementations/usages found during investigation, so future changes must be made carefully and in the correct class.

src/web/chart_test.html
This is the JavaScript/HTML chart layer.

Changes made during V2 development include:

Lightweight Charts initialization/debugging
candlestick series creation
chart sizing
drawing canvas handling
drawing canvas resizing
drawing canvas layering
crosshair synchronization
Python → JavaScript chart data handling
candle data validation/debugging
chart auto-scaling
chart fitContent()
resize observer handling
drawing redraw after chart updates
The important chart flow is:

Python
   ↓
setChartData()
   ↓
candleSeries.setData(data)
   ↓
autoScale
   ↓
fitContent()
   ↓
redrawDrawings()

3. Drawing Canvas Fix
One of the important problems discovered during V2 was related to the drawing canvas.

The drawing canvas is intentionally positioned above the chart:

Chart
  ↓
Drawing Canvas Overlay

However, the canvas must NOT intercept mouse events.

The CSS/HTML structure currently uses the drawing canvas as a visual overlay while mouse interaction remains available to the chart.

The relevant structure is:

<div id="chart">
    <canvas id="drawingCanvas"></canvas>
</div>

The canvas is resized according to the chart container:

resizeDrawingCanvas()

The canvas uses device-pixel-ratio scaling so drawings remain correctly rendered.

This was tested successfully.

Result
Before the fix:

Drawing canvas
      ↓
could interfere with chart display/input

After the fix:

Drawing canvas
      ↓
visual overlay only
      ↓
chart remains visible
      ↓
mouse/crosshair still works

This is now considered stable.

4. Popup Chart Fixes
The popup chart was initially the major problem area.

The popup had situations where:

candles were not visible,
chart dimensions were initially 0 x 0,
popup chart data was not being displayed,
popup symbol/script switching did not work,
popup refresh produced errors.
We investigated the popup separately instead of changing the entire dashboard architecture.

The popup architecture remains:

PopupChartWindow
       ↓
ChartSlot objects
       ↓
QWebEngineView
       ↓
chart_test.html
       ↓
Lightweight Charts

The popup creates its own chart slots:

for slot_id in range(8):

    slot = ChartSlot(
        slot_id,
        self
    )

Each popup slot receives its initial:

sheet
symbol
timeframe

from the source slot.

This allowed popup charts to behave consistently with the main dashboard.

5. Popup current_file Error
During testing we found:

[POPUP SLOT ERROR] Chart 1 NIFTY:
'PopupChartWindow' object has no attribute 'current_file'

Later we encountered a related variant:

'builtin_function_or_method' object has no attribute 'current_file'

This identified a popup-specific state/reference problem.

The popup was incorrectly depending on state that belongs to the main dashboard/application context.

The issue was corrected so that popup chart refresh no longer depends incorrectly on PopupChartWindow.current_file.

Result
Popup candle loading now works.

6. Popup Symbol / Script Switching
The popup originally displayed its symbol selector but changing the script did not work correctly.

The popup contains:

self.symbol_combo = QComboBox()

and connects:

self.symbol_combo.currentTextChanged.connect(
    self.symbol_changed
)

The popup symbol-change handler updates the active slot:

slot.symbol = symbol
slot.sheet = symbol

and then refreshes the slot.

The symbol list is also synchronized from the dashboard.

Result
Popup symbol/script switching is now working.

This has been explicitly tested after the latest code changes.

7. Timeframe Handling
Timeframe changes continue to operate through the slot state.

The basic flow is:

User changes timeframe
        ↓
slot.timeframe updated
        ↓
refresh_slot()
        ↓
Python prepares timeframe data
        ↓
JavaScript receives candles
        ↓
chart updates

The existing timeframe architecture was retained rather than replaced.

8. Crosshair Synchronization
Crosshair synchronization was investigated extensively.

The JavaScript chart provides:

getCrosshairMarketPosition(
    x,
    y
)

The X coordinate is converted into a market timestamp.

The other chart receives the timestamp through:

syncCrosshairFromPython(
    time
)

The receiving chart finds the nearest candle to that timestamp and uses its own candle data.

This is important because different charts may represent different instruments.

The synchronization intentionally does not copy the source chart's price.

Instead:

Source chart
    ↓
X coordinate
    ↓
Market timestamp
    ↓
Other chart
    ↓
Nearest local candle
    ↓
Local price

Result
Crosshair synchronization is working correctly.

9. Crosshair Debug Output
During development the terminal repeatedly showed:

[CROSSHAIR PYTHON] time=1785499980.0 price=0.0

This was diagnostic output only.

The crosshair synchronization itself does not depend on this print statement.

The recommendation is to remove the debug print() while keeping the actual crosshair functionality.

10. Chart Data Verification
We verified that JavaScript receives valid candle data.

Example:

[DEBUG] setChartData CALLED NIFTY2681124650PE true 1306

and:

[DEBUG] FIRST CANDLE
{"time":1785489300,"open":345.95,"high":345.95,"low":330.5,"close":330.5}

and:

[DEBUG] LAST CANDLE
{"time":1785943800,"open":154.3,"high":161.3,"low":154.25,"close":157.35}

The chart then successfully executes:

candleSeries.setData(data);

followed by:

chart.priceScale("right").applyOptions({
    autoScale: true
});

and:

chart.timeScale().fitContent();

Therefore the candle-data pipeline has been verified.

11. Chart Initialization Verification
The JavaScript console confirmed:

[DEBUG] LightweightCharts: object
[DEBUG] createChart: function
[DEBUG] CandlestickSeries: object
[DEBUG] CANDLE SERIES CREATED

and:

[CHART JS READY] slot=8 setChartData=function

This confirms that the JavaScript environment and Lightweight Charts library are loading correctly.

12. Chart Size Investigation
At one stage popup charts reported:

[DEBUG] chart size: 0 0

This helped identify that the popup chart could be initialized before its container had acquired its final dimensions.

The resize handling was subsequently strengthened using:

ResizeObserver

and:

chart.resize(
    chartContainer.clientWidth,
    chartContainer.clientHeight
);

The drawing canvas is resized at the same time.

Result
Popup charts now display correctly.

13. Resize Observer Issue
During development we temporarily encountered:

Cannot redeclare block-scoped variable 'resizeObserver'.

We searched the file and confirmed that only one declaration remained:

const resizeObserver =
    new ResizeObserver(...)

The final working version no longer has the redeclaration problem.

Do not add another const resizeObserver declaration without first checking the existing implementation.

14. Performance Instrumentation
Performance instrumentation was added/used during debugging to understand where time was being spent.

Examples included:

[PERF] refresh.excel_load

and:

[PERF] refresh.js_submit

Example observed values were very small, such as:

refresh.excel_load | time=0.08 ms
refresh.js_submit  | time=0.19 ms

This was useful for determining that the popup problem was not simply caused by slow Excel loading.

Performance instrumentation should not be confused with the functionality itself.

The diagnostic output can be removed later without removing the actual refresh/data-processing code.

15. Debug Terminal Output Cleanup
The application currently has several diagnostic messages that were useful during debugging.

Examples:

[DEBUG]
[CHART LOAD]
[CHART JS READY]
[PERF]
[CROSSHAIR PYTHON]

Now that the system is working, these messages should be cleaned up.

Important
Only remove the print() / logging statements.

Do NOT remove:

chart readiness checks
JavaScript submission
chart refresh logic
candle data processing
crosshair synchronization
resize handling
drawing logic
performance measurement code if it is still useful internally
The goal is:

Functional code → KEEP
Diagnostic terminal spam → REMOVE

16. Architectural Changes
There was no complete architectural rewrite.

The original application architecture remains.

Current structure:

Trading Dashboard
│
├── Main Dashboard
│
├── ChartSlot
│
├── PopupChartWindow
│
├── QWebEngineView
│
└── chart_test.html
        │
        └── Lightweight Charts

The V2 work consisted primarily of:

targeted bug fixes
popup state corrections
chart initialization fixes
canvas layering corrections
symbol synchronization
crosshair synchronization
resize handling
data-flow verification
performance diagnostics
This was deliberately done to avoid breaking the already-working src implementation.

17. Important Comparison Lesson: src vs ScrapCodes
During the investigation we compared the working code in src with the updated code in ScrapCodes.

This was important because src was already working correctly while the ScrapCodes version had popup-specific problems.

The main lesson is:

Do not assume the ScrapCodes version is automatically better because it is newer.

The working src implementation is the reference behavior.

Future changes should therefore follow:

Working src behavior
        ↓
Understand exact difference
        ↓
Make minimal change
        ↓
Test
        ↓
Commit

rather than:

Large architectural rewrite
        ↓
Hope everything still works

18. Current Known-Good State
At the end of 30-Aug-2026 testing:

MAIN WINDOW
    ✅ Loads
    ✅ Candles visible
    ✅ Script switching
    ✅ Timeframe switching
    ✅ Mouse interaction
    ✅ Crosshair
    ✅ Crosshair synchronization
    ✅ Drawings

POPUP WINDOW
    ✅ Opens
    ✅ Candles visible
    ✅ Script switching
    ✅ Timeframe switching
    ✅ Mouse interaction
    ✅ Crosshair
    ✅ Crosshair synchronization
    ✅ Drawings
    ✅ Resize

PYTHON → JAVASCRIPT
    ✅ Chart initialization
    ✅ setChartData()
    ✅ Candle data transfer
    ✅ candleSeries.setData()
    ✅ Auto-scale
    ✅ fitContent()

DRAWING SYSTEM
    ✅ Canvas exists
    ✅ Canvas does not hide candles
    ✅ Mouse remains functional
    ✅ Drawing redraw works

19. Immediate Next Step
Before any further optimization:

Step 1 — Remove diagnostic terminal prints
Clean:

[CROSSHAIR PYTHON]
[PERF] refresh.js_submit
[CHART JS READY]
[CHART LOAD]
[DEBUG]

Only remove their output statements.

Step 2 — Full regression test
Test:

Main window
    ↓
NIFTY
    ↓
SENSEX
    ↓
Option script
    ↓
Timeframe changes
    ↓
Crosshair
    ↓
Drawing

Then:

Popup
    ↓
NIFTY
    ↓
SENSEX
    ↓
Option script
    ↓
Timeframe changes
    ↓
Crosshair
    ↓
Drawing
    ↓
Resize
    ↓
Close/reopen popup

Step 3 — Create Git checkpoint
Once the regression test passes, commit the exact working state.

Recommended commit message:

V2 updated performance - stable charts and popup sync

This commit becomes the V2 Known-Good Baseline.

20. Development Plan From Tomorrow
Do not immediately modify chart architecture.

Continue in this order:

PHASE 1
Clean diagnostic logging
        ↓
PHASE 2
Full regression testing
        ↓
PHASE 3
Git V2 baseline checkpoint
        ↓
PHASE 4
Measure actual performance
        ↓
PHASE 5
Identify real bottlenecks
        ↓
PHASE 6
Optimize one bottleneck at a time
        ↓
PHASE 7
Regression test after every optimization

21. Performance Optimization Areas for V2
After the stable checkpoint is committed, investigate these areas in order:

1. Excel/data loading
        ↓
2. Data filtering
        ↓
3. Timeframe aggregation
        ↓
4. Python candle preparation
        ↓
5. Python → JavaScript payload
        ↓
6. JavaScript setData()
        ↓
7. Chart autoscaling
        ↓
8. fitContent()
        ↓
9. Drawing redraw
        ↓
10. Crosshair synchronization

We should measure before changing anything.

The objective is not simply to make individual operations faster.

The objective is to improve:

Dashboard responsiveness
Popup responsiveness
Chart refresh speed
Script switching speed
Timeframe switching speed
Crosshair responsiveness
Drawing responsiveness
Memory usage

while preserving all current functionality.

22. Rules for Continuing Development
From this checkpoint onward:

Rule 1
Do not make large changes to working chart code without a measured reason.

Rule 2
Do not change src and ScrapCodes simultaneously unless the difference is intentional.

Rule 3
Use the working src behavior as the reference when investigating regressions.

Rule 4
Change one functional area at a time.

Rule 5
Test after every significant change.

Rule 6
Commit every known-good milestone.

Rule 7
Do not remove functional code merely because it produced debug output.

Rule 8
Keep diagnostic logging separate from application logic.

23. Starting Point for the Next Session
When development resumes, start from:

V2 Updated Performance — 30-Aug-2026 — FUNCTIONALLY STABLE

Do NOT repeat the previous investigation unless a regression appears.

The first question should be:

"Is the V2 known-good baseline still working?"

If yes:

Clean logs
    ↓
Commit baseline
    ↓
Measure performance
    ↓
Optimize

If no:

Identify regression
    ↓
Compare with known-good commit
    ↓
Fix only the regression
    ↓
Retest

24. Final V2 Checkpoint
V2 Updated Performance — 30-Aug-2026

Status:

FUNCTIONALLY STABLE / READY FOR PERFORMANCE OPTIMIZATION

The major popup/chart/drawing/crosshair issues have been resolved.

The next development phase is performance measurement and controlled optimization, not another architectural rewrite.
