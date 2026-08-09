# Trading Dashboard — Development Progress

## Project Status

**Current Status:** Layout module under active development  
**Last Working Baseline:** GitHub-synced project copy  
**Current Priority:** Stabilize multi-layout architecture before proceeding to Custom Layout Mapping / Pop-Out

---

# 1. Project Foundation

## Completed

- Python/PySide6 desktop application established.
- `QWebEngineView` integrated for web-based chart rendering.
- Trading chart implemented using Lightweight Charts.
- Local Lightweight Charts JavaScript file integrated.
- Project structure established:

```text
Trading-Dashboard/
│
├── src/
│   ├── main.py
│   │
│   └── web/
│       ├── chart_test.html
│       └── lightweight-charts.js
│
└── ...
