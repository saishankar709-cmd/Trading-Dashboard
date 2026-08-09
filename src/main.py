import json
import sys
from pathlib import Path

import pandas as pd

from PySide6.QtCore import QDate, QUrl, Qt
from PySide6.QtWidgets import (
    QApplication,
    QComboBox,
    QDateEdit,
    QHBoxLayout,
    QLabel,
    QListWidget,
    QListWidgetItem,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QSplitter,
    QVBoxLayout,
    QWidget,
)
from PySide6.QtWebEngineWidgets import QWebEngineView

from data.excel_loader import load_sheet


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


class TradingDashboard(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Trading Dashboard")
        self.resize(1400, 900)

        self.current_file = None
        self.current_sheet = None
        self.chart_ready = False
        self.panel_expanded = True

        self.current_timeframe = "1m"

        # =================================================
        # TOP TOOLBAR
        # =================================================

        toolbar = QWidget()
        toolbar.setFixedHeight(36)

        toolbar_layout = QHBoxLayout(toolbar)
        toolbar_layout.setContentsMargins(8, 2, 8, 2)
        toolbar_layout.setSpacing(4)

        toolbar_layout.addWidget(QLabel("Symbol:"))

        self.symbol_combo = QComboBox()
        self.symbol_combo.addItems(["NIFTY", "SENSEX"])
        self.symbol_combo.setFixedWidth(95)
        self.symbol_combo.setFixedHeight(27)

        toolbar_layout.addWidget(self.symbol_combo)

        toolbar_layout.addSpacing(7)
        toolbar_layout.addWidget(QLabel("Date:"))

        self.date_edit = QDateEdit()
        self.date_edit.setCalendarPopup(True)
        self.date_edit.setDate(QDate(2026, 8, 5))
        self.date_edit.setDisplayFormat("dd-MMM-yyyy")
        self.date_edit.setFixedWidth(115)
        self.date_edit.setFixedHeight(27)

        toolbar_layout.addWidget(self.date_edit)

        self.load_button = QPushButton("Load")
        self.load_button.setFixedWidth(60)
        self.load_button.setFixedHeight(27)

        toolbar_layout.addWidget(self.load_button)

        toolbar_layout.addSpacing(12)

        # =================================================
        # TIMEFRAME BUTTONS
        # =================================================

        toolbar_layout.addWidget(QLabel("TF:"))

        self.timeframe_buttons = {}

        for label, minutes in TIMEFRAMES:
            button = QPushButton(label)
            button.setCheckable(True)
            button.setFixedHeight(27)
            button.setMinimumWidth(38)

            if label == "1m":
                button.setChecked(True)

            self.timeframe_buttons[label] = button

            toolbar_layout.addWidget(button)

            button.clicked.connect(
                lambda checked, tf=label:
                self.change_timeframe(tf)
            )

        toolbar_layout.addSpacing(10)

        # =================================================
        # TREND LINE BUTTON
        # =================================================

        self.trend_button = QPushButton("↗ Trend")
        self.trend_button.setCheckable(True)
        self.trend_button.setFixedHeight(27)

        toolbar_layout.addWidget(self.trend_button)

        self.trend_button.clicked.connect(
            self.toggle_trend_mode
        )

        toolbar_layout.addSpacing(10)

        self.status_label = QLabel("Ready")
        toolbar_layout.addWidget(self.status_label)

        toolbar_layout.addStretch()

        # =================================================
        # SHEETS PANEL
        # =================================================

        self.sheet_list = QListWidget()
        self.sheet_list.setMinimumWidth(220)

        sheets_title = QLabel("SHEETS")
        sheets_title.setFixedHeight(24)

        sheets_layout = QVBoxLayout()
        sheets_layout.setContentsMargins(5, 3, 5, 5)
        sheets_layout.setSpacing(2)

        sheets_layout.addWidget(sheets_title)
        sheets_layout.addWidget(self.sheet_list)

        self.sheets_panel = QWidget()
        self.sheets_panel.setLayout(sheets_layout)

        # =================================================
        # CHART
        # =================================================

        self.browser = QWebEngineView()

        html_file = (
            Path(__file__).parent
            / "web"
            / "chart_test.html"
        )

        self.browser.setUrl(
            QUrl.fromLocalFile(str(html_file))
        )

        self.browser.loadFinished.connect(
            self.on_chart_loaded
        )

        # =================================================
        # SPLITTER
        # =================================================

        self.splitter = QSplitter(Qt.Horizontal)

        self.splitter.addWidget(self.sheets_panel)
        self.splitter.addWidget(self.browser)

        self.splitter.setSizes([280, 1120])
        self.splitter.setChildrenCollapsible(True)

        # =================================================
        # PERMANENT COLLAPSE BUTTON
        # =================================================

        self.toggle_button = QPushButton("◀")
        self.toggle_button.setFixedSize(30, 30)
        self.toggle_button.setToolTip(
            "Collapse / Expand Sheets"
        )

        toggle_container = QWidget()

        toggle_layout = QVBoxLayout(toggle_container)
        toggle_layout.setContentsMargins(2, 2, 2, 0)
        toggle_layout.setSpacing(0)

        toggle_layout.addWidget(self.toggle_button)
        toggle_layout.addStretch()

        toggle_container.setFixedWidth(34)

        # =================================================
        # CONTENT
        # =================================================

        content_widget = QWidget()

        content_layout = QHBoxLayout(content_widget)
        content_layout.setContentsMargins(0, 0, 0, 0)
        content_layout.setSpacing(0)

        content_layout.addWidget(toggle_container)
        content_layout.addWidget(self.splitter)

        # =================================================
        # MAIN WINDOW
        # =================================================

        central_widget = QWidget()

        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        main_layout.addWidget(toolbar)
        main_layout.addWidget(content_widget)

        self.setCentralWidget(central_widget)

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

        # =================================================
        # INITIAL LOAD
        # =================================================

        self.load_selected_date()

    # =====================================================
    # FILE
    # =====================================================

    def get_selected_file(self):
        selected_date = self.date_edit.date().toPython()

        filename = (
            f"MarketArchive_{selected_date:%Y-%m-%d}.xlsx"
        )

        return DATA_FOLDER / filename

    # =====================================================
    # WORKBOOK
    # =====================================================

    def load_selected_date(self):
        file_path = self.get_selected_file()

        if not file_path.exists():
            self.current_file = None
            self.current_sheet = None

            self.sheet_list.clear()

            self.status_label.setText(
                f"File not found: {file_path.name}"
            )

            self.clear_chart()
            return

        try:
            excel_file = pd.ExcelFile(file_path)

            self.current_file = file_path
            self.sheet_list.clear()

            for sheet_name in excel_file.sheet_names:
                self.sheet_list.addItem(
                    QListWidgetItem(sheet_name)
                )

            self.status_label.setText(
                f"{file_path.name} • "
                f"{len(excel_file.sheet_names)} sheets"
            )

            items = self.sheet_list.findItems(
                "NIFTY",
                Qt.MatchExactly,
            )

            if items:
                self.sheet_list.setCurrentItem(
                    items[0]
                )

                self.load_sheet("NIFTY")

        except Exception as exc:
            QMessageBox.critical(
                self,
                "Workbook Error",
                f"Unable to open workbook:\n\n{exc}",
            )

    # =====================================================
    # SHEETS
    # =====================================================

    def sheet_clicked(self, item):
        self.load_sheet(item.text())

    def load_sheet(self, sheet_name):
        if self.current_file is None:
            return

        self.current_sheet = sheet_name

        try:
            chart_data = load_sheet(
                self.current_file,
                sheet_name,
            )

        except ValueError:
            self.status_label.setText(
                f"{sheet_name} • No OHLC chart data"
            )

            self.clear_chart()
            return

        except Exception as exc:
            self.status_label.setText(
                f"{sheet_name} • Error"
            )

            QMessageBox.warning(
                self,
                "Sheet Error",
                f"Unable to load '{sheet_name}':\n\n{exc}",
            )

            self.clear_chart()
            return

        chart_data = self.prepare_timeframe(
            chart_data,
            self.current_timeframe,
        )

        candles = []

        for _, row in chart_data.iterrows():

            candles.append(
                {
                    "time": int(
                        row["timestamp"].timestamp()
                    ),
                    "open": float(row["Open"]),
                    "high": float(row["High"]),
                    "low": float(row["Low"]),
                    "close": float(row["Close"]),
                }
            )

        if not candles:
            self.clear_chart()
            return

        latest_close = candles[-1]["close"]

        self.status_label.setText(
            f"{sheet_name} • "
            f"{self.current_timeframe} • "
            f"{len(candles)} candles • "
            f"Latest: {latest_close:.2f}"
        )

        self.send_chart_data(
            candles,
            sheet_name,
        )

    # =====================================================
    # TIMEFRAME ENGINE
    # =====================================================

    def prepare_timeframe(self, df, timeframe):
        df = df.copy()

        if df.empty:
            return df

        df["timestamp"] = pd.to_datetime(
            df["timestamp"]
        )

        df = df.sort_values(
            "timestamp"
        ).reset_index(drop=True)

        if timeframe == "1m":
            return df

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
                .reset_index(drop=True)
            )

            return result

        minutes = dict(TIMEFRAMES)[timeframe]

        # Number of minutes from the NSE session start.
        session_start_minutes = (
            df["timestamp"].dt.hour * 60
            + df["timestamp"].dt.minute
        )

        session_start = 9 * 60 + 15

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
                sort=True,
            )
            .agg(
                timestamp=("timestamp", "first"),
                Open=("Open", "first"),
                High=("High", "max"),
                Low=("Low", "min"),
                Close=("Close", "last"),
            )
            .reset_index(drop=True)
        )

        return result

    # =====================================================
    # TIMEFRAME SELECTION
    # =====================================================

    def change_timeframe(self, timeframe):

        self.current_timeframe = timeframe

        for label, button in self.timeframe_buttons.items():
            button.setChecked(
                label == timeframe
            )

        # Changing timeframe should not leave us
        # stuck in drawing mode.
        self.trend_button.setChecked(False)

        if self.chart_ready and self.current_sheet:
            self.load_sheet(
                self.current_sheet
            )

    # =====================================================
    # TREND LINE
    # =====================================================

    def toggle_trend_mode(self):

        enabled = self.trend_button.isChecked()

        self.browser.page().runJavaScript(
            f"setTrendMode({str(enabled).lower()});"
        )

        if enabled:
            self.status_label.setText(
                "Trend Line: click first point, "
                "then second point"
            )
        else:
            self.status_label.setText(
                f"{self.current_sheet} • "
                f"{self.current_timeframe}"
            )

    # =====================================================
    # CHART
    # =====================================================

    def on_chart_loaded(self, ok):

        if not ok:
            self.status_label.setText(
                "Chart failed to load"
            )
            return

        self.chart_ready = True

        if self.current_file and self.current_sheet:
            self.load_sheet(
                self.current_sheet
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

        if not self.chart_ready:
            return

        self.browser.page().runJavaScript(
            "clearChartData();"
        )

    # =====================================================
    # COLLAPSE / EXPAND
    # =====================================================

    def toggle_sheets_panel(self):

        if self.panel_expanded:

            self.splitter.setSizes(
                [0, self.splitter.width()]
            )

            self.toggle_button.setText("▶")
            self.panel_expanded = False

        else:

            self.splitter.setSizes(
                [
                    280,
                    max(
                        300,
                        self.splitter.width() - 280,
                    ),
                ]
            )

            self.toggle_button.setText("◀")
            self.panel_expanded = True


def main():

    app = QApplication(sys.argv)

    window = TradingDashboard()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
