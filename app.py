import os
import requests

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)







@app.route('/', methods=['GET'])
def index():
  try:
    driver=None
    import os
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.keys import Keys
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')  
    chrome_options.binary_location = "/app/.apt/usr/bin/google_chrome"
    driver=webdriver.Chrome("/app/.chromedriver/bin/chromedriver")
    driver.get("http://www.naukri.com")
    naukri_email=os.environ.get("NAUKRI_EMAIL")
    naukri_password=os.environ.get("NAUKRI_PASSWORD")
    import time
    time.sleep(3)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//a[@title='Jobseeker Login']"))).click()
    time.sleep(3)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter your active Email ID / Username']"))).send_keys(naukri_email)
    time.sleep(3)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter your password']"))).send_keys(naukri_password)
    time.sleep(3)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//button[@class='btn-primary loginButton']"))).click()
    time.sleep(3)
    driver.get("https://www.naukri.com/mnjuser/profile?id=&altresid")
    time.sleep(3)
    up_btn=WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@id='attachCV']")))
    time.sleep(3)
    import os
    import pytz
    import shutil
    from datetime import datetime
    tz = pytz.timezone('Asia/Kolkata')
    datee=str(datetime.now(tz))[:16]
    newfilepath=os.path.join(os.getcwd(),"Resume_Shakir_"+datee.replace(" ","-").replace(":","-")+"_Public.docx")
    r=requests.get("https://shakirpublicbucket.s3.ap-south-1.amazonaws.com/Resume_Shakir_Public.docx")
    with open(newfilepath,"wb")as f:
      f.write(r.content)
    #shutil.copyfile(os.path.join(os.getcwd(),"Resume_Shakir_November2020_public.docx"), newfilepath) 
    pathh=newfilepath
    up_btn.send_keys(pathh)
    time.sleep(3)
    if os.path.exists(pathh):
      os.remove(pathh)
    driver.quit()
    return render_template('index.html')
  except Exception as ex:
    if driver:
      driver.quit()
    return render_template('error.html',err="There was an error: "+str(ex))



if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  app.run(debug=True)
