from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://www.amazon.com/")

#print the current webpage title
print(driver.title)

# print browser name
print driver.name

# maximise the browser
driver.maximize_window()

# navigate to different site
driver.get("https://www.flipkart.com/")

# take screenshot
driver.save_screenshot("flipkart.png")

#navigate back to site1
driver.back()

# resize the window
driver.set_window_size(1024,768)

#print the current url
print driver.current_url

#refresh the page
driver.refresh()

#take screenshot
driver.save_screenshot("amazon.png")

# navigate farward or browser farward button
driver.forward()

#print html source code of the page
print driver.page_source.encode('utf-8')
# close the browser
driver.close()