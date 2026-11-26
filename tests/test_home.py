import re
from time import sleep

import pytest

from playwright.sync_api import expect
from pages.alamo_home_page import AlamoHomePage


@pytest.mark.smoke
def test_alamo_home_page(page: Page):
    item_page = AlamoHomePage(page)
    item_page.open()
    sleep(15) 
    item_page.accept_cookies()
    sleep(15)  # Wait for the page to load completely
    expect(page).to_have_title(re.compile(AlamoHomePage.HOME_PAGE_TITLE))

