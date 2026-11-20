from playwright.sync_api import Page

from pages.base_page import BasePage


class PlaywrightHomePage(BasePage):
    URL = "https://playwright.dev"

    def __init__(self, page: Page):
        super().__init__(page)

    def open(self) -> None:
        super().open(self.URL)

    def get_started_link(self):
        return self.page.get_by_role("link", name="Get started")
