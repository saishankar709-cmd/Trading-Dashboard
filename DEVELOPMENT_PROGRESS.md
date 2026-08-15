TRADING DASHBOARD — DEVELOPMENT PROGRESS / HANDOFF NOTES
1. PROJECT IDENTITY
Project name: Trading Dashboard

Local project root:

D:\Coding\Trading-Dashboard

Operating environment:

Windows
PowerShell
Python virtual environment (.venv)

Virtual environment:

D:\Coding\Trading-Dashboard\.venv

The normal terminal prompt is:

(.venv) PS D:\Coding\Trading-Dashboard>

2. CURRENT LOCAL PROJECT STRUCTURE
The current PC folder structure is:

D:\Coding\Trading-Dashboard
│
├── .venv
│   ├── Include
│   ├── Lib
│   └── Scripts
│
├── .gitignore
├── pyvenv.cfg
│
├── src
│   │
│   ├── __pycache__
│   │
│   ├── charts
│   │
│   ├── data
│   │
│   ├── ui
│   │
│   ├── web
│   │   ├── chart_test_backup_20260813_071320.html
│   │   ├── chart_test_backup.html
│   │   ├── chart_test.html
│   │   └── lightweight-charts.js
│   │
│   ├── main_backup_20260813_071320.py
│   ├── main_backup.py
│   └── main.py
│
├── tests
│
├── DEVELOPMENT_PROGRESS.md
├── sync_javascript.txt
└── sync_python_sections.txt

Important source files:

D:\Coding\Trading-Dashboard\src\main.py
D:\Coding\Trading-Dashboard\src\web\chart_test.html
D:\Coding\Trading-Dashboard\src\web\lightweight-charts.js

3. BACKUP STRUCTURE
There are already multiple local backup files.

Current backups:

D:\Coding\Trading-Dashboard\src\main_backup.py

D:\Coding\Trading-Dashboard\src\main_backup_20260813_071320.py

D:\Coding\Trading-Dashboard\src\web\chart_test_backup.html

D:\Coding\Trading-Dashboard\src\web\chart_test_backup_20260813_071320.html

The timestamped backups:

main_backup_20260813_071320.py
chart_test_backup_20260813_071320.html

represent a dated local backup point.

The normal backups:

main_backup.py
chart_test_backup.html

are also retained.

IMPORTANT BACKUP RULE
Do NOT automatically create another backup file.

Before making major changes, inspect the existing backups and GitHub state first.

If a new backup is specifically required, ask/confirm before creating additional files.

4. GITHUB
The project is synchronized with:

https://github.com/saishankar709-cmd/Trading-Dashboard

The latest working code was manually synced to GitHub after the crosshair synchronization work.

GitHub is the remote recovery point.

The local PC backups are the local recovery points.

Therefore the project currently has:

LOCAL WORKING CODE
        +
LOCAL BACKUPS
        +
GITHUB COPY

5. CURRENT DEVELOPMENT STATUS
Major completed milestone
Multi-chart crosshair synchronization
STATUS: COMPLETE / WORKING

The crosshair now synchronizes correctly between visible chart layouts.

The original problem was:

Crosshair was visible on the chart where the mouse was placed, but it did not appear correctly on the other charts/layouts.

This has now been fixed.

6. CHART SLOT ARCHITECTURE
The dashboard supports multiple chart slots.

Current chart slots include:

ChartSlot 1
ChartSlot 2
ChartSlot 3
ChartSlot 4

The application can display different layouts containing different numbers of visible chart slots.

Each chart slot has its own:

QWebEngineView
JavaScript chart
Lightweight Charts instance
Candlestick series
QWebChannel bridge
mouse handling
chart data
timeframe
instrument/sheet
crosshair state
The Python dashboard coordinates the visible chart slots.

7. ACTIVE CHART SELECTION
Each chart slot can become the active chart.

The Python dashboard maintains:

self.active_slot_id

The chart slot calls:

self.parent.set_active_slot(
    self.slot_id
)

Temporary debug messages such as:

[ACTIVE] ChartSlot 1
[CLICK] ChartSlot 1

were used during development.

These messages were removed/cleaned up because they are not needed during normal application operation.

8. CROSSHAIR SYNCHRONIZATION DESIGN
The synchronization architecture is intentionally based on time, not shared price.

This is important because different charts can represent different instruments.

The flow is:

SOURCE CHART
     │
     │ mouse movement
     ▼
browser mouse coordinates
     │
     ▼
JavaScript
     │
     │ X coordinate → market timestamp
     ▼
Python
     │
     │ timestamp
     ▼
other visible chart slots
     │
     ▼
each chart finds its own nearest candle
     │
     ▼
each chart uses its own candle close
     │
     ▼
destination crosshair

Therefore:

Do not synchronize the source chart's price to another instrument.

Only the market timestamp should be synchronized.

9. PYTHON QWEBCHANNEL BRIDGE
In:

D:\Coding\Trading-Dashboard\src\main.py

the JavaScript bridge contains:

mouse_moved = Signal(float, float)

and:

@Slot(float, float)
def chart_mouse_moved(self, time, price):
    self.mouse_moved.emit(
        time,
        price
    )

The bridge is connected to:

self.bridge.mouse_moved.connect(
    self.chart_crosshair_moved
)

The chart slot contains:

def chart_crosshair_moved(
    self,
    time,
    price
):

The price argument exists because the bridge currently emits both time and price.

However, for synchronizing different instruments, time is the important value.

The destination chart calculates its own price.

Do not unnecessarily redesign this working bridge unless required by a future feature.

10. BROWSER MOUSE HANDLING
The custom browser widget contains:

mouse_moved = Signal(int, int)
mouse_left = Signal()

Mouse tracking is enabled.

Mouse movement emits:

self.mouse_moved.emit(
    int(pos.x()),
    int(pos.y())
)

When the mouse leaves:

self.mouse_left.emit()

The chart slot connects browser movement to its own mouse handling.

This allows Python to obtain browser coordinates and ask JavaScript to determine the corresponding market timestamp.

11. JAVASCRIPT CHART BRIDGE
In:

D:\Coding\Trading-Dashboard\src\web\chart_test.html

the bridge is initialized using:

let chartBridge = null;

new QWebChannel(
    qt.webChannelTransport,
    function(channel) {
        chartBridge = channel.objects.chartBridge;
    }
);

The chart container handles pointer interaction.

The chart click handler calls:

chartBridge.chart_clicked();

The chart mouse position is converted into a market timestamp.

12. SOURCE CROSSHAIR POSITION
The source chart converts the mouse X coordinate to chart-local coordinates.

The market timestamp is obtained using:

chart.timeScale()
    .coordinateToTime(chartX);

The important design decision is:

X coordinate
    ↓
market timestamp

The source chart's price is deliberately not used for positioning the crosshair on another instrument.

13. DESTINATION CROSSHAIR FUNCTION
The JavaScript function is:

function syncCrosshairFromPython(
    time
)

It first checks that chart data exists.

It converts the incoming time:

const targetTime =
    Number(time);

It verifies that the value is finite.

Then it searches:

currentDataTimes

for the nearest candle timestamp.

The nearest candle is selected using the smallest absolute difference:

abs(destination candle time - source time)

Once the nearest candle is found:

const candle =
    currentCandleData[
        nearestIndex
    ];

The destination chart gets its own price:

const price =
    Number(candle.close);

This is the correct behavior for multi-instrument charts.

14. LIGHTWEIGHT CHARTS "VALUE IS NULL" PROBLEM
During development, repeated JavaScript errors appeared:

js: Uncaught Error: Value is null

The error happened while positioning the synchronized crosshair.

The problematic operation was effectively:

chart.setCrosshairPosition(
    price,
    nearestTime,
    candleSeries
);

The important discovery was that having a valid candle timestamp does not guarantee that Lightweight Charts currently has a valid chart coordinate for that timestamp.

Therefore:

chart.timeScale()
    .timeToCoordinate(nearestTime)

can return:

null

or:

undefined

15. FINAL FIX FOR "VALUE IS NULL"
The synchronized crosshair code now validates the coordinate before calling setCrosshairPosition().

Current logic:

const coordinate =
    chart.timeScale()
        .timeToCoordinate(
            nearestTime
        );

if (
    coordinate === null ||
    coordinate === undefined ||
    !Number.isFinite(
        Number(coordinate)
    )
) {
    return;
}

Only after this validation:

chart.setCrosshairPosition(
    price,
    nearestTime,
    candleSeries
);

This fixed the repeated:

Value is null

errors.

The application was run again after the fix and the errors disappeared.

IMPORTANT
Do not remove this coordinate validation.

It is an important defensive check around Lightweight Charts.

16. CROSSHAIR CLEARING
When the mouse leaves the source chart, synchronized crosshairs are cleared.

Python contains:

def mouse_left(self):
    self.parent.clear_synced_crosshair(
        self.slot_id
    )

The dashboard has:

def clear_synced_crosshair(
    self,
    source_slot_id
):

JavaScript contains:

function clearSyncedCrosshair() {
    if (
        typeof chart.clearCrosshairPosition
        === "function"
    ) {
        chart.clearCrosshairPosition();
    }
}

This removes the synchronized crosshair from charts when appropriate.

17. CANDLE SERIES
The candlestick series is created with:

LightweightCharts.CandlestickSeries

Current colors:

Up candle:
#26a69a

Down candle:
#ef5350

The corresponding borders and wicks use the same colors.

The chart currently has:

lastValueVisible: false

and:

priceLineVisible: false

18. DATA / TIMEFRAME ENGINE
The Python timeframe engine is:

def prepare_timeframe(
    self,
    df,
    timeframe
):

The dataframe is copied:

df = df.copy()

Empty data is handled:

if df.empty:
    return df

Timestamp conversion:

df["timestamp"] = pd.to_datetime(
    df["timestamp"]
)

Data is sorted chronologically:

df.sort_values(
    "timestamp"
)

and the index is reset.

For:

1m

the dataframe is returned directly.

19. DAILY TIMEFRAME
For:

1D

data is grouped using:

df["timestamp"].dt.date

Aggregation:

Open  = first
High  = max
Low   = min
Close = last

The resulting dataframe is returned as daily candles.

20. INTRADAY TIMEFRAMES
Intraday aggregation uses the configured timeframe minutes.

The trading session begins at:

09:15

The code calculates the number of minutes from the session start and uses that to determine the candle bucket.

The resulting candles are sorted/grouped chronologically.

21. CHART DATA TRANSFER
Python builds candle dictionaries like:

{
    "time": int(
        row["timestamp"].timestamp()
    ),
    "open": float(row["Open"]),
    "high": float(row["High"]),
    "low": float(row["Low"]),
    "close": float(row["Close"]),
}

The candle list is sent to JavaScript through:

setChartData(
    json.dumps(candles),
    json.dumps(slot.sheet)
);

The timestamp is currently represented as Unix seconds.

22. IMPORTANT DATA OBSERVATION
During investigation, searches were performed for:

drop_duplicates
isna
isnull
isfinite
nan
inf

No corresponding dataframe-cleaning logic was found in the searched section.

This was investigated while diagnosing the JavaScript "Value is null" errors.

The final root cause was not bad candle data.

The issue was the Lightweight Charts coordinate lookup returning null for a requested timestamp.

Therefore the final fix was placed in the JavaScript crosshair synchronization logic rather than unnecessarily changing the dataframe pipeline.

23. TEMPORARY DEBUGGING OUTPUT
During development the following diagnostic messages were used:

[ACTIVE] ChartSlot ...
[CLICK] ChartSlot ...
[MOUSE MOVED] ...
[CROSSHAIR] ...

These helped verify:

active chart selection
chart clicks
mouse movement
crosshair synchronization
After functionality was verified, unnecessary terminal logging was removed.

Normal startup should not continuously print these debugging messages.

24. PYTHON SYNTAX VERIFICATION
The following command was used successfully:

python -m py_compile src\main.py

Successful compilation produces no output.

This should be run after Python changes.

25. APPLICATION START COMMAND
The normal application command is:

python src\main.py

The application was successfully launched after the final crosshair fix.

The latest test produced no:

js: Uncaught Error: Value is null

messages.

26. USEFUL POWERSHELL COMMANDS
Search Python source:

Select-String -Path src\main.py -Pattern "pattern" -Context 5,15

Search JavaScript:

Select-String -Path src\web\chart_test.html -Pattern "pattern" -Context 5,15

Inspect a section:

Get-Content src\web\chart_test.html | Select-Object -Skip <line> -First <count>

Inspect Python section:

Get-Content src\main.py | Select-Object -Skip <line> -First <count>

Compile Python:

python -m py_compile src\main.py

Run application:

python src\main.py

27. DEVELOPMENT DOCUMENTS
The project currently contains:

DEVELOPMENT_PROGRESS.md
sync_javascript.txt
sync_python_sections.txt

These files are intended to help maintain continuity between development sessions.

DEVELOPMENT_PROGRESS.md should be updated after major milestones.

28. IMPORTANT FUTURE-SESSION INSTRUCTIONS
When continuing development, first assume the current crosshair implementation is a working baseline.

Before changing it:

Open the current source files.
Check the existing implementation.
Do not blindly replace working code.
Preserve the timestamp-based synchronization architecture.
Preserve nearest-candle matching.
Preserve destination-chart-specific prices.
Preserve timeToCoordinate() validation.
Preserve crosshair clearing.
Preserve multi-layout behavior.
Preserve drawing functionality.
Preserve timeframe functionality.
If a new change causes an error, diagnose the exact existing flow before modifying unrelated code.

29. BACKUP POLICY FOR FUTURE DEVELOPMENT
Existing backups are:

src\main_backup.py
src\main_backup_20260813_071320.py

src\web\chart_test_backup.html
src\web\chart_test_backup_20260813_071320.html

Do not create another backup simply because a new development session starts.

Before a major change:

1. Check current working code.
2. Check existing backups.
3. Check GitHub sync status.
4. Make the change.
5. Test.
6. If successful, sync to GitHub when appropriate.

30. CURRENT RECOVERY POINT
The current project has three levels of protection:

LEVEL 1
Current working files

D:\Coding\Trading-Dashboard\src\main.py
D:\Coding\Trading-Dashboard\src\web\chart_test.html


LEVEL 2
Local backups

D:\Coding\Trading-Dashboard\src\main_backup.py
D:\Coding\Trading-Dashboard\src\main_backup_20260813_071320.py

D:\Coding\Trading-Dashboard\src\web\chart_test_backup.html
D:\Coding\Trading-Dashboard\src\web\chart_test_backup_20260813_071320.html


LEVEL 3
GitHub remote repository

https://github.com/saishankar709-cmd/Trading-Dashboard

The latest working code has been synced to GitHub.

31. CURRENT MILESTONE
MILESTONE: MULTI-CHART CROSSHAIR SYNCHRONIZATION
STATUS: COMPLETE

Completed functionality:

Mouse crosshair works on source chart.
Source chart determines market timestamp.
Timestamp is sent through Python.
Other visible charts receive the timestamp.
Each destination chart finds its nearest candle.
Each destination chart uses its own close price.
Crosshair is positioned on destination charts.
Different instruments can therefore synchronize correctly.
Mouse leave clears synchronized crosshairs.
Lightweight Charts null-coordinate issue is handled.
"Value is null" errors are resolved.
Temporary debug terminal messages have been removed.
Python syntax has been verified.
Application has been successfully executed.
Local backups exist.
Latest working code has been synced to GitHub.
32. NEXT DEVELOPMENT SESSION
Start from:

D:\Coding\Trading-Dashboard

Activate .venv if necessary:

.\.venv\Scripts\Activate.ps1

Then verify:

python -m py_compile src\main.py

Then run:

python src\main.py

First confirm:

Application launches
Charts load
Multiple layouts work
Chart selection works
Crosshair works
Crosshair synchronizes
No "Value is null" errors

Only after confirming the baseline should the next feature be implemented.

33. GOLDEN RULE FOR THE NEXT SESSION
The current crosshair synchronization implementation is a working baseline.

Do not change the synchronization architecture unless the next requirement specifically requires it.

The most important rule is:

SOURCE CHART
    ↓
MARKET TIME ONLY
    ↓
DESTINATION CHART
    ↓
NEAREST LOCAL CANDLE
    ↓
LOCAL CLOSE PRICE
    ↓
VALIDATE timeToCoordinate()
    ↓
SET CROSSHAIR

This design must remain intact unless there is a deliberate architectural reason to change it.

34. PROJECT ROOT TO REMEMBER
For all future local development work, the project root is:

D:\Coding\Trading-Dashboard

Main Python file:

D:\Coding\Trading-Dashboard\src\main.py

Main chart HTML:

D:\Coding\Trading-Dashboard\src\web\chart_test.html

Lightweight Charts library:

D:\Coding\Trading-Dashboard\src\web\lightweight-charts.js

Development notes:

D:\Coding\Trading-Dashboard\DEVELOPMENT_PROGRESS.md

Local Python backups:

D:\Coding\Trading-Dashboard\src\main_backup.py
D:\Coding\Trading-Dashboard\src\main_backup_20260813_071320.py

Local JavaScript/HTML backups:

D:\Coding\Trading-Dashboard\src\web\chart_test_backup.html
D:\Coding\Trading-Dashboard\src\web\chart_test_backup_20260813_071320.html

GitHub repository:

https://github.com/saishankar709-cmd/Trading-Dashboard

This document is the current development handoff/reference point for the Trading Dashboard project.
--------------------------------------------------------------------------------------------------------------------------------------------
15-Aug-2026  Requirement for popup.

# Popup Chart & Mouse Hover Synchronization

## Objective

Implement a popup-chart functionality in the Trading Dashboard that allows any chart from the main window to be opened in an independent popup window while preserving all existing chart, drawing, resizing, timeframe, and crosshair functionality.

The existing working chart architecture and current crosshair synchronization must remain stable and must not be rewritten unnecessarily.

## Functional Requirements

### 1. Open Chart in Popup

* Every chart in the main dashboard must provide an option to open that chart in a separate popup window.
* The popup must use the existing chart implementation and chart engine.
* The popup must retain the same:

  * Instrument/symbol
  * Timeframe
  * OHLC/candle data
  * Chart configuration
  * Drawing tools
  * Crosshair functionality

### 2. Popup Chart Resizing

* The popup window must be freely resizable.
* The chart must automatically resize with the popup window.
* Candles, axes, crosshair, and drawing canvas must correctly adapt to the new dimensions.
* Existing drawing resize/redraw functionality must continue to work without distortion or loss of drawings.

### 3. Popup Drawing Functionality

Every popup chart must support the same drawing functionality available in the main dashboard, including:

* Trend line
* Horizontal line
* Vertical line
* Rectangle
* Drawing movement
* Drawing resizing
* Drawing deletion

Drawings must continue to use market coordinates (`time` and `price`) rather than screen coordinates.

Changing the popup size or timeframe must not cause drawings to disappear or become permanently misaligned.

### 4. Popup Drawing Independence

Each popup must maintain its own chart/drawing state.

For the initial implementation:

```text
Main Chart
    └── Own drawings

Popup Chart
    └── Own drawings
```

Drawing changes made inside a popup must not unintentionally modify drawings on the original main-window chart.

Crosshair synchronization and drawing synchronization must remain separate concerns.

### 5. Main Window ↔ Popup Mouse Hover Synchronization

Mouse-hover crosshair synchronization must work in both directions.

Example:

```text
Main Chart
    ↓
Market Timestamp
    ↓
Popup Chart
```

and:

```text
Popup Chart
    ↓
Market Timestamp
    ↓
Main Charts
```

Only the market timestamp must be synchronized.

Each destination chart must independently locate its nearest candle and use its own local price/close value.

The existing timestamp-based synchronization architecture must be preserved.

### 6. Central Crosshair Synchronization

Introduce a central synchronization mechanism that can manage both:

* Main-window chart instances
* Popup chart instances

The synchronization manager must know:

* Which charts are currently active/visible
* Which popup windows are open
* Whether synchronization is enabled for each layout
* Whether synchronization is enabled for each popup

Closed popup windows must be removed from the synchronization registry so that no synchronization calls are sent to destroyed charts.

### 7. Layout-Level Mouse Sync Toggle

Each dashboard layout must have its own Mouse Sync ON/OFF setting.

Example:

```text
Layout 1 → ON
Layout 2 → OFF
Layout 3 → ON
Layout 4 → ON
Layout 6 → OFF
Layout 8 → ON
```

When Mouse Sync is OFF for the active layout:

* Hovering one main-window chart must not synchronize the crosshair to other charts.
* The source chart must continue to display its own crosshair normally.

Changing layouts must not unexpectedly reset the configured synchronization state.

### 8. Popup-Level Mouse Sync Toggle

Every popup window must have its own Mouse Sync ON/OFF control.

Example:

```text
Popup 1 → ON
Popup 2 → OFF
Popup 3 → ON
```

When a popup's Mouse Sync is ON:

```text
Main Chart ↔ Popup
```

crosshair synchronization is allowed.

When a popup's Mouse Sync is OFF:

```text
Popup
  ↓
Popup only
```

The popup must continue displaying its own local crosshair, but it must not send or receive synchronized crosshair updates.

### 9. Synchronization Rules

The synchronization flow must remain:

```text
Source Chart
    ↓
Market Timestamp
    ↓
Synchronization Manager
    ↓
Destination Chart
    ↓
Nearest Local Candle
    ↓
Destination's Own Price
    ↓
Crosshair
```

Price values must never be copied from the source chart to another instrument.

For example:

```text
NIFTY Chart
    ↓
Timestamp = T
    ↓
BANKNIFTY Chart
    ↓
Find nearest BANKNIFTY candle at T
    ↓
Use BANKNIFTY's own close
```

### 10. Existing Crosshair Safety

The existing protection around:

```javascript
timeToCoordinate()
```

must be preserved.

If `timeToCoordinate()` returns `null` or `undefined`, the application must not call `setCrosshairPosition()` with invalid coordinates.

The existing error-handling/safety logic that prevents:

```text
Uncaught Error: Value is null
```

must not be removed or weakened.

### 11. Existing Functionality Must Remain Unchanged

The implementation must not break any currently working functionality, including:

* Main dashboard layouts
* Chart loading
* Instrument selection
* Timeframe selection
* Candle aggregation
* Chart resizing
* Chart selection
* Crosshair synchronization
* Drawing creation
* Drawing movement
* Drawing resizing
* Drawing deletion
* Existing `ChartSlot` behavior

The popup functionality must be implemented as an extension of the current architecture rather than as a replacement for the existing chart system.

## Expected Final Behavior

The final system should support:

```text
                    TRADING DASHBOARD
                           │
              ┌────────────┴────────────┐
              │                         │
         MAIN WINDOW                POPUPS
              │                         │
       ┌──────┼──────┐            ┌────┼────┐
       │      │      │            │    │    │
     Chart  Chart  Chart        P1   P2   P3
       │      │      │            │    │    │
       └──────┼──────┘            └────┼────┘
              │                         │
              └──────────┬──────────────┘
                         │
                  CROSSHAIR SYNC
                         │
                 TIMESTAMP ONLY
```

Each layout and popup independently controls whether mouse-hover synchronization is enabled.

All charts remain fully functional independently, while synchronized charts share only the market timestamp and calculate their own local crosshair price.

## Acceptance Criteria

The requirement is considered complete when:

* Any main-window chart can be opened in a popup.
* Multiple popups can exist simultaneously.
* Popup windows can be freely resized.
* Charts automatically resize correctly inside popups.
* Existing drawing tools work inside popups.
* Drawings can be moved, resized, and deleted inside popups.
* Popup resizing does not destroy drawings.
* Main charts can synchronize their crosshair with popups.
* Popups can synchronize their crosshair with main charts.
* Synchronization works in both directions.
* Layout-level Mouse Sync can be switched ON/OFF.
* Popup-level Mouse Sync can be switched ON/OFF.
* Turning synchronization OFF leaves the local chart crosshair working.
* Different instruments use their own local candle prices.
* Closing a popup removes it safely from synchronization.
* No `Value is null` crosshair errors are introduced.
* All existing functionality continues to work exactly as before.

**Implementation principle:** preserve the current working Trading Dashboard architecture and add popup functionality and synchronization capabilities around it without destabilizing the existing chart, drawing, timeframe, and crosshair systems.


