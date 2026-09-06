# =========================================================
# CHART LAYOUT DEFINITIONS
# =========================================================
#
# position = (row, column, row_span, column_span)
#
# The layout IDs are deliberately unique. The number of
# charts is stored separately as "count".
# =========================================================

LAYOUTS = {

    # -----------------------------------------------------
    # 1 CHART
    # -----------------------------------------------------

    "1_full": {
        "count": 1,
        "rows": 1,
        "cols": 1,
        "positions": [
            (0, 0, 1, 1),
        ],
    },

    # -----------------------------------------------------
    # 2 CHARTS
    # -----------------------------------------------------

    "2_horizontal": {
        "count": 2,
        "rows": 1,
        "cols": 2,
        "positions": [
            (0, 0, 1, 1),
            (0, 1, 1, 1),
        ],
    },

    "2_vertical": {
        "count": 2,
        "rows": 2,
        "cols": 1,
        "positions": [
            (0, 0, 1, 1),
            (1, 0, 1, 1),
        ],
    },

    # -----------------------------------------------------
    # 3 CHARTS
    # -----------------------------------------------------

    "3_horizontal": {
        "count": 3,
        "rows": 1,
        "cols": 3,
        "positions": [
            (0, 0, 1, 1),
            (0, 1, 1, 1),
            (0, 2, 1, 1),
        ],
    },

    "3_vertical": {
        "count": 3,
        "rows": 3,
        "cols": 1,
        "positions": [
            (0, 0, 1, 1),
            (1, 0, 1, 1),
            (2, 0, 1, 1),
        ],
    },

    "3_large_left": {
        "count": 3,
        "rows": 2,
        "cols": 2,
        "positions": [
            (0, 0, 2, 1),
            (0, 1, 1, 1),
            (1, 1, 1, 1),
        ],
    },

    "3_large_right": {
        "count": 3,
        "rows": 2,
        "cols": 2,
        "positions": [
            (0, 0, 1, 1),
            (1, 0, 1, 1),
            (0, 1, 2, 1),
        ],
    },

    "3_large_bottom": {
        "count": 3,
        "rows": 2,
        "cols": 2,
        "positions": [
            (0, 0, 1, 1),
            (0, 1, 1, 1),
            (1, 0, 1, 2),
        ],
    },

    "3_large_top": {
        "count": 3,
        "rows": 2,
        "cols": 2,
        "positions": [
            (0, 0, 1, 2),
            (1, 0, 1, 1),
            (1, 1, 1, 1),
        ],
    },

    # -----------------------------------------------------
    # 4 CHARTS
    # -----------------------------------------------------

    "4_grid": {
        "count": 4,
        "rows": 2,
        "cols": 2,
        "positions": [
            (0, 0, 1, 1),
            (0, 1, 1, 1),
            (1, 0, 1, 1),
            (1, 1, 1, 1),
        ],
    },

    "4_horizontal": {
        "count": 4,
        "rows": 1,
        "cols": 4,
        "positions": [
            (0, 0, 1, 1),
            (0, 1, 1, 1),
            (0, 2, 1, 1),
            (0, 3, 1, 1),
        ],
    },

    "4_vertical": {
        "count": 4,
        "rows": 4,
        "cols": 1,
        "positions": [
            (0, 0, 1, 1),
            (1, 0, 1, 1),
            (2, 0, 1, 1),
            (3, 0, 1, 1),
        ],
    },

    "4_large_left": {
        "count": 4,
        "rows": 3,
        "cols": 2,
        "positions": [
            (0, 0, 3, 1),
            (0, 1, 1, 1),
            (1, 1, 1, 1),
            (2, 1, 1, 1),
        ],
    },

    "4_large_right": {
        "count": 4,
        "rows": 3,
        "cols": 2,
        "positions": [
            (0, 0, 1, 1),
            (1, 0, 1, 1),
            (2, 0, 1, 1),
            (0, 1, 3, 1),
        ],
    },

    "4_large_top": {
        "count": 4,
        "rows": 2,
        "cols": 3,
        "positions": [
            (0, 0, 1, 3),
            (1, 0, 1, 1),
            (1, 1, 1, 1),
            (1, 2, 1, 1),
        ],
    },

    "4_large_bottom": {
        "count": 4,
        "rows": 2,
        "cols": 3,
        "positions": [
            (0, 0, 1, 1),
            (0, 1, 1, 1),
            (0, 2, 1, 1),
            (1, 0, 1, 3),
        ],
    },

    # -----------------------------------------------------
    # 5 CHARTS
    # -----------------------------------------------------

    "5_horizontal": {
        "count": 5,
        "rows": 1,
        "cols": 5,
        "positions": [
            (0, 0, 1, 1),
            (0, 1, 1, 1),
            (0, 2, 1, 1),
            (0, 3, 1, 1),
            (0, 4, 1, 1),
        ],
    },

    "5_two_three": {
        "count": 5,
        "rows": 2,
        "cols": 6,
        "positions": [
            (0, 0, 1, 3),
            (0, 3, 1, 3),
            (1, 0, 1, 2),
            (1, 2, 1, 2),
            (1, 4, 1, 2),
        ],
    },

    # -----------------------------------------------------
    # 6 CHARTS
    # -----------------------------------------------------

    "6_grid": {
        "count": 6,
        "rows": 2,
        "cols": 3,
        "positions": [
            (0, 0, 1, 1),
            (0, 1, 1, 1),
            (0, 2, 1, 1),
            (1, 0, 1, 1),
            (1, 1, 1, 1),
            (1, 2, 1, 1),
        ],
    },

    "6_horizontal": {
        "count": 6,
        "rows": 1,
        "cols": 6,
        "positions": [
            (0, 0, 1, 1),
            (0, 1, 1, 1),
            (0, 2, 1, 1),
            (0, 3, 1, 1),
            (0, 4, 1, 1),
            (0, 5, 1, 1),
        ],
    },

    # -----------------------------------------------------
    # 8 CHARTS
    # -----------------------------------------------------

    "8_grid": {
        "count": 8,
        "rows": 2,
        "cols": 4,
        "positions": [
            (0, 0, 1, 1),
            (0, 1, 1, 1),
            (0, 2, 1, 1),
            (0, 3, 1, 1),
            (1, 0, 1, 1),
            (1, 1, 1, 1),
            (1, 2, 1, 1),
            (1, 3, 1, 1),
        ],
    },

    "8_horizontal": {
        "count": 8,
        "rows": 1,
        "cols": 8,
        "positions": [
            (0, 0, 1, 1),
            (0, 1, 1, 1),
            (0, 2, 1, 1),
            (0, 3, 1, 1),
            (0, 4, 1, 1),
            (0, 5, 1, 1),
            (0, 6, 1, 1),
            (0, 7, 1, 1),
        ],
    },
}

import math
import json
import sys
from pathlib import Path

import time as time_module

import pandas as pd

from PySide6.QtWebChannel import QWebChannel

from PySide6.QtCore import (
    QDate,
    QUrl,
    Qt,
    Signal,
    QObject,
    Slot,
    QSize,
)

from PySide6.QtGui import (
    QPainter,
    QPen,
    QColor,
)

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
    QToolButton,
    QWidgetAction,
    QFrame,
    QFileDialog,
)
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWebEngineCore import QWebEnginePage
from data.excel_loader import load_sheet
from data.data_repository import DataRepository
from performance_monitor import perf

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

class ChartBridge(QObject):

    clicked = Signal()
    mouse_moved = Signal(float, float)

    @Slot()
    def chart_clicked(self):
        self.clicked.emit()

    @Slot(float, float)
    def chart_mouse_moved(self, time, price):
        self.mouse_moved.emit(
            time,
            price
        )

# =========================================================
# CLICKABLE / MOUSE-AWARE CHART
# =========================================================
class DebugWebEnginePage(QWebEnginePage):

    def javaScriptConsoleMessage(
        self,
        level,
        message,
        lineNumber,
        sourceID
    ):
        print(
            f"[JS] {message} "
            f"(line {lineNumber}, source={sourceID})"
        )

class ClickableChartView(QWebEngineView):

    print("[TEST] ClickableChartView class loaded")
    clicked = Signal()
    mouse_moved = Signal(int, int)
    mouse_left = Signal()

    def javaScriptConsoleMessage(
        self,
        level,
        message,
        lineNumber,
        sourceID
    ):
        print("[TEST] javaScriptConsoleMessage CALLED")
        print(
            f"[JS] {message} "
            f"(line {lineNumber}, source={sourceID})"
        )
    
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setMouseTracking(True)

    def mousePressEvent(self, event):
        self.clicked.emit()
        super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        pos = event.position()

        self.mouse_moved.emit(
            int(pos.x()),
            int(pos.y())
        )

        super().mouseMoveEvent(event)

    def leaveEvent(self, event):
        self.mouse_left.emit()
        super().leaveEvent(event)

# =========================================================
# LAYOUT ICON
# =========================================================

class LayoutIconButton(QPushButton):

    clicked_layout = Signal(str)

    def __init__(
        self,
        layout_id,
        selected=False,
        parent=None
    ):

        super().__init__(parent)

        self.layout_id = layout_id
        self.selected = selected

        self.setFixedSize(
            34,
            28
        )

        self.setCursor(
            Qt.PointingHandCursor
        )

        self.setStyleSheet(
            """
            QPushButton {
                border: none;
                background: transparent;
                padding: 0px;
            }

            QPushButton:hover {
                background: #e8f5e9;
            }
            """
        )

        self.clicked.connect(
            lambda:
            self.clicked_layout.emit(
                self.layout_id
            )
        )

    def set_selected(
        self,
        selected
    ):

        self.selected = selected
        self.update()

    def paintEvent(
        self,
        event
    ):

        painter = QPainter(
            self
        )

        painter.setRenderHint(
            QPainter.Antialiasing
        )

        if self.selected:

            painter.setPen(
                Qt.NoPen
            )

            painter.setBrush(
                QColor(
                    "#b7f7d0"
                )
            )

            painter.drawRoundedRect(
                1,
                1,
                self.width() - 2,
                self.height() - 2,
                3,
                3
            )

        layout = LAYOUTS[
            self.layout_id
        ]

        rows = layout["rows"]
        cols = layout["cols"]

        positions = layout[
            "positions"
        ]

        pen = QPen(
            QColor(
                "#30343b"
            )
        )

        pen.setWidth(
            1
        )

        painter.setPen(
            pen
        )

        painter.setBrush(
            QColor(
                "#ffffff"
            )
        )

        margin = 6

        width = (
            self.width()
            - margin * 2
        )

        height = (
            self.height()
            - margin * 2
        )

        for (
            row,
            col,
            row_span,
            col_span
        ) in positions:

            x = (
                margin
                +
                width
                * col
                / cols
            )

            y = (
                margin
                +
                height
                * row
                / rows
            )

            w = (
                width
                * col_span
                / cols
            )

            h = (
                height
                * row_span
                / rows
            )

            painter.drawRect(
                int(x),
                int(y),
                max(
                    1,
                    int(w)
                ),
                max(
                    1,
                    int(h)
                )
            )

# =========================================================
# LAYOUT MENU ROW
# =========================================================

class LayoutMenuRow(QWidget):

    def __init__(
        self,
        dashboard,
        count,
        layout_ids,
        parent=None
    ):

        super().__init__(
            parent
        )

        self.dashboard = dashboard
        self.count = count
        self.buttons = {}

        layout = QHBoxLayout(
            self
        )

        layout.setContentsMargins(
            4,
            2,
            8,
            2
        )

        layout.setSpacing(
            2
        )

        label = QLabel(
            str(count)
        )

        label.setFixedWidth(
            16
        )

        label.setAlignment(
            Qt.AlignCenter
        )

        label.setStyleSheet(
            """
            QLabel {
                color: #7a7f87;
                font-size: 11px;
                background: transparent;
            }
            """
        )

        layout.addWidget(
            label
        )

        for layout_id in layout_ids:

            button = LayoutIconButton(
                layout_id,
                selected=(
                    layout_id
                    ==
                    dashboard.current_layout
                )
            )

            button.clicked_layout.connect(
                self.layout_selected
            )

            self.buttons[
                layout_id
            ] = button

            layout.addWidget(
                button
            )

        layout.addStretch()

    def layout_selected(
        self,
        layout_id
    ):

        self.dashboard.set_layout(
            layout_id
        )

        self.dashboard.layouts_menu.close()

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

        self.popup_button = QPushButton(
            "↗"
        )

        self.popup_button.setFixedSize(
            24,
            20
        )

        self.popup_button.setToolTip(
            "Open chart in popup"
        )

        self.popup_button.setStyleSheet(
            """
            QPushButton {
                border: none;
                color: #555555;
                background: transparent;
                font-size: 12px;
                font-weight: 600;
            }

            QPushButton:hover {
                color: #1565c0;
                background: #eeeeee;
            }
            """
        )

        self.popup_button.clicked.connect(
            self.open_popup
        )

        self.header_layout.addWidget(
            self.popup_button
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
                     
        self.bridge = ChartBridge()

        self.bridge.mouse_moved.connect(
            self.chart_crosshair_moved
        )

        self.channel = QWebChannel(
            self.browser.page()
        )

        self.channel.registerObject(
            "chartBridge",
            self.bridge
        )

        self.browser.page().setWebChannel(
            self.channel
        )

        self.bridge.clicked.connect(
            self.select
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
        """
        Crosshair movement is handled by the
        Lightweight Charts crosshairMove event.

        Do not call JavaScript from the Qt mouseMoveEvent.

        The previous implementation performed:

            Qt mouseMove
                ↓
            Python
                ↓
            JavaScript
                ↓
            Python callback

        on every mouse movement.

        That creates an unnecessary high-frequency
        Python <-> JavaScript round trip.

        The Lightweight Charts JavaScript event already
        provides the logical candle time, so this Qt
        mouse handler no longer needs to do anything.
        """

        return
    # =====================================================
    # JAVASCRIPT CROSSHAIR MOVED
    # =====================================================

    def chart_crosshair_moved(
        self,
        time,
        price
    ):        
        if not self.chart_ready:
            return

        if time is None:
            return

        # -------------------------------------------------
        # SOURCE WINDOW MOUSE SYNC MASTER SWITCH
        # -------------------------------------------------

        if not self.parent.sync_enabled:
            return

        if isinstance(
            self.parent,
            PopupChartWindow
        ):
            self.parent.sync_crosshair(
                self.slot_id,
                float(time)
            )
        else:
            self.parent.sync_crosshair(
                self,
                float(time)
            )

    # =====================================================
    # CROSSHAIR RESULT
    # =====================================================

    def _crosshair_result(
        self,
        result
    ):

        print(
            f"[CROSSHAIR RESULT] "
            f"slot={self.slot_id + 1} "
            f"result={result}"
        )

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

        print(
            f"[CROSSHAIR TIME] "
            f"slot={self.slot_id + 1} "
            f"time={time}"
        )

        if time is None:
            return

        # -------------------------------------------------
        # SOURCE WINDOW MOUSE SYNC MASTER SWITCH
        # -------------------------------------------------

        if not self.parent.sync_enabled:
            return

        if isinstance(
            self.parent,
            PopupChartWindow
        ):
            self.parent.sync_crosshair(
                self.slot_id,
                time
            )
        else:
            self.parent.sync_crosshair(
                self,
                time
            )

    # =====================================================
    # MOUSE LEFT
    # =====================================================

    def mouse_left(self):

        if isinstance(
            self.parent,
            PopupChartWindow
        ):
            self.parent.clear_synced_crosshair(
                self.slot_id
            )
        else:
            self.parent.clear_synced_crosshair(
                self
            )

    # =====================================================
    # CHART LOADED
    # =====================================================

    def on_chart_loaded(
        self,
        ok
    ):
        self.chart_ready = bool(ok)

        print(
            f"[CHART LOAD] slot={self.slot_id + 1} ok={ok}"
        )

        if not ok:
            return

        def js_ready(result):
            print(
                f"[CHART JS READY] "
                f"slot={self.slot_id + 1} "
                f"setChartData={result}"
            )

            if result != "function":
                print(
                    f"[CHART ERROR] "
                    f"slot={self.slot_id + 1} "
                    f"setChartData is not available"
                )
                return

            self.parent.refresh_slot(
                self.slot_id
            )

        self.browser.page().runJavaScript(
            "typeof setChartData",
            js_ready
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
     
    def activate(self):
        self.parent.set_active_slot(self.slot_id)

    # =====================================================
    # OPEN POPUP
    # =====================================================

    def open_popup(self):
        self.parent.open_popup(
        self
        )

# =========================================================
# POPUP CHART WINDOW
# =========================================================

# =========================================================
# POPUP CHART WINDOW
# =========================================================

class PopupChartWindow(QMainWindow):

    def __init__(
        self,
        parent_dashboard,
        source_slot
    ):

        super().__init__()

        self.dashboard = parent_dashboard
        self.source_slot = source_slot

        # -------------------------------------------------
        # POPUP STATE
        # -------------------------------------------------

        self.current_layout = "1_full"

        self.active_slot_id = 0

        self.layout_sync_enabled = {
            layout_id: True
            for layout_id in LAYOUTS
        }

        self.sync_enabled = True
        
        self.closing = False

        # -------------------------------------------------
        # CHART SLOTS
        # -------------------------------------------------

        self.chart_slots = []

        for slot_id in range(8):

            slot = ChartSlot(
                slot_id,
                self
            )

            self.chart_slots.append(
                slot
            )

        # -------------------------------------------------
        # INITIAL SLOT STATE
        # -------------------------------------------------

        for slot in self.chart_slots:

            slot.sheet = (
                source_slot.sheet
            )

            slot.symbol = (
                source_slot.symbol
            )

            slot.timeframe = (
                source_slot.timeframe
            )

            slot.update_header()

        # -------------------------------------------------
        # INITIAL WINDOW
        # -------------------------------------------------

        self.setWindowTitle(
            f"Trading Dashboard Popup • "
            f"{source_slot.symbol} • "
            f"{source_slot.timeframe}"
        )

        self.resize(
            1100,
            700
        )

        # =================================================
        # CENTRAL WIDGET
        # =================================================

        central = QWidget()

        main_layout = QVBoxLayout(
            central
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
            3,
            8,
            3
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

        self.symbol_combo.setFixedWidth(
            130
        )

        self.symbol_combo.setFixedHeight(
            27
        )

        self.symbol_combo.addItems(
            self.dashboard.sheet_names
        )

        current_symbol = (
            source_slot.symbol
        )

        if current_symbol in (
            self.dashboard.sheet_names
        ):

            self.symbol_combo.setCurrentText(
                current_symbol
            )

        self.symbol_combo.currentTextChanged.connect(
            self.symbol_changed
        )

        toolbar_layout.addWidget(
            self.symbol_combo
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

            button.setChecked(
                label
                ==
                source_slot.timeframe
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
            6
        )

        # -------------------------------------------------
        # DRAWINGS
        # -------------------------------------------------

        self.drawings_button = QPushButton(
            "Drawings ▾"
        )

        self.drawings_button.setFixedHeight(
            27
        )

        self.drawings_button.setMinimumWidth(
            90
        )

        drawings_menu = QMenu(
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
                drawings_menu.addAction(
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
            drawings_menu
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

        self.layouts_menu.setStyleSheet(
            """
            QMenu {
                background: #ffffff;
                border: 1px solid #d5d8dc;
                padding: 4px;
            }

            QMenu::separator {
                height: 1px;
                background: #e5e7eb;
                margin: 2px 4px;
            }
            """
        )

        layout_groups = {

            1: [
                "1_full",
            ],

            2: [
                "2_horizontal",
                "2_vertical",
            ],

            3: [
                "3_horizontal",
                "3_vertical",
                "3_large_left",
                "3_large_right",
                "3_large_top",
                "3_large_bottom",
            ],

            4: [
                "4_grid",
                "4_horizontal",
                "4_vertical",
                "4_large_left",
                "4_large_right",
                "4_large_top",
                "4_large_bottom",
            ],

            5: [
                "5_horizontal",
                "5_two_three",
            ],

            6: [
                "6_grid",
                "6_horizontal",
            ],

            8: [
                "8_grid",
                "8_horizontal",
            ],
        }

        for index, (
            count,
            layout_ids
        ) in enumerate(
            layout_groups.items()
        ):

            row_widget = LayoutMenuRow(
                self,
                count,
                layout_ids
            )

            action = QWidgetAction(
                self.layouts_menu
            )

            action.setDefaultWidget(
                row_widget
            )

            self.layouts_menu.addAction(
                action
            )

            if index < (
                len(layout_groups) - 1
            ):

                self.layouts_menu.addSeparator()

        self.layouts_button.setMenu(
            self.layouts_menu
        )

        toolbar_layout.addWidget(
            self.layouts_button
        )

        # =================================================
        # MOUSE SYNC
        # =================================================

        self.sync_button = QPushButton(
            "Mouse Sync: ON"
        )

        self.sync_button.setCheckable(
            True
        )

        self.sync_button.setChecked(
            True
        )

        self.sync_button.setFixedHeight(
            27
        )

        self.sync_button.clicked.connect(
            self.toggle_layout_sync
        )

        toolbar_layout.addWidget(
            self.sync_button
        )

        # -------------------------------------------------
        # CLOSE
        # -------------------------------------------------

        self.close_button = QPushButton(
            "Close"
        )

        self.close_button.setFixedHeight(
            27
        )

        self.close_button.clicked.connect(
            self.close
        )

        toolbar_layout.addWidget(
            self.close_button
        )

        main_layout.addWidget(
            toolbar
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

        main_layout.addWidget(
            self.workspace
        )

        self.setCentralWidget(
            central
        )

        # =================================================
        # INITIAL LAYOUT
        # =================================================

        self.set_layout(
            "1_full"
        )

    # =====================================================
    # ACTIVE SLOT
    # =====================================================

    @property
    def chart_ready(self):
        return any(
            getattr(slot, "chart_ready", False)
            for slot in self.chart_slots
        )

    def active_slot(
        self
    ):

        return self.chart_slots[
            self.active_slot_id
        ]

    # =====================================================
    # SET ACTIVE SLOT
    # =====================================================

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

        visible = (
            self.visible_slot_ids()
        )

        for slot in self.chart_slots:

            slot.set_active(
                slot.slot_id
                ==
                self.active_slot_id
                and
                slot.slot_id in visible
            )

    # =====================================================
    # VISIBLE SLOTS
    # =====================================================

    def visible_slot_ids(
        self
    ):

        layout = LAYOUTS.get(
            self.current_layout
        )

        if not layout:
            return []

        return list(
            range(
                layout["count"]
            )
        )

    # =====================================================
    # LAYOUT ENGINE
    # =====================================================

    def set_layout(
        self,
        layout_id
    ):

        if layout_id not in LAYOUTS:
            return

        self.current_layout = (
            layout_id
        )

        config = LAYOUTS[
            layout_id
        ]

        rows = config[
            "rows"
        ]

        cols = config[
            "cols"
        ]

        positions = config[
            "positions"
        ]

        chart_count = config[
            "count"
        ]

        # -------------------------------------------------
        # REMOVE CURRENT WIDGETS
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
        # ADD CHARTS
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
            >= chart_count
        ):

            self.active_slot_id = 0

        self.set_active_slot(
            self.active_slot_id
        )

        # -------------------------------------------------
        # REFRESH VISIBLE CHARTS
        # -------------------------------------------------

        for slot_id in (
            self.visible_slot_ids()
        ):

            self.refresh_slot(
                slot_id
            )

        # -------------------------------------------------
        # STATUS
        # -------------------------------------------------

        self.setWindowTitle(
            f"Trading Dashboard Popup • "
            f"Layout {layout_id} • "
            f"Chart "
            f"{self.active_slot_id + 1}"
        )

    # =====================================================
    # SYMBOL CHANGE
    # =====================================================

    def symbol_changed(
        self,
        symbol
    ):

        if not symbol:
            return

        if symbol not in (
            self.dashboard.sheet_names
        ):
            return

        slot = self.active_slot()

        slot.symbol = symbol
        slot.sheet = symbol

        slot.update_header()

        self.refresh_slot(
            slot.slot_id
        )

        self.update_header()

    # =====================================================
    # TIMEFRAME CHANGE
    # =====================================================

    def change_timeframe(
        self,
        timeframe
    ):

        if timeframe not in dict(
            TIMEFRAMES
        ):
            return

        slot = self.active_slot()

        slot.timeframe = (
            timeframe
        )

        for label, button in (
            self.timeframe_buttons.items()
        ):

            button.blockSignals(
                True
            )

            button.setChecked(
                label == timeframe
            )

            button.blockSignals(
                False
            )

        slot.update_header()

        self.refresh_slot(
            slot.slot_id
        )

        self.update_header()

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

        javascript = (
            "setDrawingModeFromPython("
            f"{json.dumps(tool)}"
            ");"
        )

        slot.browser.page().runJavaScript(
            javascript
        )

    # =====================================================
    # MOUSE SYNC
    # =====================================================

    def toggle_layout_sync(
        self,
        checked
    ):
        checked = bool(checked)

        # -------------------------------------------------
        # POPUP MOUSE SYNC STATE
        # -------------------------------------------------
        #
        # This controls whether the popup participates
        # in mouse/crosshair synchronization with the
        # main dashboard.
        #
        self.sync_enabled = checked

        # -------------------------------------------------
        # POPUP INTERNAL LAYOUT SYNC STATE
        # -------------------------------------------------
        #
        # Keep the existing layout-specific behavior.
        #
        self.layout_sync_enabled[
            self.current_layout
        ] = checked

        self.update_mouse_sync_button()

        # -------------------------------------------------
        # CLEAR EXISTING SYNCED CROSSHAIRS WHEN OFF
        # -------------------------------------------------
        if not checked:

            for slot_id in (
                self.visible_slot_ids()
            ):

                slot = self.chart_slots[
                    slot_id
                ]

                if not slot.chart_ready:
                    continue

                slot.browser.page().runJavaScript(
                    "clearSyncedCrosshair();"
                )

    # =====================================================
    # UPDATE MOUSE SYNC BUTTON
    # =====================================================

    def update_mouse_sync_button(
        self
    ):

        enabled = (
            self.layout_sync_enabled.get(
                self.current_layout,
                True
            )
        )

        self.sync_button.blockSignals(
            True
        )

        self.sync_button.setChecked(
            enabled
        )

        self.sync_button.setText(
            "Mouse Sync: ON"
            if enabled
            else
            "Mouse Sync: OFF"
        )

        self.sync_button.blockSignals(
            False
        )

    # =====================================================
    # CROSSHAIR
    # =====================================================

    def sync_crosshair(
        self,
        slot_id,
        time
    ):
        """
        Synchronize a crosshair originating from one chart
        inside a popup.

        There are TWO synchronization levels:

        1. Charts inside this popup.
        2. Main dashboard + other popup windows.

        The source popup's own settings control whether
        synchronization is allowed.
        """

        # =====================================================
        # VALIDATE POPUP MASTER SYNC
        # =====================================================

        if not self.sync_enabled:
            return

        # =====================================================
        # VALIDATE TIME
        # =====================================================

        try:
            time = float(time)
        except (
            TypeError,
            ValueError
        ):
            return

        if not math.isfinite(time):
            return

        # =====================================================
        # INTERNAL POPUP SYNCHRONIZATION
        # =====================================================

        #
        # IMPORTANT:
        #
        # A popup layout is a group of charts.
        #
        # We synchronize the source chart with every OTHER
        # visible chart in the current popup layout.
        #

        layout_sync = self.layout_sync_enabled.get(
            self.current_layout,
            True
        )

        if layout_sync:

            visible_ids = (
                self.visible_slot_ids()
            )

            if slot_id in visible_ids:

                javascript = (
                    "syncCrosshairFromPython("
                    f"{time}"
                    ");"
                )

                for target_id in visible_ids:

                    if target_id == slot_id:
                        continue

                    target = self.chart_slots[
                        target_id
                    ]

                    if not target.chart_ready:
                        continue

                    target.browser.page().runJavaScript(
                        javascript
                    )

        # =====================================================
        # MAIN DASHBOARD + OTHER POPUPS
        # =====================================================

        #
        # Do NOT stop here after the popup-local sync.
        #
        # The dashboard is the global router.
        #

        self.dashboard.sync_crosshair(
            self,
            time
        )

    # =====================================================
    # CLEAR CROSSHAIR
    # =====================================================

    def clear_synced_crosshair(
        self,
        slot_id
    ):

        if not self.layout_sync_enabled.get(
            self.current_layout,
            True
        ):
            return

        for target_id in (
            self.visible_slot_ids()
        ):

            if target_id == slot_id:
                continue

            target = self.chart_slots[
                target_id
            ]

            if not target.chart_ready:
                continue

            target.browser.page().runJavaScript(
                "clearSyncedCrosshair();"
            )

        self.dashboard.clear_synced_crosshair(
            self
        )

    # =====================================================
    # REFRESH SLOT
    # =====================================================

    def refresh_slot(
        self,
        slot_id
    ):

        if self.closing:
            return

        if self.dashboard.current_file is None:
            return

        if slot_id < 0:
            return

        if slot_id >= len(
            self.chart_slots
        ):
            return

        slot = self.chart_slots[
            slot_id
        ]

        if not slot.chart_ready:
            return

        try:

            with perf.measure(
                "refresh.excel_load",
                extra={
                    "slot": slot_id + 1,
                    "sheet": slot.sheet,
                },
            ):
                chart_data = load_sheet(
                    self.dashboard.current_file,
                    slot.sheet
                )

        except Exception as exc:

            print(
                f"[POPUP SLOT ERROR] "
                f"Chart {slot_id + 1} "
                f"{slot.sheet}: {exc}"
            )

            slot.browser.page().runJavaScript(
                "clearChartData();"
            )

            return

        try:

            chart_data = (
                self.dashboard.prepare_timeframe(
                    chart_data,
                    slot.timeframe
                )
            )

        except Exception as exc:

            print(
                f"[POPUP TIMEFRAME ERROR] "
                f"Chart {slot_id + 1}: {exc}"
            )

            slot.browser.page().runJavaScript(
                "clearChartData();"
            )

            return

        candles = []

        with perf.measure(
            "refresh.candle_build",
            extra={
                "slot": slot_id + 1,
                "rows": len(chart_data),
            },
        ):
            for _, row in (
                chart_data.iterrows()
            ):

                try:

                    timestamp = int(
                        row[
                            "timestamp"
                        ].timestamp()
                    )

                    open_price = float(
                        row["Open"]
                    )

                    high_price = float(
                        row["High"]
                    )

                    low_price = float(
                        row["Low"]
                    )

                    close_price = float(
                        row["Close"]
                    )

                except Exception:

                    continue

                if not all(
                    math.isfinite(value)
                    for value in (
                        open_price,
                        high_price,
                        low_price,
                        close_price
                    )
                ):

                    continue

                candles.append(
                    {
                        "time": timestamp,
                        "open": open_price,
                        "high": high_price,
                        "low": low_price,
                        "close": close_price,
                    }
                )

        if not candles:

            slot.browser.page().runJavaScript(
                "clearChartData();"
            )

            return

        with perf.measure(
            "refresh.json_serialize",
            extra={
                "slot": slot_id,
                "candles": len(candles),
            },
        ):
            javascript = (
                "setChartData("
                f"{json.dumps(candles)},"
                f"{json.dumps(slot.sheet)}"
                ");"
            )


        with perf.measure(
            "refresh.js_submit",
            extra={
                "slot": slot_id + 1 if isinstance(slot_id, int) else slot_id,
                "candles": len(candles),
                "payload_bytes": len(javascript),
            },
        ):

            slot.browser.page().runJavaScript(
                javascript
            )
        
        slot.update_header()

    # =====================================================
    # REFRESH ALL SLOTS
    # =====================================================

    def refresh_all_slots(
        self
    ):

        if self.closing:
            return

        for slot_id in (
            self.visible_slot_ids()
        ):

            self.refresh_slot(
                slot_id
            )

    # =====================================================
    # UPDATE SYMBOL LIST
    # =====================================================

    def update_symbol_list(
        self
    ):

        current_symbol = (
            self.active_slot().symbol
        )

        self.symbol_combo.blockSignals(
            True
        )

        self.symbol_combo.clear()

        self.symbol_combo.addItems(
            self.dashboard.sheet_names
        )

        if current_symbol in (
            self.dashboard.sheet_names
        ):

            self.symbol_combo.setCurrentText(
                current_symbol
            )

        elif self.dashboard.sheet_names:

            slot = self.active_slot()

            slot.symbol = (
                self.dashboard.sheet_names[0]
            )

            slot.sheet = slot.symbol

            self.symbol_combo.setCurrentText(
                slot.symbol
            )

        self.symbol_combo.blockSignals(
            False
        )

    # =====================================================
    # UPDATE HEADER
    # =====================================================

    def update_header(
        self
    ):

        slot = self.active_slot()

        self.symbol_combo.blockSignals(
            True
        )

        if slot.symbol in (
            self.dashboard.sheet_names
        ):

            self.symbol_combo.setCurrentText(
                slot.symbol
            )

        self.symbol_combo.blockSignals(
            False
        )

        self.setWindowTitle(
            f"Trading Dashboard Popup • "
            f"{slot.symbol} • "
            f"{slot.timeframe}"
        )

    # =====================================================
    # CLOSE
    # =====================================================

    def closeEvent(
        self,
        event
    ):

        self.closing = True

        self.dashboard.unregister_popup(
            self
        )

        event.accept()

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

        self.data_repository = DataRepository()

        self.current_date = None

        self.panel_expanded = True

        self.active_slot_id = 0

        self.current_layout = "1_full"

        self.sheet_names = []

        self.current_timeframe = "1m"

        self.data_folder = DATA_FOLDER

        # -------------------------------------------------
        # -------------------------------------------------
        # MOUSE SYNC STATE
        # -------------------------------------------------

        # Master switch for mouse synchronization
        # originating from the MAIN WINDOW.
        self.sync_enabled = True

        # Internal chart-to-chart synchronization
        # for each layout.
        self.layout_sync_enabled = {
            layout_id: True
            for layout_id in LAYOUTS
        }

        # -------------------------------------------------
        # POPUP WINDOWS
        # -------------------------------------------------

        self.popup_windows = []
         
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

        self.symbol_combo.setFixedWidth(
            130
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

        # -------------------------------------------------
        # DATA FOLDER
        # -------------------------------------------------

        self.folder_button = QPushButton(
            "Data Folder"
        )

        self.folder_button.setFixedHeight(
            27
        )

        self.folder_button.setToolTip(
            "Select market data folder"
        )

        self.folder_button.clicked.connect(
            self.select_data_folder
        )

        toolbar_layout.addWidget(
            self.folder_button
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

        self.layouts_menu.setStyleSheet(
            """
            QMenu {
                background: #ffffff;
                border: 1px solid #d5d8dc;
                padding: 4px;
            }

            QMenu::separator {
                height: 1px;
                background: #e5e7eb;
                margin: 2px 4px;
            }
            """
        )

        layout_groups = {
            1: [
                "1_full",
            ],

            2: [
                "2_horizontal",
                "2_vertical",
            ],

            3: [
                "3_horizontal",
                "3_vertical",
                "3_large_left",
                "3_large_right",
                "3_large_top",
                "3_large_bottom",
            ],

            4: [
                "4_grid",
                "4_horizontal",
                "4_vertical",
                "4_large_left",
                "4_large_right",
                "4_large_top",
                "4_large_bottom",
            ],

            5: [
                "5_horizontal",
                "5_two_three",
            ],

            6: [
                "6_grid",
                "6_horizontal",
            ],

            8: [
                "8_grid",
                "8_horizontal",
            ],
        }

        for index, (
            count,
            layout_ids
        ) in enumerate(
            layout_groups.items()
        ):

            row_widget = LayoutMenuRow(
                self,
                count,
                layout_ids
            )

            action = QWidgetAction(
                self.layouts_menu
            )

            action.setDefaultWidget(
                row_widget
            )

            self.layouts_menu.addAction(
                action
            )

            if index < (
                len(layout_groups) - 1
            ):

                self.layouts_menu.addSeparator()

        self.layouts_button.setMenu(
            self.layouts_menu
        )

        toolbar_layout.addWidget(
            self.layouts_button
        )

        # =================================================
        # MOUSE SYNC
        # =================================================

        self.mouse_sync_button = QPushButton(
            "Mouse Sync: ON"
        )

        self.mouse_sync_button.setCheckable(
            True
        )

        self.mouse_sync_button.setChecked(
            True
        )

        self.mouse_sync_button.setFixedHeight(
            27
        )

        self.mouse_sync_button.clicked.connect(
            self.toggle_mouse_sync
        )

        toolbar_layout.addWidget(
            self.mouse_sync_button
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
            "1_full"
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

        return self.data_folder / filename

    def select_data_folder(self):
        folder = QFileDialog.getExistingDirectory(
            self,
            "Select Market Data Folder",
            str(self.data_folder)
        )

        if not folder:
            return

        self.data_folder = Path(folder)

        self.load_selected_date()

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

            self.data_repository.set_workbook(
                file_path
            )

            self.sheet_names = list(
                excel_file.sheet_names
            )

            # -------------------------------------------------
            # UPDATE SYMBOL DROPDOWN
            # -------------------------------------------------

            self.symbol_combo.blockSignals(
                True
            )

            self.symbol_combo.clear()

            self.symbol_combo.addItems(
                self.sheet_names
            )

            # -------------------------------------------------
            # UPDATE OPEN POPUP SYMBOL LISTS
            # -------------------------------------------------

            for popup in list(
                self.popup_windows
            ):

                if popup.closing:
                    continue

                popup.update_symbol_list()

            self.symbol_combo.blockSignals(
                False
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
            # -------------------------------------------------
            # REFRESH OPEN POPUPS
            # -------------------------------------------------

            for popup in list(
                self.popup_windows
            ):

                if popup.closing:
                    continue

                popup.chart_ready = (
                    popup.chart_ready
                )

                popup.update_symbol_list()

                popup.refresh_all_slots()

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

        slot = self.active_slot()
        
        if not slot.chart_ready:
            return

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

    def sync_crosshair(
        self,
        source,
        time
    ):
        """
        Synchronize crosshair from either the main dashboard
        or a popup window.

        This version preserves the working routing behaviour
        and measures the Python routing cost.
        """

        # =====================================================
        # VALIDATE TIME
        # =====================================================

        # =====================================================
        # CROSSHAIR EVENT RATE MEASUREMENT
        # =====================================================

        now = time_module.perf_counter()

        if not hasattr(
            self,
            "_crosshair_event_count"
        ):
            self._crosshair_event_count = 0
            self._crosshair_event_start = now

        self._crosshair_event_count += 1

        elapsed = (
            now
            -
            self._crosshair_event_start
        )

        if elapsed >= 1.0:

            print(
                "[CROSSHAIR RATE] "
                f"events/sec="
                f"{self._crosshair_event_count / elapsed:.1f}",
                flush=True
            )

            self._crosshair_event_count = 0
            self._crosshair_event_start = now

        if time is None:
            return

        try:
            time = float(time)

        except (
            TypeError,
            ValueError
        ):
            return

        if not math.isfinite(time):
            return

        # =====================================================
        # SOURCE SYNC STATE
        # =====================================================

        if isinstance(
            source,
            PopupChartWindow
        ):

            if not source.sync_enabled:
                return

        elif isinstance(
            source,
            ChartSlot
        ):

            if not self.sync_enabled:
                return

            if not self.layout_sync_enabled.get(
                self.current_layout,
                True
            ):
                return

            if source.slot_id not in (
                self.visible_slot_ids()
            ):
                return

        else:
            return

        # =====================================================
        # BUILD JAVASCRIPT ONCE
        # =====================================================

        javascript = (
            "syncCrosshairFromPython("
            f"{time}"
            ");"
        )

        main_targets = 0
        popup_targets = 0

        # =====================================================
        # MEASURE COMPLETE ROUTING
        # =====================================================

        with perf.measure(
            "crosshair.sync_crosshair",
            extra={
                "source_type":
                    type(source).__name__,
                "time":
                    time,
            },
        ):

            # ================================================
            # MAIN WINDOW CHARTS
            # ================================================

            if (
                self.sync_enabled
                and
                self.layout_sync_enabled.get(
                    self.current_layout,
                    True
                )
            ):

                for slot_id in (
                    self.visible_slot_ids()
                ):

                    slot = self.chart_slots[
                        slot_id
                    ]

                    # Do not update the source chart.
                    if (
                        isinstance(
                            source,
                            ChartSlot
                        )
                        and
                        slot.slot_id
                        ==
                        source.slot_id
                    ):
                        continue

                    if not slot.chart_ready:
                        continue

                    slot.browser.page().runJavaScript(
                        javascript
                    )

                    main_targets += 1

            # ================================================
            # POPUP WINDOWS
            # ================================================

            for popup in list(
                self.popup_windows
            ):

                if popup is source:
                    continue

                if popup.closing:
                    continue

                if not popup.sync_enabled:
                    continue

                for slot_id in (
                    popup.visible_slot_ids()
                ):

                    slot = popup.chart_slots[
                        slot_id
                    ]

                    if not slot.chart_ready:
                        continue

                    slot.browser.page().runJavaScript(
                        javascript
                    )

                    popup_targets += 1

        # =====================================================
        # ROUTING DEBUG
        # =====================================================

        total_targets = (
            main_targets
            +
            popup_targets
        )

        print(
            "[CROSSHAIR ROUTE] "
            f"source="
            f"{type(source).__name__} "
            f"main_targets="
            f"{main_targets} "
            f"popup_targets="
            f"{popup_targets} "
            f"total_targets="
            f"{total_targets}",
            flush=True
        )

    # =====================================================
    # CLEAR SYNCHRONIZED CROSSHAIR
    # =====================================================

    def clear_synced_crosshair(
        self,
        source
    ):

        javascript = (
            "clearSyncedCrosshair();"
        )

        # -------------------------------------------------
        # MAIN WINDOW
        # -------------------------------------------------

        if self.layout_sync_enabled.get(
            self.current_layout,
            True
        ):

            for slot_id in (
                self.visible_slot_ids()
            ):

                slot = self.chart_slots[
                    slot_id
                ]

                if (
                    isinstance(
                        source,
                        ChartSlot
                    )
                    and
                    slot.slot_id
                    ==
                    source.slot_id
                ):
                    continue

                if not slot.chart_ready:
                    continue

                slot.browser.page().runJavaScript(
                    javascript
                )

        # -------------------------------------------------
        # POPUPS
        # -------------------------------------------------

        for popup in list(
            self.popup_windows
        ):

            if popup is source:
                continue

            if popup.closing:
                continue

            if not popup.chart_ready:
                continue

            if not popup.sync_enabled:
                continue

            popup.browser.page().runJavaScript(
                javascript
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

            with perf.measure(
                "refresh.data_repository",
                extra={
                    "slot": slot_id,
                    "sheet": slot.sheet,
                    "timeframe": slot.timeframe,
                },
            ):
                chart_data = self.data_repository.get_timeframe(
                    slot.sheet,
                    slot.timeframe,
                    self.prepare_timeframe,
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
        # Timeframe preparation is now owned by DataRepository.
        # The repository returns cached/prepared data here.


        candles = []

        with perf.measure(
            "refresh.candle_build",
            extra={
                "slot": slot_id,
                "rows": len(chart_data),
            },
        ):
            for _, row in (
                chart_data.iterrows()
            ):

                timestamp = int(
                    row["timestamp"].timestamp()
                )

                open_price = float(row["Open"])
                high_price = float(row["High"])
                low_price = float(row["Low"])
                close_price = float(row["Close"])

                if not all(
                    math.isfinite(value)
                    for value in (
                        open_price,
                        high_price,
                        low_price,
                        close_price,
                    )
                ):
                    print(
                        "[INVALID CANDLE]",
                        timestamp,
                        open_price,
                        high_price,
                        low_price,
                        close_price
                    )
                    continue

                candles.append(
                    {
                        "time": timestamp,
                        "open": open_price,
                        "high": high_price,
                        "low": low_price,
                        "close": close_price,
                    }
                )

        times = [
            candle["time"]
            for candle in candles
        ]

        duplicates = (
            len(times) -
            len(set(times))
        )

        if duplicates:
            print(
                f"[DUPLICATE TIMES] {duplicates}"
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

        with perf.measure(
            "refresh.json_serialize",
            extra={
                "slot": slot_id + 1,
                "candles": len(candles),
            },
        ):
            javascript = (
                "setChartData("
                f"{json.dumps(candles)},"
                f"{json.dumps(slot.sheet)}"
                ");"
            )


        with perf.measure(
            "refresh.js_submit",
            extra={
                "slot": slot_id + 1 if isinstance(slot_id, int) else slot_id,
                "candles": len(candles),
                "payload_bytes": len(javascript),
            },
        ):
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
        print(
            f"[DRAWING] Chart {slot.slot_id + 1} -> {tool}, "
            f"ready={slot.chart_ready}"
        )

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

    def visible_slot_ids(
        self
    ):

        layout = LAYOUTS.get(
            self.current_layout
        )

        if not layout:
            return []

        return list(
            range(
                layout["count"]
            )
        )

    # =====================================================
    # LAYOUT ENGINE
    # =====================================================

    # =====================================================
    # LAYOUT ENGINE
    # =====================================================

    def set_layout(
        self,
        layout_id
    ):

        if layout_id not in LAYOUTS:
            return

        self.current_layout = (
            layout_id
        )

        self.update_mouse_sync_button()

        layout_config = LAYOUTS[
            layout_id
        ]

        rows = layout_config[
            "rows"
        ]

        cols = layout_config[
            "cols"
        ]

        positions = layout_config[
            "positions"
        ]

        chart_count = layout_config[
            "count"
        ]

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
        # ADD CHARTS
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
            >= chart_count
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
            f"{layout_id}"
            f" • "
            f"{chart_count} charts"
            f" • Active: "
            f"Chart "
            f"{self.active_slot_id + 1}"
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
    
    # =====================================================
    # LAYOUT MOUSE SYNC
    # =====================================================

    def toggle_layout_sync(
        self,
        checked
    ):

        self.layout_sync_enabled[
            self.current_layout
        ] = bool(
            checked
        )

        self.update_mouse_sync_button()

        if not checked:

            for slot_id in (
                self.visible_slot_ids()
            ):

                slot = self.chart_slots[
                    slot_id
                ]

                if not slot.chart_ready:
                    continue

                slot.browser.page().runJavaScript(
                    "clearSyncedCrosshair();"
                )

    # =====================================================
    # MASTER MOUSE SYNC
    # =====================================================

    def toggle_mouse_sync(
        self,
        checked
    ):

        self.sync_enabled = bool(
            checked
        )

        self.update_mouse_sync_button()

        # -------------------------------------------------
        # When MAIN mouse sync is turned OFF,
        # remove any crosshair that was synchronized
        # into other charts/windows.
        # -------------------------------------------------

        if not self.sync_enabled:

            javascript = (
                "clearSyncedCrosshair();"
            )

            # ---------------------------------------------
            # MAIN WINDOW CHARTS
            # ---------------------------------------------

            for slot_id in (
                self.visible_slot_ids()
            ):

                slot = self.chart_slots[
                    slot_id
                ]

                if not slot.chart_ready:
                    continue

                slot.browser.page().runJavaScript(
                    javascript
                )

            # ---------------------------------------------
            # POPUP WINDOWS
            # ---------------------------------------------

            for popup in list(
                self.popup_windows
            ):

                if popup.closing:
                    continue

                if not popup.sync_enabled:
                    continue

                for slot_id in (
                    popup.visible_slot_ids()
                ):

                    slot = popup.chart_slots[
                        slot_id
                    ]

                    if not slot.chart_ready:
                        continue

                    slot.browser.page().runJavaScript(
                        javascript
                    )
    
    # =====================================================
    # UPDATE SYNC BUTTON
    # =====================================================

    def update_mouse_sync_button(
        self
    ):

        enabled = self.sync_enabled

        self.mouse_sync_button.blockSignals(
            True
        )

        self.mouse_sync_button.setChecked(
            enabled
        )

        self.mouse_sync_button.setText(
            "Mouse Sync: ON"
            if enabled
            else
            "Mouse Sync: OFF"
        )

        self.mouse_sync_button.blockSignals(
            False
        )

    # =====================================================
    # OPEN POPUP
    # =====================================================

    def open_popup(
        self,
        source_slot
    ):

        popup = PopupChartWindow(
            self,
            source_slot
        )

        self.popup_windows.append(
            popup
        )

        popup.show()
        popup.raise_()
        popup.activateWindow()

    # =====================================================
    # UNREGISTER POPUP
    # =====================================================

    def unregister_popup(
        self,
        popup
    ):

        if popup in self.popup_windows:

            self.popup_windows.remove(
                popup
            )

        try:

            popup.browser.page().runJavaScript(
            "clearSyncedCrosshair();"
            )

        except Exception:
            pass

    # =====================================================
    # REFRESH POPUP
    # =====================================================
    # =====================================================
    # REFRESH POPUP
    # =====================================================

    def refresh_popup(
        self,
        popup
    ):

        if popup is None:
            return

        if popup.closing:
            return

        popup.refresh_all_slots()

# =====================================================
# CLOSE MAIN WINDOW
# =====================================================

# =====================================================
# CLOSE MAIN WINDOW
# =====================================================

    # =====================================================
    # CLOSE MAIN WINDOW
    # =====================================================

    def closeEvent(
        self,
        event
    ):

        for popup in list(
            self.popup_windows
        ):

            try:

                if not popup.closing:
                    popup.closing = True
                    popup.close()

            except Exception:
                pass

        self.popup_windows.clear()

        event.accept()

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
