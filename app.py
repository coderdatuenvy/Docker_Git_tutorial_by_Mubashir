from selenium import webdriver
from flask import Flask
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import logging
import os

app = Flask(__name__)

logging.basicConfig(
     filename='log_file_name.log',
     level=logging.DEBUG, 
     format= '[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
     datefmt='%H:%M:%S'
 )


@app.route('/')
def hello():
    logging.info("Execution Started")
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("enable-automation")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--headless")
   # service = Service(executable_path="./chromedriver_linux64/chromedriver")
    service = Service(executable_path="./chromedriver_win32/chromedriver.exe")
    driver = webdriver.Chrome()
    logging.debug(f"This is driver {driver}")
    driver.get("https://www.google.com/")
    driver.save_screenshot("ss.png")
    driver.quit()
    logging.debug(f"Executed Succesfully")
    return "TEST EXECUTED PROPERLY"

if __name__ == '__main__':
    app.run(host = '0.0.0.0',port = 8000,debug=True)