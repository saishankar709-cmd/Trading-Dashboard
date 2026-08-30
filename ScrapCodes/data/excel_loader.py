from src.performance_monitor import perf
from pathlib import Path

import pandas as pd


def load_sheet(file_path: str | Path, sheet_name: str) -> pd.DataFrame:
    """
    Load one market-data worksheet from an Excel workbook.

    Returns a DataFrame sorted chronologically with:
    timestamp, open, high, low, close, volume
    """

    file_path = Path(file_path)

    df = pd.read_excel(
        file_path,
        sheet_name=sheet_name,
    )

    required_columns = [
        "Date",
        "Time",
        "Open",
        "High",
        "Low",
        "Close",
    ]

    missing = [column for column in required_columns if column not in df.columns]

    if missing:
        raise ValueError(
            f"Sheet '{sheet_name}' is missing required columns: {missing}"
        )

    # Combine the separate Excel Date and Time columns.
    df["timestamp"] = pd.to_datetime(
        df["Date"].astype(str) + " " + df["Time"].astype(str),
        errors="coerce",
    )

    # Remove rows where the timestamp or OHLC data is invalid.
    df = df.dropna(
        subset=[
            "timestamp",
            "Open",
            "High",
            "Low",
            "Close",
        ]
    ).copy()

    # The workbook stores newest → oldest.
    # Charts need oldest → newest.
    df = df.sort_values("timestamp").reset_index(drop=True)

    columns = [
        "timestamp",
        "Open",
        "High",
        "Low",
        "Close",
    ]

    if "Volume" in df.columns:
        columns.append("Volume")

    return df[columns]
