from selenium import webdriver

DRIVER = 'chromedriver'
driver = webdriver.Chrome()
driver.get('https://www.spotify.com')
screenshot = driver.save_screenshot('my_screenshot.png')
driver.quit()