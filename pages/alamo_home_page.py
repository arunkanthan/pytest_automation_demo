from playwright.sync_api import Page
from pytest_playwright.pytest_playwright import page

import config.test_config as TestConfig
from pages.base_page import BasePage


class AlamoHomePage(BasePage):
    URL = TestConfig.ALAMO_HOME_URL
    HOME_PAGE_TITLE = "Alamo Drafthouse Cinema"

    def __init__(self, page: Page):
        super().__init__(page)
        self.accept_cookies_button = page.locator(
        "#onetrust-accept-btn-handler"
    )

    def open(self) -> None:
        super().open(self.URL)

    def accept_cookies(self) -> None:
        if self.accept_cookies_button.is_visible():
            self.accept_cookies_button.click()
