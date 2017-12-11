# By ID
# By Class Name
# By Name
# By xpath
# By CSS Path
# By Link Text
# Tag Name - send out keyboard entries like closing the browser

from selenium import webdriver
from time import sleep


# Browser
driver = webdriver.Chrome()

# Login to the appliation
# driver.get('http://127.0.0.1/orangehrm/symfony/web/index.php/auth/login')
# sleep(2)
# Input Username
# username = driver.find_element_by_class_name('textInputContainer')
# username.send_keys('admin')
driver.get('https://www.amazon.com/')
driver.find_element_by_id('twotabsearchtextbox').send_keys('alexa')
driver.find_element_by_css_selector('#nav-cart > span.nav-cart-icon.nav-sprite').click()
# Input Password

#Click on submit button
