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
