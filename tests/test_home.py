import re
from time import sleep

import pytest
from playwright.sync_api import Page, expect

from pages.playwright_home_page import PlaywrightHomePage


@pytest.mark.smoke
def test_playwright_home_page(page: Page):
    item_page = PlaywrightHomePage(page)
    item_page.open()

    sleep(10)  # Wait for the page to load
    expect(page).to_have_title(re.compile("Playwright"))
    expect(item_page.get_started_link()).to_be_visible()
