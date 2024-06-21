from playwright.sync_api import Page, expect
import pytest
from playwright.sync_api import sync_playwright


def test_title(page: Page):
    page.goto("https://www.saucedemo.com/")
    assert page.title() == "Swag Labs"


def test_inventory_site(page: Page):
    page.goto("https://www.saucedemo.com/inventory.html")
    assert page.inner_text('h3') == "Epic sadface: You can only access '/inventory.html' when you are logged in."


def test_login_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Откройте страницу входа
        page.goto("https://example.com/login")

        # Введите логин
        page.fill("input[name='username']", "username")

        # Введите пароль
        page.fill("input[name='password']", "password")

        # Нажмите кнопку входа
        page.click("button[type='submit']")

        # Проверка успешного входа
        assert page.url == "https://example.com/dashboard"

        context.close()
        browser.close()
