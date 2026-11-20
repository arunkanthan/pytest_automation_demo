from pathlib import Path

import pytest


@pytest.fixture(scope="session")
def base_url() -> str:
    return "https://playwright.dev"


@pytest.fixture(autouse=True)
def attach_page_for_screenshots(request, page):
    request.node._browser_page = page
    yield
    request.node._browser_page = None


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = getattr(item, "_browser_page", None)
        if page is not None:
            screenshot_dir = Path("artifacts/screenshots")
            screenshot_dir.mkdir(parents=True, exist_ok=True)
            page.screenshot(path=str(screenshot_dir / f"{item.name}-failure.png"), full_page=True)
