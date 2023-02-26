from selenium import webdriver
import time
import datetime
from selenium.common.exceptions import NoSuchElementException

def make_screenshot(driver):
    now = datetime.datetime.now()
    screenshot = 'screenshot' + now.strftime('%H:%M:%S') + '.png'
    driver.get_screenshot_as_file(screenshot)

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('https://www.saucedemo.com/')
    print('Nazwa strony',driver.title)
    time.sleep(1)

    try:
        username_field = driver.find_element('id','user-name')

    except NoSuchElementException:
        make_screenshot(driver)
        raise                   #wyrzuc jaki to blad

    username_field.clear()
    username_field.send_keys('standard_user')

    password_field = driver.find_element('id', 'password')
    password_field.clear()
    password_field.send_keys('secret_sauce')

    login_field = driver.find_element('id', 'login-button')
    if not login_field.get_attribute('disabled'):
        login_field.click()

    time.sleep(1)
    driver.get_screenshot_as_file('screenshot.png')
    driver.quit()