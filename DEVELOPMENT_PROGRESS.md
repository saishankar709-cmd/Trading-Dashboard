Trading Dashboard — Development Progress Notes
1. Project foundation

Project: Trading-Dashboard

GitHub repository: Trading-Dashboard

Local project:

D:\Coding\Trading-Dashboard

Python virtual environment:

D:\Coding\Trading-Dashboard\.venv

The application is being developed as a PySide6 desktop trading dashboard with embedded HTML/JavaScript charts.

2. Current architecture

The project currently has three important layers:

Python / PySide6
        │
        ├── Trading Dashboard window
        ├── ChartSlot instances
        ├── chart selection
        ├── timeframe handling
        ├── Excel/data loading
        └── QWebChannel bridge
                │
                ▼
        HTML / JavaScript
                │
                ├── Lightweight Charts
                ├── candle rendering
                ├── crosshair
                ├── drawing tools
                └── drawing interaction
3. Folder structure

The local structure we've been working with is approximately:

Trading-Dashboard/
│
├── .venv/
│
├── src/
│   │
│   ├── main.py
│   ├── main_backup.py
│   │
│   ├── data/
│   │   └── excel_loader.py
│   │
│   └── web/
│       │
│       ├── chart_test.html
│       ├── chart_test_backup.html
│       └── lightweight-charts.js
│
└── ...
Important files
src/main.py

Main PySide6 application.

Responsible for:

Main window
Dashboard layout
Multiple chart slots
Chart selection
Active chart highlighting
Timeframe controls
Sheet selection
Data loading
QWebEngineView
QWebChannel
Python ↔ JavaScript communication
Crosshair synchronization
src/web/chart_test.html

Main chart implementation.

Responsible for:

Lightweight Charts
Candlestick data
Crosshair
Drawing tools
Rectangle
Trend line
Horizontal line
Vertical line
Drawing selection
Drawing movement
Drawing resizing
Drawing deletion
JavaScript-side chart interaction
src/web/lightweight-charts.js

Charting library used by the HTML chart.

src/data/excel_loader.py

Used for loading trading data from Excel/data files.

Current data folder configured in Python:

D:\DataP\Files
4. ChartSlot development

We implemented multiple chart slots.

Each chart has:

Chart 1
Chart 2
...

A chart slot contains:

Header
Sheet name
Timeframe label
Chart browser
Active/inactive state
Mouse tracking
Drawing interaction
Crosshair interaction
Active chart

Clicking a chart changes the active slot.

Example terminal output:

[CLICK] ChartSlot 2
[ACTIVE] ChartSlot 2

This is currently working.

5. Chart selection

We implemented chart selection using:

self.parent.set_active_slot(
    self.slot_id
)

The active chart receives a blue border.

Inactive chart:

border: 1px solid #d5d5d5

Active chart:

border: 2px solid #1976d2

The title also changes color/weight when active.

6. Drawing system

A substantial amount of work has been completed on the drawing system.

Current drawing types include:

rectangle
trend
horizontal
vertical

The HTML drawing engine maintains drawings in market coordinates.

For two-point drawings, we use:

drawing.first
drawing.second

with:

{
    time,
    price
}

This was important because drawings need to survive timeframe changes.

7. Rectangle functionality

We specifically worked on rectangle interaction.

The rectangle supports:

Create
Move
Resize
Delete

The resize/move logic is implemented around:

function resizeOrMoveRectangle(...)

and:

function moveTwoPointDrawing(...)

The rectangle has different drag modes such as:

move
topLeft
topRight
bottomLeft
bottomRight

etc.

8. Important drawing bug we fixed

Initially:

Rectangle could be created, resized and deleted, but could not properly move.

We traced this through:

pointerdown
      ↓
hitTestDrawing()
      ↓
dragMode
      ↓
dragStartPoint
      ↓
dragOriginal
      ↓
pointermove
      ↓
moveTwoPointDrawing()

We discovered that the movement was dependent on converting screen coordinates into market coordinates.

The relevant functions are:

screenToMarketPoint()

and:

getLocalPosition()

Current conversion:

chart.timeScale().coordinateToTime(x)

and:

candleSeries.coordinateToPrice(y)

This allows drawings to be stored in market coordinates instead of screen coordinates.

Result

The rectangle movement issue was fixed and you confirmed:

done working

9. Timeframe changes

We also made the drawing system preserve drawings when timeframe changes.

The important function is:

function setChartData(data, sheetName)

The design decision was:

Do NOT clear drawings when changing timeframe.

Instead:

candleSeries.setData(data)

is performed while existing drawings remain stored.

After chart data updates:

redrawDrawings();

is called.

This allows drawings to be reconstructed from their market coordinates.

10. QWebChannel integration

We introduced a Python/JavaScript bridge.

Python:

class ChartBridge(QObject):

with signals/slots.

The browser registers:

self.channel = QWebChannel(
    self.browser.page()
)

and:

self.channel.registerObject(
    "chartBridge",
    self.bridge
)

JavaScript accesses the bridge through:

chartBridge

This gives us Python ↔ JavaScript communication.

11. Chart click communication

The JavaScript chart can notify Python when a chart is clicked.

The Python side ultimately calls:

self.select

and then:

self.parent.set_active_slot(
    self.slot_id
)

This is working.

12. Crosshair synchronization

This is the current development area.

The goal is:

Mouse over Chart 1
        ↓
Chart 1 determines market timestamp
        ↓
Python receives timestamp
        ↓
Python sends timestamp to other charts
        ↓
Each chart finds its nearest candle
        ↓
Each chart displays its own crosshair

This approach is important because different charts may have:

Different instruments
Different timeframes
Different price values

Therefore we decided not to synchronize the source chart's price.

Instead, synchronize the time.

13. Current crosshair JavaScript design

The chart has:

function getCrosshairMarketPosition(
    x,
    y
)

It converts the mouse X coordinate to a market timestamp.

The important part is:

chart.timeScale()
    .coordinateToTime(
        chartX
    );

The result is essentially:

{
    time: Number(time)
}
14. Crosshair synchronization target

Python has:

def sync_crosshair(
    self,
    source_slot_id,
    time
):

The target charts receive:

syncCrosshairFromPython(time)

Each target chart searches:

currentDataTimes

for the nearest timestamp.

Then it retrieves that chart's own candle:

const candle =
    currentCandleData[
        nearestIndex
    ];

and uses:

candle.close

for that chart's crosshair price.

So the intended behavior is:

Chart 1
timestamp = 10:35
        │
        ▼
Chart 2 finds nearest 10:35 candle
        │
        ▼
Chart 2 uses its own close price

This is the correct architecture for multi-chart synchronization.

15. Crosshair mouse-leave behavior

We also have:

clearSyncedCrosshair()

and Python:

clear_synced_crosshair(
    source_slot_id
)

The intention is:

Mouse leaves Chart 1
        ↓
Chart 2 / other charts
        ↓
Clear synchronized crosshair
16. Issue encountered during crosshair development

During the crosshair changes, we temporarily added:

self.bridge.mouse_moved.connect(
    self.market_mouse_moved
)

but ChartSlot did not contain:

market_mouse_moved()

This caused:

AttributeError:
'ChartSlot' object has no attribute 'market_mouse_moved'

We subsequently removed that invalid connection.

You confirmed:

done working fine.

The application is currently running again.

17. Important current baseline

At the moment, the safest known working baseline is:

Application launches
        ✓
Chart slots work
        ✓
Chart selection works
        ✓
Active chart highlighting works
        ✓
Rectangle creation works
        ✓
Rectangle resizing works
        ✓
Rectangle deletion works
        ✓
Rectangle movement works
        ✓
Timeframe changes work
        ✓
Drawing preservation architecture exists
        ✓
QWebChannel exists
        ✓
Crosshair synchronization
        → still being developed/tested
18. Backup files

We created:

src/main_backup.py
src/web/chart_test_backup.html

Current verification showed:

main.py
    ==
main_backup.py

and:

chart_test.html
    ==
chart_test_backup.html

So these backups are currently snapshots of the same modified state, not an older clean version.

This is important for future work: we should create a new dated/versioned backup before making the next significant change.

For example:

src/backups/

could eventually contain:

main_v001.py
main_v002.py
main_v003.py

chart_test_v001.html
chart_test_v002.html
chart_test_v003.html

That would be much safer than repeatedly overwriting main_backup.py.

19. GitHub ScrapCodes

You also decided to maintain experimental/development code under:

Trading-Dashboard/
└── ScrapCodes/

The purpose is to keep experimental code separate from the main production/application code.

This is where we can put:

ScrapCodes/
├── experiments/
├── backups/
├── old_versions/
├── chart_tests/
└── notes/

as the project grows.

We should not mix experimental files into src/ unless they become part of the actual application.

20. Recommended development rule going forward

From this point, I recommend we use this workflow:

1. Backup current working code
        ↓
2. Make ONE change
        ↓
3. py_compile / syntax check
        ↓
4. Run application
        ↓
5. Test
        ↓
6. Confirm working
        ↓
7. Commit to GitHub
        ↓
8. Move to next change

Especially for main.py, we should avoid commands that rewrite the entire file unnecessarily because that caused the special-character/encoding problem earlier.

Current milestone
Milestone 1 — Multi-chart dashboard

Status: Working

Milestone 2 — Interactive drawings

Status: Working

Milestone 3 — Drawing persistence across timeframe changes

Status: Implemented

Milestone 4 — Crosshair synchronization

Status: In progress

Milestone 5 — Production cleanup/versioned backups

Status: Not started

Milestone 6 — GitHub cleanup/documentation

Status: In progress
