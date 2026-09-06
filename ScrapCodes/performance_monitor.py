import os
import time
import threading
import tracemalloc
from contextlib import contextmanager


# ============================================================
# Performance Monitoring
# ============================================================

ENABLED = True


def _rss_mb():
    """
    Return current process RSS in MB.

    Uses psutil when available. If unavailable, returns None.
    """
    try:
        import psutil

        process = psutil.Process(os.getpid())
        return process.memory_info().rss / (1024 * 1024)
    except Exception:
        return None


def _format_ms(value):
    if value is None:
        return "n/a"
    return f"{value:.3f} ms"


def _format_mb(value):
    if value is None:
        return "n/a"
    return f"{value:.2f} MB"


class PerformanceMonitor:
    """
    Lightweight performance instrumentation for V2.

    This class is intentionally independent of the application's
    architecture. It only measures operations.
    """

    def __init__(self, enabled=True):
        self.enabled = enabled
        self.results = []
        self._lock = threading.Lock()

    @contextmanager
    def measure(self, name, *, extra=None):
        if not self.enabled:
            yield
            return

        start = time.perf_counter()
        start_rss = _rss_mb()

        try:
            yield
        finally:
            elapsed_ms = (time.perf_counter() - start) * 1000
            end_rss = _rss_mb()

            delta_rss = None

            if start_rss is not None and end_rss is not None:
                delta_rss = end_rss - start_rss

            result = {
                "name": name,
                "elapsed_ms": elapsed_ms,
                "start_rss_mb": start_rss,
                "end_rss_mb": end_rss,
                "delta_rss_mb": delta_rss,
                "extra": extra or {},
            }

            with self._lock:
                self.results.append(result)

            message = (
                f"[PERF] {name} | "
                f"time={_format_ms(elapsed_ms)} | "
                f"RSS={_format_mb(end_rss)}"
            )

            if delta_rss is not None:
                message += f" | ΔRSS={delta_rss:+.2f} MB"

            if extra:
                formatted_extra = " | ".join(
                    f"{key}={value}"
                    for key, value in extra.items()
                )
                message += f" | {formatted_extra}"

            print(message, flush=True)

    def mark(self, name, *, extra=None):
        """
        Record a point-in-time RSS measurement.
        """
        if not self.enabled:
            return

        rss = _rss_mb()

        result = {
            "name": name,
            "elapsed_ms": None,
            "start_rss_mb": rss,
            "end_rss_mb": rss,
            "delta_rss_mb": None,
            "extra": extra or {},
        }

        with self._lock:
            self.results.append(result)

        message = (
            f"[PERF] {name} | "
            f"RSS={_format_mb(rss)}"
        )

        if extra:
            formatted_extra = " | ".join(
                f"{key}={value}"
                for key, value in extra.items()
            )
            message += f" | {formatted_extra}"

        print(message, flush=True)

    def summary(self):
        """
        Print all collected measurements.
        """
        if not self.enabled:
            return

        print("\n" + "=" * 72)
        print("V2 PERFORMANCE SUMMARY")
        print("=" * 72)

        for result in self.results:
            name = result["name"]
            elapsed = _format_ms(result["elapsed_ms"])
            rss = _format_mb(result["end_rss_mb"])
            delta = result["delta_rss_mb"]

            if delta is None:
                delta_text = "n/a"
            else:
                delta_text = f"{delta:+.2f} MB"

            print(
                f"{name:<40} "
                f"time={elapsed:<14} "
                f"RSS={rss:<14} "
                f"ΔRSS={delta_text}"
            )

        print("=" * 72)

    def clear(self):
        with self._lock:
            self.results.clear()


# Global monitor.
perf = PerformanceMonitor(enabled=ENABLED)


def enable_tracemalloc():
    """
    Optional detailed Python allocation tracking.

    Not enabled by default because tracemalloc itself adds overhead.
    """
    if not tracemalloc.is_tracing():
        tracemalloc.start()


def tracemalloc_snapshot(label="snapshot"):
    """
    Capture a Python allocation snapshot.

    Use only for detailed investigations, not normal baseline runs.
    """
    if not tracemalloc.is_tracing():
        return None

    snapshot = tracemalloc.take_snapshot()

    print(
        f"[PERF] tracemalloc snapshot captured: {label}",
        flush=True,
    )

    return snapshot
