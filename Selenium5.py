from selenium import webdriver
from Selenium4 import LoginPage
import time
from Selenium2 import make_screenshot
import pytest

test_data = [
    ('standard_user','secret_sauce','https://www.saucedemo.com/inventory.html'),
    ('locked_out_user','secret_sauce','https://www.saucedemo.com/inventory.html'),
    ('problem_user','secret_sauce','https://www.saucedemo.com/inventory.html'),
    ('performance_glitch_user','secret_sauce','https://www.saucedemo.com/inventory.html'),
]
@pytest.mark.parametrize('username, password, url', test_data)
def test_login_page(username, password, url):
    driver = webdriver.Chrome()
    page = LoginPage(driver)
    page.open()
    page.enter_username(username)
    page.enter_password(password)
    page.click_login()
    time.sleep(1)

    try:
        assert driver.current_url == url, make_screenshot(driver)
    except AssertionError:
        print('\nAsercja nie przeszła')
    else:
        print('\nAsercja przeszła')
    finally:
        print('Jestesmy po asercji')
        driver.quit()

    print('Dodałem nowego brancha')

# def test_login_page():
#     driver = webdriver.Chrome()
#     page = LoginPage(driver)
#     page.open()
#     page.enter_username('standard_user')
#     page.enter_password('secret_sauce')
#     page.click_login()
#     time.sleep(2)
#
#     try:
#         assert driver.current_url == 'https://www.saucedemo.com/inventory.html', make_screenshot(driver)
#     except AssertionError:
#         print('\nAsercja nie przeszła')
#     else:
#         print('\nAsercja przeszła')
#     finally:
#         print('Jestesmy po asercji')
#         driver.quit()