from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
import time

time.sleep(1)
driver = webdriver.Chrome()
driver.get('https://www.google.com/')
print('Nazwa strony',driver.title)
time.sleep(1)
button1_accept = driver.find_element('id','L2AGLb')
# L2AGLb
button1_accept.click()
search_field = driver.find_element('name','q')
search_field.send_keys('Czy jutro jest niedziela handlowa?')

# search_field.send_keys(Keys.ENTER)
search_button = driver.find_element('name','btnK')
search_button.submit()         #submit jak enter


time.sleep(2)
driver.quit()