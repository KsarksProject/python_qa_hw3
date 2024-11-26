import pytest
from selene import browser


@pytest.fixture(scope='function')
def browser_with_custom_size():
    # Настройка размера окна браузера
    browser.config.window_width = 1280
    browser.config.window_height = 720
    browser.open('https://www.google.com/ncr')
    yield browser
    browser.quit()
