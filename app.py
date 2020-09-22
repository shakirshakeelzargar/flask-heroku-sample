import os

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)






@app.route('/', methods=['GET'])
def index():
  try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.keys import Keys
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.binary_location = "/app/.apt/usr/bin/google_chrome"
    driver=webdriver.Chrome("/app/.chromedriver/bin/chromedriver")
    driver.get("http://www.naukri.com")
    return render_template('index.html')
  except Exception as ex:
    return render_template('error.html',err=str(ex))



if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  app.run(debug=True)
