# Trading Dashboard — Development Progress

## Project Status

**Current Status:** Layout module under active development  
**Last Working Baseline:** GitHub-synced project copy  
**Current Priority:** Stabilize multi-layout architecture before proceeding to Custom Layout Mapping / Pop-Out

---

# 1. Project Foundation

## Completed

- Python/PySide6 desktop application established.
- `QWebEngineView` integrated for web-based chart rendering.
- Trading chart implemented using Lightweight Charts.
- Local Lightweight Charts JavaScript file integrated.
- Project structure established:

```text
Trading-Dashboard/
│
├── src/
│   ├── main.py
│   │
│   └── web/
│       ├── chart_test.html
│       └── lightweight-charts.js
│
└── ...
2. Chart Module
Completed
Candlestick chart implemented.
Closing-price line removed.
Candlestick OHLC data displayed.
Chart zooming/panning implemented through Lightweight Charts.
Local Lightweight Charts library integrated.
Chart loads through PySide6/QWebEngineView.
3. Timeframe Module
Completed

Timeframe functionality has been implemented for:

1 minute
3 minutes
5 minutes
10 minutes
15 minutes
30 minutes
1 hour
4 hours
1 day

The architecture supports changing the timeframe of the active chart.

Remaining Work

In multi-layout mode:

Each chart must be independently changeable.
Selecting a timeframe must affect only the selected/active chart.
Timeframe state must remain associated with its chart.
Switching layouts must not unexpectedly reset chart timeframes.
4. Drawing Module
Implemented Drawing Types
Trend Line
Horizontal Line
Vertical Line
Rectangle
Drawing Functionality Implemented
Drawing creation.
Drawing selection.
Drawing movement.
Drawing resizing.
Drawing deletion.
Drawing color functionality.
Drawing state stored within chart instances.
Drawing interaction across chart coordinates implemented.
Known Issues

The drawing module is not yet fully stable in multi-layout mode.

Known/observed problems:

Drawing behavior is inconsistent between multiple charts.
Drawing controls currently appear inside individual chart instances.
Drawing controls need to be centralized into the main dashboard.
Drawings must operate only on the currently active chart.
Each chart must maintain its own independent drawing collection.
Drawing state must survive layout changes.
Drawing interaction must not affect another chart.
5. Drawings Menu
Design Requirement

Drawing tools should NOT appear as permanent controls inside every chart.

Required design:

Drawings ▼
│
├── Trend Line
├── Horizontal Line
├── Vertical Line
└── Rectangle

The selected drawing tool must apply only to the currently active chart.

Current Status

Not completed.

The current implementation still contains drawing-related UI inside the chart HTML.

This must be removed/refactored.

6. Multi-Layout Module
Implemented

Layout engine has been introduced.

Supported layout concepts include:

1 chart
2 charts
3 charts
4 charts
6 charts
8 charts

Chart slots were introduced so that multiple chart instances can exist simultaneously.

The architecture includes the concept of:

ChartSlot

Each chart slot is intended to maintain its own:

Symbol
Sheet
Timeframe
Chart instance
Drawings
Chart state
7. Current Multi-Layout Problems
IMPORTANT

Multi-layout functionality is NOT currently considered complete or stable.

The following issues remain unresolved.

7.1 Mouse / Crosshair Synchronization

Required behavior:

Mouse over Chart 1
        ↓
Crosshair position
        ↓
Chart 2
Chart 3
Chart 4
...

The crosshair should synchronize based on market time/data rather than simply copying screen coordinates.

Current Status

NOT WORKING CORRECTLY.

Crosshair synchronization has not been successfully completed.

8. Independent Timeframe Per Chart

Required behavior:

Chart 1 → 1 minute
Chart 2 → 5 minute
Chart 3 → 15 minute
Chart 4 → 1 day

Changing Chart 3 to 15 minutes must not modify Charts 1, 2 or 4.

Current Status

Partially implemented in the Python architecture, but not yet verified/stable in the complete multi-layout environment.

Needs full testing.

9. Independent Drawings Per Chart

Required behavior:

Chart 1
 └── Trend Line A

Chart 2
 └── Rectangle B

Chart 3
 └── Horizontal Line C

Drawings must remain associated with their respective chart.

Current Status

Drawing state is implemented within individual HTML chart instances, but multi-layout interaction is not yet fully stable.

Needs architectural cleanup and testing.

10. Active Chart Selection

Required behavior:

When a chart is clicked:

Chart 2
   ↓
becomes ACTIVE
   ↓
Toolbar controls operate on Chart 2

Therefore:

Timeframe
Drawings
Symbol
Chart options

must operate on the selected chart.

Current Status

Active chart architecture exists.

However, recent changes introduced an issue involving:

ClickableChartView.mouse_left

which caused:

AttributeError:
'ClickableChartView' object has no attribute 'mouse_left'

A correction was attempted using the existing clicked signal.

This needs to be re-tested from a clean GitHub checkpoint tomorrow.

11. Drawing Box Problem

Current behavior:

Each chart instance can display its own drawing control box.

This is NOT the desired design.

Required Design

Only the main dashboard should contain:

Drawings ▼

The chart itself should contain only the chart.

No permanent drawing control box should appear on every chart.

Current Status

NOT COMPLETED.

12. Layout State Persistence

Required behavior:

If:

Chart 1 → NIFTY → 1m
Chart 2 → BANKNIFTY → 5m
Chart 3 → SENSEX → 15m

then changing:

1 layout → 4 layout → 2 layout → 4 layout

should preserve the chart configuration.

Each slot should retain its:

Symbol
Timeframe
Drawings
Chart settings
Data state
Current Status

NOT YET VERIFIED.

13. Custom Layout Mapping
Planned

After basic layouts are stable, implement custom layout mapping.

Example:

Layout A

┌──────────────────────┬───────────┐
│                      │           │
│       Chart 1        │ Chart 2   │
│                      │           │
├──────────────┬───────┴───────────┤
│   Chart 3    │      Chart 4      │
└──────────────┴────────────────────┘

User should be able to define which chart occupies which position.

Status

NOT STARTED.

14. Pop-Out Chart
Planned Requirement

From a multi-chart layout:

┌──────────────┬──────────────┐
│   Chart 1    │   Chart 2    │
├──────────────┼──────────────┤
│   Chart 3    │   Chart 4    │
└──────────────┴──────────────┘

User should be able to select one chart and choose:

Pop Out

Result:

┌─────────────────────────────────────┐
│                                     │
│             Chart 3                 │
│                                     │
│       Full-size analysis view       │
│                                     │
└─────────────────────────────────────┘

The chart must retain:

Symbol
Timeframe
Drawings
Chart settings
Current data
Status

NOT STARTED.

15. Planned Chart Options

Every chart in every layout should eventually support the same chart controls.

Required capabilities include:

Timeframe
Drawings
Drawing color
Chart type
Zoom
Pan
Crosshair
Indicators
Price scale options
Chart settings
Symbol selection
Data visibility controls

These controls must operate on the active chart.

Status

PARTIALLY IMPLEMENTED.

16. Testing Status

Basic single-chart functionality has previously been tested successfully.

However, the current multi-layout implementation has NOT passed complete integration testing.

Required Testing Matrix
Layouts
 1 chart
 2 charts
 3 charts
 4 charts
 6 charts
 8 charts
Timeframes

Each visible chart must independently support:

 1m
 3m
 5m
 10m
 15m
 30m
 1h
 4h
 1D
Drawings

For every chart:

 Trend line
 Horizontal line
 Vertical line
 Rectangle
 Select
 Move
 Resize
 Delete
 Change color
 Create multiple drawings
Layout State
 Change timeframe
 Add drawing
 Switch layout
 Return to previous layout
 Verify state retained
Crosshair
 Chart 1 → Chart 2
 Chart 2 → Chart 1
 Chart 1 → all visible charts
 Different timeframes
 Different symbols
 Different chart sizes
17. Current Known Errors

The latest local execution produced:

AttributeError:
'ClickableChartView' object has no attribute 'mouse_left'

Location:

src/main.py

The application was attempting to connect:

self.browser.mouse_left.connect(...)

while the current ClickableChartView implementation does not expose that signal.

A correction using the existing clicked signal was attempted.

This must be verified from the latest clean GitHub copy before proceeding.

18. Important Development Rule Going Forward

Because the project has become large, avoid piecemeal code insertion unless the exact insertion point is clearly identified.

For every module:

1. Establish working GitHub checkpoint
2. Inspect current code
3. Make ONE architectural change
4. Run application
5. Test the change
6. Commit to GitHub
7. Create development checkpoint
8. Move to next change

Do NOT mix:

Layout changes
Drawing changes
Crosshair changes
Timeframe changes

in one uncontrolled edit.

19. Immediate Next Session Plan
Step 1 — Recovery

Start from the latest confirmed working GitHub copy.

Do not make additional edits until:

python src\main.py

starts successfully.

Step 2 — Stabilize ChartSlot

Verify:

ChartSlot
 ├── browser
 ├── symbol
 ├── timeframe
 ├── drawings
 └── active state
Step 3 — Fix Active Chart

Clicking a chart must reliably make it the active chart.

Step 4 — Fix Independent Timeframes

Verify every visible chart can independently use:

1m / 3m / 5m / 10m / 15m / 30m /
1h / 4h / 1D
Step 5 — Remove Drawing Box

Move all drawing controls to:

Drawings ▼

in the main toolbar.

Step 6 — Stabilize Drawings

Verify every chart can independently:

Create
Select
Move
Resize
Delete
Change Color

drawings.

Step 7 — Crosshair Synchronization

Implement proper time-based crosshair synchronization.

Important:

Do not synchronize raw pixel coordinates.

Charts can have:

different dimensions
different timeframes
different symbols

Therefore synchronization should be based on market time.

Step 8 — Full Layout Testing

Test:

1 → 2 → 3 → 4 → 6 → 8

and back again.

Step 9 — Custom Layout Mapping

Only after the basic layout engine is stable.

Step 10 — Pop-Out

Implement selected-chart pop-out after layout mapping is stable.

20. Overall Progress
Module	Status
Project foundation	✅ Complete
PySide6 application	✅ Complete
Lightweight Charts	✅ Complete
Candlestick chart	✅ Complete
Closing line removal	✅ Complete
Timeframes	🟡 Partially complete
Trend line	🟡 Implemented / needs multi-layout validation
Horizontal line	🟡 Implemented / needs multi-layout validation
Vertical line	🟡 Implemented / needs multi-layout validation
Rectangle	🟡 Implemented / needs multi-layout validation
Drawing color	🟡 Implemented / needs UI redesign
Drawing selection	🟡 Needs multi-layout validation
Drawing movement	🟡 Needs multi-layout validation
Drawing resize	🟡 Needs multi-layout validation
Drawing deletion	🟡 Needs multi-layout validation
Layout engine	🟡 In development
Active chart	🟡 Needs stabilization
Per-chart timeframe	🟡 Needs stabilization
Per-chart drawings	🟡 Needs stabilization
Crosshair synchronization	❌ Not working
Drawing box removal	❌ Not completed
Layout state persistence	❌ Not verified
Custom layout mapping	⏳ Not started
Pop-out chart	⏳ Not started
Complete integration testing	❌ Not completed
21. Current Project Direction

The long-term architecture is:

Trading Dashboard
│
├── Dashboard
│
├── Layout Manager
│
├── Chart Slot Manager
│
├── Chart Engine
│
├── Timeframe Manager
│
├── Drawing Manager
│
├── Crosshair Synchronizer
│
├── Indicator Manager
│
├── Custom Layout Manager
│
└── Pop-Out Manager

The goal is for every chart in every layout to behave like a complete independent trading chart, while the dashboard controls the active chart and provides synchronized analysis functionality.

END OF CURRENT DEVELOPMENT CHECKPOINT

### Tomorrow's starting point

We should **not continue from tonight's broken state**.

We'll start by:

**GitHub → latest correct checkpoint → run → verify → checkpoint → fix active chart → fix timeframes → fix drawings → crosshair.**

And importantly, **the layout issues are explicitly recorded as unfinished**. We will not mark the layout module complete until those tests actually pass.
