from pathlib import Path
import json

import pandas as pd

from PySide6.QtCore import QUrl, Signal, Qt
from PySide6.QtWidgets import (
    QComboBox,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)
from PySide6.QtWebEngineWidgets import QWebEngineView


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


class ChartPanel(QWidget):
    """
    Reusable independent trading chart.

    Each ChartPanel owns its own:
        - sheet/instrument
        - timeframe
        - chart
        - chart state
        - future drawing manager
        - future pop-out state
    """

    sheetChanged = Signal(str)
    timeframeChanged = Signal(str)
    maximizeRequested = Signal(object)
    popOutRequested = Signal(object)

    def __init__(
        self,
        parent=None,
        sheet_names=None,
    ):
        super().__init__(parent)

        self.sheet_names = sheet_names or []

        self.current_sheet = None
        self.current_timeframe = "1m"

        self.chart_ready = False
        self.current_candles = []

        self._build_ui()

    # =====================================================
    # UI
    # =====================================================

    def _build_ui(self):

        self.setObjectName("chartPanel")

        self.setStyleSheet(
            """
            QWidget#chartPanel {
                background: #ffffff;
                border: 1px solid #d8d8d8;
            }

            QComboBox {
                background: #ffffff;
                border: 1px solid #cccccc;
                padding: 2px 5px;
                min-height: 24px;
            }

            QPushButton {
                background: #ffffff;
                border: 1px solid #cccccc;
                padding: 2px 7px;
                min-height: 24px;
            }

            QPushButton:hover {
                background: #f2f6fa;
            }

            QLabel {
                color: #333333;
            }
            """
        )

        # -------------------------------------------------
        # Panel toolbar
        # -------------------------------------------------

        self.toolbar = QWidget()

        toolbar_layout = QHBoxLayout(
            self.toolbar
        )

        toolbar_layout.setContentsMargins(
            4, 3, 4, 3
        )

        toolbar_layout.setSpacing(4)

        self.sheet_combo = QComboBox()

        self.sheet_combo.setMinimumWidth(190)

        if self.sheet_names:
            self.sheet_combo.addItems(
                self.sheet_names
            )

        toolbar_layout.addWidget(
            self.sheet_combo
        )

        self.timeframe_combo = QComboBox()

        for label, _ in TIMEFRAMES:
            self.timeframe_combo.addItem(
                label
            )

        self.timeframe_combo.setCurrentText(
            "1m"
        )

        self.timeframe_combo.setFixedWidth(65)

        toolbar_layout.addWidget(
            self.timeframe_combo
        )

        toolbar_layout.addStretch()

        # -------------------------------------------------
        # Future chart actions
        # -------------------------------------------------

        self.maximize_button = QPushButton(
            "⛶"
        )

        self.maximize_button.setToolTip(
            "Maximize chart"
        )

        self.maximize_button.setFixedWidth(32)

        toolbar_layout.addWidget(
            self.maximize_button
        )

        self.popout_button = QPushButton(
            "↗"
        )

        self.popout_button.setToolTip(
            "Pop out chart"
        )

        self.popout_button.setFixedWidth(32)

        toolbar_layout.addWidget(
            self.popout_button
        )

        # -------------------------------------------------
        # Chart
        # -------------------------------------------------

        self.browser = QWebEngineView()

        html_file = (
            Path(__file__).resolve().parent.parent
            / "web"
            / "chart_test.html"
        )

        self.browser.setUrl(
            QUrl.fromLocalFile(
                str(html_file)
            )
        )

        self.browser.loadFinished.connect(
            self._on_chart_loaded
        )

        # -------------------------------------------------
        # Main layout
        # -------------------------------------------------

        layout = QVBoxLayout(self)

        layout.setContentsMargins(
            0,
            0,
            0,
            0,
        )

        layout.setSpacing(0)

        layout.addWidget(
            self.toolbar
        )

        layout.addWidget(
            self.browser
        )

        # -------------------------------------------------
        # Signals
        # -------------------------------------------------

        self.sheet_combo.currentTextChanged.connect(
            self._sheet_changed
        )

        self.timeframe_combo.currentTextChanged.connect(
            self._timeframe_changed
        )

        self.maximize_button.clicked.connect(
            lambda: self.maximizeRequested.emit(
                self
            )
        )

        self.popout_button.clicked.connect(
            lambda: self.popOutRequested.emit(
                self
            )
        )

    # =====================================================
    # SHEET
    # =====================================================

    def _sheet_changed(self, sheet_name):

        if not sheet_name:
            return

        self.current_sheet = sheet_name

        self.sheetChanged.emit(
            sheet_name
        )

    def set_sheet_names(
        self,
        sheet_names,
    ):

        current = self.current_sheet

        self.sheet_names = list(
            sheet_names
        )

        self.sheet_combo.blockSignals(
            True
        )

        self.sheet_combo.clear()

        self.sheet_combo.addItems(
            self.sheet_names
        )

        if current in self.sheet_names:

            self.sheet_combo.setCurrentText(
                current
            )

        self.sheet_combo.blockSignals(
            False
        )

    def set_sheet(
        self,
        sheet_name,
    ):

        if sheet_name not in self.sheet_names:
            return

        self.sheet_combo.setCurrentText(
            sheet_name
        )

        self.current_sheet = sheet_name

    # =====================================================
    # TIMEFRAME
    # =====================================================

    def _timeframe_changed(
        self,
        timeframe,
    ):

        if not timeframe:
            return

        self.current_timeframe = timeframe

        self.timeframeChanged.emit(
            timeframe
        )

    def set_timeframe(
        self,
        timeframe,
    ):

        if timeframe not in dict(
            TIMEFRAMES
        ):
            return

        self.timeframe_combo.setCurrentText(
            timeframe
        )

        self.current_timeframe = timeframe

    # =====================================================
    # CHART LOADING
    # =====================================================

    def _on_chart_loaded(
        self,
        success,
    ):

        self.chart_ready = success

        if not success:
            return

        # Restore current timeframe
        self.browser.page().runJavaScript(
            f"setTimeframe("
            f"{json.dumps(self.current_timeframe)}"
            f");"
        )

        if self.current_candles:
            self.send_chart_data(
                self.current_candles,
                self.current_sheet or "",
            )

    # =====================================================
    # DATA
    # =====================================================

    def set_chart_data(
        self,
        dataframe,
        sheet_name=None,
    ):

        if dataframe is None:
            return

        if dataframe.empty:
            self.clear_chart()
            return

        df = dataframe.copy()

        if "timestamp" not in df.columns:

            if (
                "Date" in df.columns
                and "Time" in df.columns
            ):

                df["timestamp"] = pd.to_datetime(
                    df["Date"].astype(str)
                    + " "
                    + df["Time"].astype(str)
                )

        df = df.sort_values(
            "timestamp"
        )

        candles = []

        for _, row in df.iterrows():

            candles.append(
                {
                    "time": int(
                        pd.Timestamp(
                            row["timestamp"]
                        ).timestamp()
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

        self.current_candles = candles

        if sheet_name:
            self.set_sheet(
                sheet_name
            )

        self.send_chart_data(
            candles,
            sheet_name or self.current_sheet or "",
        )

    def send_chart_data(
        self,
        candles,
        sheet_name,
    ):

        if not self.chart_ready:
            return

        javascript = (
            "setChartData("
            f"{json.dumps(candles)},"
            f"{json.dumps(sheet_name)}"
            ");"
        )

        self.browser.page().runJavaScript(
            javascript
        )

    def clear_chart(self):

        self.current_candles = []

        if not self.chart_ready:
            return

        self.browser.page().runJavaScript(
            "clearChartData();"
        )

    # =====================================================
    # STATE
    # =====================================================

    def get_state(self):

        return {
            "sheet": self.current_sheet,
            "timeframe": self.current_timeframe,
        }

    def restore_state(
        self,
        state,
    ):

        if not state:
            return

        sheet = state.get(
            "sheet"
        )

        timeframe = state.get(
            "timeframe",
            "1m",
        )

        if sheet:
            self.set_sheet(
                sheet
            )

        self.set_timeframe(
            timeframe
        )
