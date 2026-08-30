from pathlib import Path

import pandas as pd

from data.excel_loader import load_sheet


class DataRepository:
    """
    Shared data repository for the Trading Dashboard.

    Cache ownership:
        raw_cache:
            contract -> raw DataFrame

        timeframe_cache:
            (contract, timeframe) -> processed DataFrame

    The repository does not know anything about charts or UI.
    """

    def __init__(self):
        self.raw_cache = {}
        self.timeframe_cache = {}

        self.current_file = None
        self.current_file_signature = None

    # =========================================================
    # WORKBOOK
    # =========================================================

    def set_workbook(self, file_path):
        """
        Set the active workbook.

        Changing the workbook invalidates all cached data.
        """

        file_path = Path(file_path)

        signature = self._file_signature(file_path)

        if (
            self.current_file != file_path
            or self.current_file_signature != signature
        ):
            self.clear()

            self.current_file = file_path
            self.current_file_signature = signature

    def _file_signature(self, file_path):
        """
        Return a lightweight workbook identity.

        Currently based on:
            absolute path
            modification time
            file size
        """

        file_path = Path(file_path)

        stat = file_path.stat()

        return (
            str(file_path.resolve()),
            stat.st_mtime_ns,
            stat.st_size,
        )

    def _check_workbook_changed(self):
        """
        Detect an external workbook modification.

        If the workbook changed, invalidate all cached data.
        """

        if self.current_file is None:
            return False

        try:
            signature = self._file_signature(
                self.current_file
            )
        except OSError:
            self.clear()
            return True

        if signature != self.current_file_signature:

            self.raw_cache.clear()
            self.timeframe_cache.clear()

            self.current_file_signature = signature

            return True

        return False

    # =========================================================
    # RAW DATA
    # =========================================================

    def get_raw(self, contract):
        """
        Return raw contract data.

        Cache key:
            contract
        """

        if self.current_file is None:
            raise RuntimeError(
                "No workbook has been configured."
            )

        self._check_workbook_changed()

        contract = str(contract)

        if contract in self.raw_cache:

            print(
                f"[DATA] raw cache HIT | "
                f"contract={contract}"
            )

            return self.raw_cache[contract]

        print(
            f"[DATA] raw cache MISS | "
            f"contract={contract}"
        )

        df = load_sheet(
            self.current_file,
            contract,
        )

        self.raw_cache[contract] = df

        return df

    # =========================================================
    # TIMEFRAME DATA
    # =========================================================

    def get_timeframe(
        self,
        contract,
        timeframe,
        prepare_timeframe,
    ):
        """
        Return timeframe-specific data.

        Cache key:
            (contract, timeframe)

        prepare_timeframe is supplied by the caller so the
        repository does not need to know UI/application logic.
        """

        if self.current_file is None:
            raise RuntimeError(
                "No workbook has been configured."
            )

        self._check_workbook_changed()

        contract = str(contract)
        timeframe = str(timeframe)

        cache_key = (
            contract,
            timeframe,
        )

        if cache_key in self.timeframe_cache:

            print(
                f"[DATA] timeframe cache HIT | "
                f"contract={contract} | "
                f"timeframe={timeframe}"
            )

            return self.timeframe_cache[cache_key]

        print(
            f"[DATA] timeframe cache MISS | "
            f"contract={contract} | "
            f"timeframe={timeframe}"
        )

        raw_df = self.get_raw(
            contract
        )

        timeframe_df = prepare_timeframe(
            raw_df,
            timeframe,
        )

        self.timeframe_cache[cache_key] = (
            timeframe_df
        )

        return timeframe_df

    # =========================================================
    # INVALIDATION
    # =========================================================

    def invalidate_contract(self, contract):
        """
        Invalidate one contract and all of its derived
        timeframe data.
        """

        contract = str(contract)

        self.raw_cache.pop(
            contract,
            None,
        )

        keys_to_remove = [
            key
            for key in self.timeframe_cache
            if key[0] == contract
        ]

        for key in keys_to_remove:
            self.timeframe_cache.pop(
                key,
                None,
            )

    def clear(self):
        """
        Clear all cached data.
        """

        self.raw_cache.clear()
        self.timeframe_cache.clear()

    # =========================================================
    # DEBUG / MONITORING
    # =========================================================

    def cache_stats(self):
        """
        Return lightweight cache statistics.
        """

        return {
            "raw_contracts": len(
                self.raw_cache
            ),
            "timeframe_entries": len(
                self.timeframe_cache
            ),
            "raw_keys": list(
                self.raw_cache.keys()
            ),
            "timeframe_keys": list(
                self.timeframe_cache.keys()
            ),
        }
