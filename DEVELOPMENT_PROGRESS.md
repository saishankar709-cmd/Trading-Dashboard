# Trading Dashboard — Development Progress

## Project Status

The Trading Dashboard is being developed as a desktop trading-chart application using:

- Python
- PySide6
- PySide6-WebEngine
- Pandas
- OpenPyXL
- Lightweight Charts
- Excel market archive files

Primary market data source:

`D:\DataP\Files\MarketArchive_YYYY-MM-DD.xlsx`

---

# 1. Data Source & Excel Integration

## Completed

### Correct market archive identified

The initial file:

`NIFTY_2026-08-05.xlsx`

was identified as an incomplete/wrong source for the dashboard.

The correct archive is:

`MarketArchive_2026-08-05.xlsx`

Location:

`D:\DataP\Files\MarketArchive_2026-08-05.xlsx`

### Workbook sheets verified

The archive contains:

- Metadata
- Collection_Report
- Summary
- NIFTY
- NIFTY option sheets
- SENSEX
- SENSEX option sheets

The dashboard is designed to display all workbook sheets, including:

- Metadata
- Collection_Report
- Summary

exactly as available in the Excel workbook.

---

# 2. Market Data Validation

## Completed

### NIFTY

Verified structure:

- Date
- Time
- Open
- High
- Low
- Close
- Volume

NIFTY contains approximately 375 one-minute records for the trading session.

Verified:

- First candle: 09:15
- Last candle: 15:29

### Options

Option sheets contain approximately 1501 records.

Example:

`NIFTY2681124550CE`

Verified:

- First record: 09:15
- Last record: 15:30
- OHLC data
- Volume data

This confirmed that the option sheets contain usable intraday data.

---

# 3. Python Environment

## Completed

Python virtual environment is being used:

`.venv`

Installed/verified:

- pandas
- numpy
- openpyxl
- python-dateutil
- PySide6
- PySide6-WebEngine

PySide6 WebEngine was initially unavailable through the attempted package name, but the installed environment was subsequently verified successfully with:

`from PySide6.QtWebEngineWidgets import QWebEngineView`

Qt WebEngine is working.

---

# 4. Desktop Application

## Completed

A PySide6 desktop application has been established.

The application can:

- Start from `src/main.py`
- Load the chart HTML through QWebEngineView
- Display the trading chart inside the desktop application
- Communicate between Python and JavaScript

---

# 5. Lightweight Charts Integration

## Completed

Lightweight Charts is integrated through the local project file:

`src/web/lightweight-charts.js`

Important issue resolved:

`LightweightCharts is not defined`

was caused by an incorrect JavaScript library filename/reference.

The application now correctly loads:

`lightweight-charts.js`

---

# 6. Candlestick Chart

## Completed

A working candlestick chart has been implemented.

Supported:

- Open
- High
- Low
- Close
- Time
- Candlestick colors
- Chart resizing
- Time scrolling
- Zooming

---

# 7. Chart Appearance

## Completed

The chart was changed from the original black background to a clean white background.

Current appearance:

- White background
- Light horizontal grid
- Light vertical grid
- Reduced grid brightness
- Dark readable text
- Light price-scale border
- Light time-scale border

The chart is now visually closer to a professional trading interface.

---

# 8. Last Close Price Line

## Completed

The automatic last-close horizontal price line was removed.

Current configuration:

- `lastValueVisible: false`
- `priceLineVisible: false`

This applies to the candlestick series.

---

# 9. Automatic Price Scale

## Completed

Automatic price scaling was implemented.

This is important because different instruments have very different price ranges.

Examples:

- NIFTY ≈ 24,624
- SENSEX ≈ 78,581
- Options ≈ hundreds

When switching instruments, the right price scale automatically recalculates.

The selected instrument is therefore visible correctly instead of retaining the previous instrument's price range.

---

# 10. Sheet Navigation

## Completed

A left-side Sheets panel has been implemented.

It displays the workbook sheets, including:

- Metadata
- Collection_Report
- Summary
- NIFTY
- SENSEX
- CE option sheets
- PE option sheets

Selecting a sheet loads its market data where applicable.

---

# 11. Collapsible Sheets Panel

## Completed

The left Sheets panel is collapsible/expandable.

Current behavior:

- Expand
- Collapse
- Dedicated toggle button
- Chart area expands when the panel is collapsed

This has been tested and confirmed working.

---

# 12. Date/File Loading

## Completed

The application is designed around date-based market archives.

Example:

`MarketArchive_2026-08-05.xlsx`

The selected date determines the archive filename.

The application can detect when the expected archive is unavailable and report the problem instead of silently failing.

---

# 13. Timeframe System

## Completed / In Progress

The application now has a timeframe architecture based on the underlying one-minute data.

Planned/implemented timeframe buttons:

- 1m
- 3m
- 5m
- 10m
- 15m
- 30m
- 1H
- 1D

OHLC aggregation follows:

- Open = first Open
- High = maximum High
- Low = minimum Low
- Close = last Close

The aggregation is aligned with the market session rather than blindly grouping arbitrary rows.

Timeframe switching has been verified as working.

---

# 14. Initial Trend Line

## In Progress

A first Trend Line implementation was created.

Initial version successfully allowed:

- Selecting Trend Line mode
- Selecting two chart points
- Creating a trend line

However, the first implementation revealed limitations.

### Problems identified

The initial drawing implementation:

- Could not reliably select an existing line
- Could not move an existing line
- Could not resize an existing line
- Could not delete an existing line
- Had visibility problems when switching to higher timeframes

The reason is that the first version was primarily a canvas overlay rather than a complete drawing-management system.

---

# 15. Trend Line Architecture — Required Upgrade

## Next immediate work

The Trend Line system will be rebuilt as a proper Drawing Manager.

Required behavior:

### Create

- Click Trend Line
- Click first point
- Click second point
- Create line

### Select

- Click an existing line
- Show selected state/handles

### Move

- Drag the line itself
- Move the entire line

### Resize

- Drag first endpoint
- Drag second endpoint

### Delete

- Select line
- Press Delete or Backspace

### Deselect

- Click empty chart area

### Multiple drawings

Multiple Trend Lines must be supported simultaneously.

### Coordinate model

Drawings will be stored as:

`time + price`

rather than screen/pixel coordinates.

This is essential for:

- Zoom
- Scroll
- Timeframe changes
- Different chart sizes
- Pop-out charts
- Multiple layouts

---

# 16. Major Architecture Decision

## Locked In

The dashboard will not remain a single-chart application.

The architecture will be changed to use reusable independent `ChartPanel` components.

Conceptually:

Dashboard

- ChartPanel 1
- ChartPanel 2
- ChartPanel 3
- ChartPanel 4
- etc.

Each ChartPanel is a complete independent trading chart.

---

# 17. ChartPanel Requirements

Every ChartPanel must independently contain:

### Instrument

Any applicable workbook sheet.

### Timeframe

- 1m
- 3m
- 5m
- 10m
- 15m
- 30m
- 1H
- 1D

### Chart

- Candlesticks
- Automatic price scale
- Time scale
- Crosshair
- Zoom
- Scroll
- Fit content
- Light grid
- White background
- No last-close price line

### Drawings

- Trend Line
- Horizontal Line
- Vertical Line
- Rectangle

Each drawing must support appropriate:

- Create
- Select
- Move
- Resize
- Delete

---

# 18. Layout System

## Planned

A dedicated Layout Manager will be introduced.

Initial layouts:

### Single chart

`1 × 1`

### Two charts

`2 × 1`

### Four charts

`2 × 2`

### Custom layouts

User-defined panel arrangements.

---

# 19. Independent Chart State

## Required

Every chart in a layout must operate independently.

Example:

Panel 1:

`NIFTY — 5m`

Panel 2:

`NIFTY CE — 1m`

Panel 3:

`NIFTY PE — 15m`

Panel 4:

`SENSEX — 1H`

Changing Panel 2 from 1m to 5m must not affect any other panel.

Each panel independently controls:

- Instrument
- Timeframe
- Drawings
- Zoom
- Scroll
- Price scale
- Chart state

---

# 20. Custom Layout Mapping

## Planned

Users will be able to assign specific instruments/sheets to individual panels.

Example:

`My NIFTY Options Layout`

Panel 1:
- NIFTY
- 5m

Panel 2:
- NIFTY2681124550CE
- 1m

Panel 3:
- NIFTY2681124550PE
- 15m

Panel 4:
- SENSEX
- 1H

Custom layouts will eventually be saveable and reloadable.

---

# 21. Pop-Out Chart

## Planned / Architecture Locked

A selected chart inside a multi-chart layout must be able to pop out into a larger independent analysis window.

Example:

4-chart layout

→ select NIFTY CE

→ Pop Out

→ larger NIFTY CE analysis window

The pop-out must preserve the same chart state.

It must retain:

- Instrument
- Timeframe
- Drawings
- Zoom
- Scroll position
- Price scale
- Chart settings

Closing the pop-out must return the chart to the layout without losing state.

---

# 22. Maximize Chart

## Planned

In addition to Pop Out, a panel should be able to temporarily maximize inside the dashboard.

Difference:

### Maximize

Expands the selected panel inside the main dashboard.

### Pop Out

Creates a separate larger analysis window.

Both should operate on the same ChartPanel state.

---

# 23. Drawing Manager

## Planned Architecture

A reusable Drawing Manager will handle all drawing types.

Current target:

- Trend Line
- Horizontal Line
- Vertical Line
- Rectangle

The Drawing Manager must be reusable across every ChartPanel.

This prevents the drawing implementation from having to be rebuilt when multi-chart layouts are introduced.

---

# 24. Workspace Persistence

## Planned

Eventually the dashboard will save/load complete workspace state.

A saved layout will contain information such as:

- Layout arrangement
- Panel assignments
- Instrument/sheet
- Timeframe
- Drawings
- Chart state
- Zoom/visible range
- Relevant chart settings

Example:

`My Options Layout`

can later be loaded and reconstruct the complete workspace.

---

# 25. Future Development Roadmap

## Phase A — Chart Foundation

### Completed

- Excel archive loading
- Sheet discovery
- Sheet navigation
- NIFTY/SENSEX/options
- Candlestick chart
- White theme
- Light grid
- Automatic price scale
- Last-close line removal
- Collapsible sheet panel
- PySide6 desktop integration

---

## Phase B — Timeframes

### Completed / Active

- 1m
- 3m
- 5m
- 10m
- 15m
- 30m
- 1H
- 1D

---

## Phase C — Drawing Engine

### Current

- Trend Line

### Next

- Select
- Move
- Resize
- Delete
- Multiple Trend Lines
- Timeframe persistence

Then:

- Horizontal Line
- Vertical Line
- Rectangle

---

## Phase D — ChartPanel Architecture

### Next major module

Create reusable independent ChartPanel components.

Each panel gets its own:

- Instrument
- Timeframe
- Chart
- Drawings
- Chart state
- Navigation
- Settings

---

## Phase E — Layout Manager

Implement:

- Single chart
- 2-chart layout
- 4-chart layout
- Custom layouts
- Custom instrument mapping
- Independent panel controls

---

## Phase F — Maximize / Pop-Out

Implement:

- Panel maximize
- Panel pop-out
- State preservation
- Return-to-layout behavior

---

## Phase G — Workspace Persistence

Implement:

- Save layout
- Load layout
- Save drawings
- Save timeframes
- Save instrument mapping
- Save chart state

---

## Phase H — Final Trading UI

Future enhancements:

- Keyboard shortcuts
- Improved crosshair
- Better panel controls
- Tooltips
- Layout management UI
- Workspace management
- Improved option-sheet navigation
- Final visual polish

---

# Important Design Decision

The project will remain focused on:

**Price action + charting + drawings + layouts + market-data visualization.**

No technical indicators are currently planned.

The four primary drawing tools are:

1. Trend Line
2. Horizontal Line
3. Vertical Line
4. Rectangle

The architecture must support these tools independently in every chart panel and every layout.

---

# Current Development Position

## Stable

- Data loading
- Excel integration
- Sheet navigation
- Candlestick rendering
- White/light chart
- Automatic instrument price scaling
- Last-close line removal
- Collapsible Sheets panel
- Basic timeframe switching

## Active

- Robust Trend Line Drawing Manager

## Next Major Architecture

**ChartPanel + Layout Manager**

This architecture will support:

- Multiple charts
- Independent timeframes
- Independent drawings
- Custom instrument mapping
- Maximize
- Pop-out
- Workspace persistence

The multi-chart architecture should be established before implementing the remaining drawing tools so that the drawing system does not need to be rewritten later.