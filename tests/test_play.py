from playwright.sync_api import Page, expect
import pytest


def test_page(page: Page):
    page.goto('https://naveenautomationlabs.com/opencart/')
    page.get_by_placeholder('Search').fill('search')
    page.locator('.input-group-btn').click()
    print(page.url)
