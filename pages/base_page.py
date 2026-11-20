from pathlib import Path

from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def open(self, url: str) -> None:
        self.page.goto(url)

    def title(self) -> str:
        return self.page.title()

    def take_screenshot(self, name: str) -> str:
        screenshot_dir = Path("artifacts/screenshots")
        screenshot_dir.mkdir(parents=True, exist_ok=True)
        path = screenshot_dir / name
        self.page.screenshot(path=str(path), full_page=True)
        return str(path)
