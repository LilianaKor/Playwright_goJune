import time
from idlelib import browser

from  playwright.sync_api import Page, expect


def test_wiki(page: Page):
    page.goto('https://en.wikipedia.org/wiki/Main_Page')
    print(page.title())
    page.get_by_role('link', name='Welcome to Wikipedia')
    expect(page.get_by_text('Welcome to Wikipedia')).to_be_visible()
    time.sleep(5)



def test_wiki2(page: Page):
    page.goto('https://en.wikipedia.org/wiki/Main_Page')
    page.get_by_role('link', name='Welcome to Wikipedia')
    page.locator('#vector-main-menu-dropdown-checkbox').click()
    page.get_by_role('link', name='Contents').click()
    page.locator('#ca-talk').click()
    time.sleep(3)
    expect(page.locator('#firstHeading')).to_have_text('Wikipedia talk:Contents')