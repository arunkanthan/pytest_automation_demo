from playwright.sync_api import Page
from pytest_playwright.pytest_playwright import page

import config.test_config as TestConfig
from pages.base_page import BasePage


class AlamoHomePage(BasePage):
    URL = TestConfig.ALAMO_HOME_URL
    HOME_PAGE_TITLE = "Alamo Drafthouse Cinema"
    LOCATION_BUTTON_SELECTOR = "#ion-overlay-4 > div > ion-grid > div:nth-child(1) > a > div:has-text('{}')"
    SELECT_LOCATION_IN_SHOW_ME_SECTION = "button.show-me-slider-item:has-text('Select Location')"
    ACCEPT_COOKIES_BUTTON = "#onetrust-accept-btn-handler"

    def __init__(self, page: Page):
        super().__init__(page)


    def open(self) -> None:
        super().open(self.URL)

    def accept_cookies(self) -> None:
        if self.page.locator(self.ACCEPT_COOKIES_BUTTON).is_visible():
            self.page.locator(self.ACCEPT_COOKIES_BUTTON).click()

    def click_on_select_location_in_show_me_section(self) -> None:
        self.page.locator(self.SELECT_LOCATION_IN_SHOW_ME_SECTION).scroll_into_view_if_needed()
        if self.page.locator(self.SELECT_LOCATION_IN_SHOW_ME_SECTION).is_visible():
            self.page.locator(self.SELECT_LOCATION_IN_SHOW_ME_SECTION).click()

    def select_location(self, location_name: str) -> None:
        location_button = self.page.locator(
            self.LOCATION_BUTTON_SELECTOR.format(location_name)
        )
        location_button.scroll_into_view_if_needed()
        if location_button.is_visible():
         location_button.click()
