import re
from time import sleep

import pytest

from playwright.sync_api import Page, expect
from pages.alamo_home_page import AlamoHomePage


# @pytest.mark.smoke
# def test_alamo_home_page(page: Page):
#     item_page = AlamoHomePage(page)
#     item_page.open()
#     sleep(5) 
#     item_page.accept_cookies()
#     sleep(5)  # Wait for the page to load completely
#     expect(page).to_have_title(re.compile(AlamoHomePage.HOME_PAGE_TITLE))

@pytest.mark.smoke
def test_location_page_is_opened(page: Page):
    item_page = AlamoHomePage(page)
    item_page.open() 
    sleep(5) 
    item_page.accept_cookies()
    sleep(5) 
    item_page.click_on_select_location_in_show_me_section()
    item_page.select_location("Austin")
    expect(page).to_have_url("https://drafthouse.com/austin")