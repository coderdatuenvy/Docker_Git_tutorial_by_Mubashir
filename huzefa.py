from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
browser = webdriver.Firefox()
browser.implicitly_wait(30)
browser.get('https://accounts.google.com/ServiceLogin?service=mail&passive=true&rm=false&continue=https://mail.google.com/mail/&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1#identifier')
email = browser.find_element_by_xpath('//*[@id="Email"]')
email.clear()
email.send_keys("email@gmail.com")  # change email
email.send_keys(Keys.RETURN)
password = browser.find_element_by_xpath('//*[@id="Passwd"]')
password.clear()
password.send_keys("password")  # Change Password
password.send_keys(Keys.RETURN)
time.sleep(10)
browser.save_screenshot('screen_shot.png')
browser.close()