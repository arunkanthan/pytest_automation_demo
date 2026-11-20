# Playwright Web Automation Framework

A pytest and Playwright framework using Page Object Model patterns.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
playwright install chromium
```

## Run tests

```bash
pytest
pytest --headed
pytest -m smoke
pytest --browser chromium
```

## Structure

- `pages/`: Page Object classes
- `tests/`: pytest test modules
- `conftest.py`: shared fixtures and failure hooks
- `artifacts/screenshots/`: failure screenshots
