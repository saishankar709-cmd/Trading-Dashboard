import json
import sys
from pathlib import Path

import pandas as pd

from PySide6.QtCore import QDate, QUrl, Qt, Signal
from PySide6.QtWidgets import (
    QApplication,
    QComboBox,
    QDateEdit,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QListWidget,
    QListWidgetItem,
    QMainWindow,
    QMenu,
    QMessageBox,
    QPushButton,
    QSplitter,
    QVBoxLayout,
    QWidget,
)
from PySide6.QtWebEngineWidgets import QWebEngineView

from data.excel_loader import load_sheet


# =========================================================
# CONFIGURATION
# =========================================================

DATA_FOLDER = Path(r"D:\DataP\Files")

TIMEFRAMES = [
    ("1m", 1),
    ("3m", 3),
    ("5m", 5),
    ("10m", 10),
    ("15m", 15),
    ("30m", 30),
    ("1H", 60),
    ("1D", 1440),
]


# =========================================================
# CLICKABLE / MOUSE-AWARE CHART
# =========================================================
class ClickableChartView(QWebEngineView):

    clicked = Signal()
    mouse_moved = Signal(int, int)

    def mousePressEvent(self, event):

        self.clicked.emit()

        super().mousePressEvent(event)

    def mouseMoveEvent(self, event):

        position = event.position()

        self.mouse_moved.emit(
            int(position.x()),
            int(position.y())
        )

        super().mouseMoveEvent(event)

    # -----------------------------------------------------
    # MOUSE LEAVE
    # -----------------------------------------------------

    def leaveEvent(self, event):

        self.mouse_left.emit()

        super().leaveEvent(event)


# =========================================================
# CHART SLOT
# =========================================================

class ChartSlot:

    def __init__(
        self,
        slot_id,
        parent
    ):

        self.slot_id = slot_id
        self.parent = parent

        # -------------------------------------------------
        # STATE
        # -------------------------------------------------

        self.sheet = "NIFTY"
        self.symbol = "NIFTY"

        self.timeframe = "1m"

        self.chart_ready = False

        # -------------------------------------------------
        # CONTAINER
        # -------------------------------------------------

        self.container = QWidget()

        self.container.setObjectName(
            f"chartSlot_{slot_id}"
        )

        self.container.setStyleSheet(
            """
            QWidget#chartSlot {
                border: 1px solid #d5d5d5;
                background: #ffffff;
            }
            """
        )

        self.container.setProperty(
            "active",
            False
        )

        self.layout = QVBoxLayout(
            self.container
        )

        self.layout.setContentsMargins(
            1,
            1,
            1,
            1
        )

        self.layout.setSpacing(0)

        # -------------------------------------------------
        # SLOT HEADER
        # -------------------------------------------------

        self.header = QWidget()

        self.header.setFixedHeight(
            25
        )

        self.header_layout = QHBoxLayout(
            self.header
        )

        self.header_layout.setContentsMargins(
            6,
            0,
            4,
            0
        )

        self.header_layout.setSpacing(
            5
        )

        self.title_label = QLabel(
            f"{self.slot_id + 1}. NIFTY"
        )

        self.title_label.setStyleSheet(
            """
            QLabel {
                color: #333333;
                font-size: 11px;
                font-weight: 600;
            }
            """
        )

        self.header_layout.addWidget(
            self.title_label
        )

        self.header_layout.addStretch()

        self.tf_label = QLabel(
            "1m"
        )

        self.tf_label.setStyleSheet(
            """
            QLabel {
                color: #666666;
                font-size: 10px;
            }
            """
        )

        self.header_layout.addWidget(
            self.tf_label
        )

        self.layout.addWidget(
            self.header
        )

        # -------------------------------------------------
        # CHART
        # -------------------------------------------------

        self.browser = ClickableChartView()

        self.browser.setContextMenuPolicy(
            Qt.NoContextMenu
        )

        self.browser.clicked.connect(
            self.select
        )

        self.browser.mouse_moved.connect(
            self.mouse_moved
        )

        
        html_file = (
            Path(__file__).parent
            / "web"
            / "chart_test.html"
        )

        self.browser.setUrl(
            QUrl.fromLocalFile(
                str(html_file)
            )
        )

        self.browser.loadFinished.connect(
            self.on_chart_loaded
        )

        self.layout.addWidget(
            self.browser
        )

        # -------------------------------------------------
        # INITIAL STYLE
        # -------------------------------------------------

        self.set_active(False)

    # =====================================================
    # ACTIVE STATE
    # =====================================================

    def set_active(
        self,
        active
    ):

        if active:

            self.container.setStyleSheet(
                """
                QWidget#chartSlot {
                    border: 2px solid #1976d2;
                    background: #ffffff;
                }
                """
            )

            self.title_label.setStyleSheet(
                """
                QLabel {
                    color: #1565c0;
                    font-size: 11px;
                    font-weight: 700;
                }
                """
            )

        else:

            self.container.setStyleSheet(
                """
                QWidget#chartSlot {
                    border: 1px solid #d5d5d5;
                    background: #ffffff;
                }
                """
            )

            self.title_label.setStyleSheet(
                """
                QLabel {
                    color: #333333;
                    font-size: 11px;
                    font-weight: 600;
                }
                """
            )

    # =====================================================
    # SELECT
    # =====================================================

    def select(self):

        self.parent.set_active_slot(
            self.slot_id
        )

    # =====================================================
    # MOUSE MOVED
    # =====================================================

    def mouse_moved(
        self,
        x,
        y
    ):

        if not self.chart_ready:
            return

        javascript = (
            "getCrosshairMarketPosition("
            f"{int(x)},"
            f"{int(y)}"
            ");"
        )

        self.browser.page().runJavaScript(
            javascript,
            self._crosshair_result
        )

    # =====================================================
    # CROSSHAIR RESULT
    # =====================================================

    def _crosshair_result(
        self,
        result
    ):

        if not result:
            return

        if not isinstance(
            result,
            dict
        ):
            return

        time = result.get(
            "time"
        )

        if time is None:
            return

        self.parent.sync_crosshair(
            self.slot_id,
            time
        )

    # =====================================================
    # MOUSE LEFT
    # =====================================================

    def mouse_left(self):

        self.parent.clear_synced_crosshair(
            self.slot_id
        )

    # =====================================================
    # CHART LOADED
    # =====================================================

    def on_chart_loaded(
        self,
        ok
    ):

        self.chart_ready = bool(
            ok
        )

        if not ok:
            return

        self.parent.refresh_slot(
            self.slot_id
        )

    # =====================================================
    # HEADER
    # =====================================================

    def update_header(self):

        self.title_label.setText(
            f"{self.slot_id + 1}. "
            f"{self.sheet}"
        )

        self.tf_label.setText(
            self.timeframe
        )

    def mouse_moved(
        self,
        x,
        y
    ):

        self.parent.sync_crosshair(
        self.slot_id,
        x,
        y
    )
# =========================================================
# MAIN WINDOW
# =========================================================

class TradingDashboard(
    QMainWindow
):

    def __init__(self):

        super().__init__()

        self.setWindowTitle(
            "Trading Dashboard"
        )

        self.resize(
            1400,
            900
        )

        # -------------------------------------------------
        # GLOBAL STATE
        # -------------------------------------------------

        self.current_file = None

        self.current_date = None

        self.panel_expanded = True

        self.active_slot_id = 0

        self.current_layout = 1

        self.sheet_names = []

        self.current_timeframe = "1m"

        # -------------------------------------------------
        # CHART SLOTS
        # -------------------------------------------------

        self.chart_slots = []

        for slot_id in range(8):

            self.chart_slots.append(
                ChartSlot(
                    slot_id,
                    self
                )
            )

        # =================================================
        # TOOLBAR
        # =================================================

        toolbar = QWidget()

        toolbar.setFixedHeight(
            38
        )

        toolbar_layout = QHBoxLayout(
            toolbar
        )

        toolbar_layout.setContentsMargins(
            8,
            2,
            8,
            2
        )

        toolbar_layout.setSpacing(
            4
        )

        # -------------------------------------------------
        # SYMBOL
        # -------------------------------------------------

        toolbar_layout.addWidget(
            QLabel("Symbol:")
        )

        self.symbol_combo = QComboBox()

        self.symbol_combo.addItems(
            [
                "NIFTY",
                "SENSEX",
            ]
        )

        self.symbol_combo.setFixedWidth(
            95
        )

        self.symbol_combo.setFixedHeight(
            27
        )

        toolbar_layout.addWidget(
            self.symbol_combo
        )

        # -------------------------------------------------
        # DATE
        # -------------------------------------------------

        toolbar_layout.addSpacing(
            6
        )

        toolbar_layout.addWidget(
            QLabel("Date:")
        )

        self.date_edit = QDateEdit()

        self.date_edit.setCalendarPopup(
            True
        )

        self.date_edit.setDate(
            QDate(
                2026,
                8,
                5
            )
        )

        self.date_edit.setDisplayFormat(
            "dd-MMM-yyyy"
        )

        self.date_edit.setFixedWidth(
            115
        )

        self.date_edit.setFixedHeight(
            27
        )

        toolbar_layout.addWidget(
            self.date_edit
        )

        # -------------------------------------------------
        # LOAD
        # -------------------------------------------------

        self.load_button = QPushButton(
            "Load"
        )

        self.load_button.setFixedWidth(
            60
        )

        self.load_button.setFixedHeight(
            27
        )

        toolbar_layout.addWidget(
            self.load_button
        )

        toolbar_layout.addSpacing(
            8
        )

        # -------------------------------------------------
        # TIMEFRAME
        # -------------------------------------------------

        toolbar_layout.addWidget(
            QLabel("TF:")
        )

        self.timeframe_buttons = {}

        for label, minutes in TIMEFRAMES:

            button = QPushButton(
                label
            )

            button.setCheckable(
                True
            )

            button.setFixedHeight(
                27
            )

            button.setMinimumWidth(
                38
            )

            if label == "1m":

                button.setChecked(
                    True
                )

            self.timeframe_buttons[
                label
            ] = button

            toolbar_layout.addWidget(
                button
            )

            button.clicked.connect(
                lambda checked=False,
                tf=label:
                self.change_timeframe(
                    tf
                )
            )

        toolbar_layout.addSpacing(
            8
        )

        # =================================================
        # DRAWINGS MENU
        # =================================================

        self.drawings_button = QPushButton(
            "Drawings ▾"
        )

        self.drawings_button.setFixedHeight(
            27
        )

        self.drawings_button.setMinimumWidth(
            90
        )

        self.drawings_menu = QMenu(
            self
        )

        drawing_actions = [
            (
                "↗ Trend Line",
                "trend"
            ),
            (
                "━ Horizontal Line",
                "horizontal"
            ),
            (
                "│ Vertical Line",
                "vertical"
            ),
            (
                "▭ Rectangle",
                "rectangle"
            ),
        ]

        for label, tool in drawing_actions:

            action = (
                self.drawings_menu.addAction(
                    label
                )
            )

            action.triggered.connect(
                lambda checked=False,
                tool_name=tool:
                self.activate_drawing_tool(
                    tool_name
                )
            )

        self.drawings_button.setMenu(
            self.drawings_menu
        )

        toolbar_layout.addWidget(
            self.drawings_button
        )

        # =================================================
        # LAYOUTS MENU
        # =================================================

        self.layouts_button = QPushButton(
            "Layouts ▾"
        )

        self.layouts_button.setFixedHeight(
            27
        )

        self.layouts_button.setMinimumWidth(
            90
        )

        self.layouts_menu = QMenu(
            self
        )

        layout_options = [
            (
                "▣  1 Chart",
                1
            ),
            (
                "▥  2 Charts",
                2
            ),
            (
                "▦  3 Charts",
                3
            ),
            (
                "▦  4 Charts",
                4
            ),
            (
                "▦  6 Charts",
                6
            ),
            (
                "▦  8 Charts",
                8
            ),
        ]

        for label, count in layout_options:

            action = (
                self.layouts_menu.addAction(
                    label
                )
            )

            action.triggered.connect(
                lambda checked=False,
                layout_count=count:
                self.set_layout(
                    layout_count
                )
            )

        self.layouts_button.setMenu(
            self.layouts_menu
        )

        toolbar_layout.addWidget(
            self.layouts_button
        )

        # -------------------------------------------------
        # STATUS
        # -------------------------------------------------

        toolbar_layout.addSpacing(
            8
        )

        self.status_label = QLabel(
            "Ready"
        )

        toolbar_layout.addWidget(
            self.status_label
        )

        toolbar_layout.addStretch()

        # =================================================
        # SHEETS PANEL
        # =================================================

        self.sheet_list = QListWidget()

        self.sheet_list.setMinimumWidth(
            220
        )

        sheets_title = QLabel(
            "SHEETS"
        )

        sheets_title.setFixedHeight(
            24
        )

        sheets_layout = QVBoxLayout()

        sheets_layout.setContentsMargins(
            5,
            3,
            5,
            5
        )

        sheets_layout.setSpacing(
            2
        )

        sheets_layout.addWidget(
            sheets_title
        )

        sheets_layout.addWidget(
            self.sheet_list
        )

        self.sheets_panel = QWidget()

        self.sheets_panel.setLayout(
            sheets_layout
        )

        # =================================================
        # WORKSPACE
        # =================================================

        self.workspace = QWidget()

        self.workspace_layout = QGridLayout(
            self.workspace
        )

        self.workspace_layout.setContentsMargins(
            2,
            2,
            2,
            2
        )

        self.workspace_layout.setSpacing(
            3
        )

        # =================================================
        # SHEETS + WORKSPACE SPLITTER
        # =================================================

        self.splitter = QSplitter(
            Qt.Horizontal
        )

        self.splitter.addWidget(
            self.sheets_panel
        )

        self.splitter.addWidget(
            self.workspace
        )

        self.splitter.setSizes(
            [
                280,
                1120
            ]
        )

        self.splitter.setChildrenCollapsible(
            True
        )

        # =================================================
        # COLLAPSE BUTTON
        # =================================================

        self.toggle_button = QPushButton(
            "◀"
        )

        self.toggle_button.setFixedSize(
            30,
            30
        )

        self.toggle_button.setToolTip(
            "Collapse / Expand Sheets"
        )

        # =================================================
        # CONTENT
        # =================================================

        toggle_container = QWidget()

        toggle_layout = QVBoxLayout(
            toggle_container
        )

        toggle_layout.setContentsMargins(
            2,
            2,
            2,
            0
        )

        toggle_layout.setSpacing(
            0
        )

        toggle_layout.addWidget(
            self.toggle_button
        )

        toggle_layout.addStretch()

        toggle_container.setFixedWidth(
            34
        )

        content_widget = QWidget()

        content_layout = QHBoxLayout(
            content_widget
        )

        content_layout.setContentsMargins(
            0,
            0,
            0,
            0
        )

        content_layout.setSpacing(
            0
        )

        content_layout.addWidget(
            toggle_container
        )

        content_layout.addWidget(
            self.splitter
        )

        # =================================================
        # MAIN WINDOW
        # =================================================

        central_widget = QWidget()

        main_layout = QVBoxLayout(
            central_widget
        )

        main_layout.setContentsMargins(
            0,
            0,
            0,
            0
        )

        main_layout.setSpacing(
            0
        )

        main_layout.addWidget(
            toolbar
        )

        main_layout.addWidget(
            content_widget
        )

        self.setCentralWidget(
            central_widget
        )

        # =================================================
        # SIGNALS
        # =================================================

        self.toggle_button.clicked.connect(
            self.toggle_sheets_panel
        )

        self.load_button.clicked.connect(
            self.load_selected_date
        )

        self.sheet_list.itemClicked.connect(
            self.sheet_clicked
        )

        self.symbol_combo.currentTextChanged.connect(
            self.symbol_changed
        )

        # =================================================
        # INITIAL LAYOUT
        # =================================================

        self.set_layout(
            1
        )

        # =================================================
        # INITIAL LOAD
        # =================================================

        self.load_selected_date()

    # =====================================================
    # FILE
    # =====================================================

    def get_selected_file(self):

        selected_date = (
            self.date_edit
            .date()
            .toPython()
        )

        filename = (
            f"MarketArchive_"
            f"{selected_date:%Y-%m-%d}"
            f".xlsx"
        )

        return DATA_FOLDER / filename

    # =====================================================
    # WORKBOOK
    # =====================================================

    def load_selected_date(self):

        file_path = (
            self.get_selected_file()
        )

        if not file_path.exists():

            self.current_file = None

            self.sheet_names = []

            self.sheet_list.clear()

            self.status_label.setText(
                f"File not found: "
                f"{file_path.name}"
            )

            for slot in self.chart_slots:

                slot.chart_ready = False

            return

        try:

            excel_file = pd.ExcelFile(
                file_path
            )

            self.current_file = (
                file_path
            )

            self.sheet_names = list(
                excel_file.sheet_names
            )

            self.sheet_list.clear()

            for sheet_name in (
                self.sheet_names
            ):

                self.sheet_list.addItem(
                    QListWidgetItem(
                        sheet_name
                    )
                )

            self.status_label.setText(
                f"{file_path.name} • "
                f"{len(self.sheet_names)} sheets"
            )

            # -------------------------------------------------
            # INITIAL SLOT MAPPING
            # -------------------------------------------------

            default_sheet = "NIFTY"

            if default_sheet not in (
                self.sheet_names
            ):

                if self.sheet_names:

                    default_sheet = (
                        self.sheet_names[0]
                    )

            for slot in self.chart_slots:

                if (
                    slot.sheet
                    not in self.sheet_names
                ):

                    slot.sheet = (
                        default_sheet
                    )

                    slot.symbol = (
                        default_sheet
                    )

                slot.update_header()

            # -------------------------------------------------
            # LOAD VISIBLE SLOTS
            # -------------------------------------------------

            for slot_id in (
                self.visible_slot_ids()
            ):

                self.refresh_slot(
                    slot_id
                )

            self.select_sheet_in_list(
                self.chart_slots[
                    self.active_slot_id
                ].sheet
            )

        except Exception as exc:

            QMessageBox.critical(
                self,
                "Workbook Error",
                "Unable to open workbook:\n\n"
                f"{exc}",
            )

    # =====================================================
    # SHEETS
    # =====================================================

    def sheet_clicked(
        self,
        item
    ):

        slot = self.active_slot()

        sheet_name = item.text()

        if (
            sheet_name
            not in self.sheet_names
        ):
            return

        slot.sheet = sheet_name

        slot.symbol = sheet_name

        slot.update_header()

        self.refresh_slot(
            slot.slot_id
        )

        self.status_label.setText(
            f"Chart {slot.slot_id + 1} • "
            f"{sheet_name} • "
            f"{slot.timeframe}"
        )

    # =====================================================
    # SYMBOL
    # =====================================================

    def symbol_changed(
        self,
        symbol
    ):

        if not symbol:
            return

        slot = self.active_slot()

        # -------------------------------------------------
        # Only switch automatically if the matching
        # sheet exists.
        # -------------------------------------------------

        if symbol in self.sheet_names:

            slot.symbol = symbol

            slot.sheet = symbol

            slot.update_header()

            self.select_sheet_in_list(
                symbol
            )

            self.refresh_slot(
                slot.slot_id
            )

    # =====================================================
    # ACTIVE SLOT
    # =====================================================

    def active_slot(self):

        return self.chart_slots[
            self.active_slot_id
        ]

    def set_active_slot(
        self,
        slot_id
    ):

        if slot_id < 0:
            return

        if slot_id >= len(
            self.chart_slots
        ):
            return

        self.active_slot_id = (
            slot_id
        )

        for slot in self.chart_slots:

            slot.set_active(
                slot.slot_id
                == slot_id
            )

        slot = self.active_slot()

        self.current_timeframe = (
            slot.timeframe
        )

        # -------------------------------------------------
        # TIMEFRAME BUTTONS
        # -------------------------------------------------

        for label, button in (
            self.timeframe_buttons.items()
        ):

            button.setChecked(
                label
                == slot.timeframe
            )

        # -------------------------------------------------
        # SYMBOL
        # -------------------------------------------------

        index = (
            self.symbol_combo.findText(
                slot.symbol
            )
        )

        if index >= 0:

            self.symbol_combo.blockSignals(
                True
            )

            self.symbol_combo.setCurrentIndex(
                index
            )

            self.symbol_combo.blockSignals(
                False
            )

        # -------------------------------------------------
        # SHEET
        # -------------------------------------------------

        self.select_sheet_in_list(
            slot.sheet
        )

        self.status_label.setText(
            f"Chart {slot.slot_id + 1} • "
            f"{slot.sheet} • "
            f"{slot.timeframe}"
        )

    # =====================================================
    # SELECT SHEET LIST ITEM
    # =====================================================

    def select_sheet_in_list(
        self,
        sheet_name
    ):

        if not sheet_name:
            return

        matches = (
            self.sheet_list.findItems(
                sheet_name,
                Qt.MatchExactly
            )
        )

        if not matches:
            return

        self.sheet_list.blockSignals(
            True
        )

        self.sheet_list.setCurrentItem(
            matches[0]
        )

        self.sheet_list.blockSignals(
            False
        )

    # =====================================================
    # CROSSHAIR SYNCHRONIZATION
    # =====================================================
    def sync_crosshair( self, source_slot_id, x, y):

        source_slot = self.chart_slots[
        source_slot_id
    ]

        if not source_slot.chart_ready:
            return

        javascript = (
        "syncCrosshairFromPython("
        f"{int(x)},"
        f"{int(y)}"
        ");"
    )

        for slot_id in self.visible_slot_ids():

            if slot_id == source_slot_id:
                continue

            slot = self.chart_slots[
                slot_id
            ]

            if not slot.chart_ready:
                continue

            slot.browser.page().runJavaScript(
            javascript
        )

    # =====================================================
    # CLEAR SYNCHRONIZED CROSSHAIR
    # =====================================================

    def clear_synced_crosshair(self, source_slot_id):

        for slot_id in (
            self.visible_slot_ids()
        ):

            if (
                slot_id
                == source_slot_id
            ):
                continue

            slot = self.chart_slots[
                slot_id
            ]

            if not slot.chart_ready:
                continue

            slot.browser.page().runJavaScript(
                "clearSyncedCrosshair();"
            )

    # =====================================================
    # LOAD SHEET INTO SLOT
    # =====================================================

    def refresh_slot(
        self,
        slot_id
    ):

        if self.current_file is None:
            return

        slot = self.chart_slots[
            slot_id
        ]

        if not slot.chart_ready:
            return

        try:

            chart_data = load_sheet(
                self.current_file,
                slot.sheet
            )

        except ValueError:

            self.clear_slot(
                slot_id
            )

            return

        except Exception as exc:

            self.status_label.setText(
                f"Chart {slot_id + 1} • "
                f"Error: {exc}"
            )

            self.clear_slot(
                slot_id
            )

            return

        # -------------------------------------------------
        # TIMEFRAME
        # -------------------------------------------------

        chart_data = (
            self.prepare_timeframe(
                chart_data,
                slot.timeframe
            )
        )

        candles = []

        for _, row in (
            chart_data.iterrows()
        ):

            candles.append(
                {
                    "time": int(
                        row["timestamp"]
                        .timestamp()
                    ),

                    "open": float(
                        row["Open"]
                    ),

                    "high": float(
                        row["High"]
                    ),

                    "low": float(
                        row["Low"]
                    ),

                    "close": float(
                        row["Close"]
                    ),
                }
            )

        if not candles:

            self.clear_slot(
                slot_id
            )

            return

        latest_close = (
            candles[-1]["close"]
        )

        slot.update_header()

        javascript = (
            "setChartData("
            f"{json.dumps(candles)},"
            f"{json.dumps(slot.sheet)}"
            ");"
        )

        slot.browser.page().runJavaScript(
            javascript
        )

        if slot_id == (
            self.active_slot_id
        ):

            self.status_label.setText(
                f"Chart {slot_id + 1} • "
                f"{slot.sheet} • "
                f"{slot.timeframe} • "
                f"{len(candles)} candles • "
                f"Latest: {latest_close:.2f}"
            )

    # =====================================================
    # CLEAR SLOT
    # =====================================================

    def clear_slot(
        self,
        slot_id
    ):

        slot = self.chart_slots[
            slot_id
        ]

        if not slot.chart_ready:
            return

        slot.browser.page().runJavaScript(
            "clearChartData();"
        )

    # =====================================================
    # TIMEFRAME ENGINE
    # =====================================================

    def prepare_timeframe(
        self,
        df,
        timeframe
    ):

        df = df.copy()

        if df.empty:
            return df

        df["timestamp"] = pd.to_datetime(
            df["timestamp"]
        )

        df = (
            df.sort_values(
                "timestamp"
            )
            .reset_index(
                drop=True
            )
        )

        # -------------------------------------------------
        # 1 MINUTE
        # -------------------------------------------------

        if timeframe == "1m":

            return df

        # -------------------------------------------------
        # DAILY
        # -------------------------------------------------

        if timeframe == "1D":

            result = (
                df.groupby(
                    df["timestamp"].dt.date
                )
                .agg(
                    {
                        "timestamp": "first",
                        "Open": "first",
                        "High": "max",
                        "Low": "min",
                        "Close": "last",
                    }
                )
                .reset_index(
                    drop=True
                )
            )

            return result

        # -------------------------------------------------
        # INTRADAY
        # -------------------------------------------------

        minutes = dict(
            TIMEFRAMES
        )[timeframe]

        session_start_minutes = (
            df["timestamp"].dt.hour * 60
            + df["timestamp"].dt.minute
        )

        session_start = (
            9 * 60 + 15
        )

        df["_session_offset"] = (
            session_start_minutes
            - session_start
        )

        df["_bucket"] = (
            df["_session_offset"]
            // minutes
        )

        result = (
            df.groupby(
                [
                    df["timestamp"].dt.date,
                    "_bucket",
                ],
                sort=True
            )
            .agg(
                timestamp=(
                    "timestamp",
                    "first"
                ),

                Open=(
                    "Open",
                    "first"
                ),

                High=(
                    "High",
                    "max"
                ),

                Low=(
                    "Low",
                    "min"
                ),

                Close=(
                    "Close",
                    "last"
                ),
            )
            .reset_index(
                drop=True
            )
        )

        return result

    # =====================================================
    # TIMEFRAME SELECTION
    # =====================================================

    def change_timeframe(
        self,
        timeframe
    ):

        slot = self.active_slot()

        slot.timeframe = (
            timeframe
        )

        for label, button in (
            self.timeframe_buttons.items()
        ):

            button.setChecked(
                label == timeframe
            )

        slot.update_header()

        self.refresh_slot(
            slot.slot_id
        )

        self.status_label.setText(
            f"Chart {slot.slot_id + 1} • "
            f"{slot.sheet} • "
            f"{timeframe}"
        )

    # =====================================================
    # DRAWINGS
    # =====================================================

    def activate_drawing_tool(
        self,
        tool
    ):

        slot = self.active_slot()

        if not slot.chart_ready:
            return

        labels = {
            "trend": "Trend Line",
            "horizontal": "Horizontal Line",
            "vertical": "Vertical Line",
            "rectangle": "Rectangle",
        }

        label = labels.get(
            tool,
            "Drawing"
        )

        self.status_label.setText(
            f"Chart {slot.slot_id + 1} • "
            f"{label}: click on chart"
        )

        javascript = (
            "setDrawingModeFromPython("
            f"{json.dumps(tool)}"
            ");"
        )

        slot.browser.page().runJavaScript(
            javascript
        )

    # =====================================================
    # VISIBLE SLOTS
    # =====================================================

    def visible_slot_ids(self):

        count = (
            self.current_layout
        )

        return list(
            range(count)
        )

    # =====================================================
    # LAYOUT ENGINE
    # =====================================================

    def set_layout(
        self,
        layout_count
    ):

        if layout_count not in [
            1,
            2,
            3,
            4,
            6,
            8
        ]:

            return

        self.current_layout = (
            layout_count
        )

        # -------------------------------------------------
        # REMOVE EXISTING WIDGETS
        # -------------------------------------------------

        while (
            self.workspace_layout.count()
            > 0
        ):

            item = (
                self.workspace_layout.takeAt(
                    0
                )
            )

            widget = item.widget()

            if widget:

                widget.hide()

        # -------------------------------------------------
        # LAYOUT GEOMETRY
        # -------------------------------------------------

        if layout_count == 1:

            rows = 1
            cols = 1

            positions = [
                (0, 0, 1, 1)
            ]

        elif layout_count == 2:

            rows = 1
            cols = 2

            positions = [
                (0, 0, 1, 1),
                (0, 1, 1, 1),
            ]

        elif layout_count == 3:

            rows = 2
            cols = 2

            positions = [
                (0, 0, 1, 2),
                (1, 0, 1, 1),
                (1, 1, 1, 1),
            ]

        elif layout_count == 4:

            rows = 2
            cols = 2

            positions = [
                (0, 0, 1, 1),
                (0, 1, 1, 1),
                (1, 0, 1, 1),
                (1, 1, 1, 1),
            ]

        elif layout_count == 6:

            rows = 2
            cols = 3

            positions = [
                (0, 0, 1, 1),
                (0, 1, 1, 1),
                (0, 2, 1, 1),
                (1, 0, 1, 1),
                (1, 1, 1, 1),
                (1, 2, 1, 1),
            ]

        else:

            rows = 2
            cols = 4

            positions = [
                (0, 0, 1, 1),
                (0, 1, 1, 1),
                (0, 2, 1, 1),
                (0, 3, 1, 1),
                (1, 0, 1, 1),
                (1, 1, 1, 1),
                (1, 2, 1, 1),
                (1, 3, 1, 1),
            ]

        # -------------------------------------------------
        # CLEAR STRETCH
        # -------------------------------------------------

        for row in range(8):

            self.workspace_layout.setRowStretch(
                row,
                0
            )

        for col in range(8):

            self.workspace_layout.setColumnStretch(
                col,
                0
            )

        # -------------------------------------------------
        # ADD SLOTS
        # -------------------------------------------------

        for index, position in enumerate(
            positions
        ):

            (
                row,
                col,
                row_span,
                col_span
            ) = position

            slot = self.chart_slots[
                index
            ]

            self.workspace_layout.addWidget(
                slot.container,
                row,
                col,
                row_span,
                col_span
            )

            slot.container.show()

        # -------------------------------------------------
        # STRETCH
        # -------------------------------------------------

        for row in range(rows):

            self.workspace_layout.setRowStretch(
                row,
                1
            )

        for col in range(cols):

            self.workspace_layout.setColumnStretch(
                col,
                1
            )

        # -------------------------------------------------
        # ACTIVE SLOT
        # -------------------------------------------------

        if (
            self.active_slot_id
            >= layout_count
        ):

            self.active_slot_id = 0

        self.set_active_slot(
            self.active_slot_id
        )

        # -------------------------------------------------
        # LOAD VISIBLE CHARTS
        # -------------------------------------------------

        for slot_id in (
            self.visible_slot_ids()
        ):

            self.refresh_slot(
                slot_id
            )

        self.status_label.setText(
            f"Layout: "
            f"{layout_count} chart"
            f"{'s' if layout_count != 1 else ''}"
            f" • Active: "
            f"Chart {self.active_slot_id + 1}"
        )

    # =====================================================
    # SHEETS PANEL
    # =====================================================

    def toggle_sheets_panel(
        self
    ):

        if self.panel_expanded:

            self.splitter.setSizes(
                [
                    0,
                    self.splitter.width()
                ]
            )

            self.toggle_button.setText(
                "▶"
            )

            self.panel_expanded = False

        else:

            self.splitter.setSizes(
                [
                    280,
                    max(
                        300,
                        self.splitter.width()
                        - 280
                    )
                ]
            )

            self.toggle_button.setText(
                "◀"
            )

            self.panel_expanded = True


# =========================================================
# APPLICATION ENTRY
# =========================================================

def main():

    app = QApplication(
        sys.argv
    )

    window = TradingDashboard()

    window.show()

    sys.exit(
        app.exec()
    )


if __name__ == "__main__":

    main()
