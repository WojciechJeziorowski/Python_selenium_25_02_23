from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://www.saucedemo.com/')
print('Nazwa strony',driver.title)
time.sleep(1)

username_field = driver.find_element('id','user-name')
username_field.clear()
username_field.send_keys('standard_user')

password_field = driver.find_element('id', 'password')
password_field.clear()
password_field.send_keys('secret_sauce')

login_field = driver.find_element('id', 'login-button')
login_field.submit()

time.sleep(2)
# driver.get_screenshot_as_file('screenshot.png')
driver.quit()