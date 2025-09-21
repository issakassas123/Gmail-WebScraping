import json
import undetected_chromedriver as uc
import time
from configparser import ConfigParser
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pyfiglet
import os
import sys
#https://jerrynsh.com/how-to-package-python-selenium-applications-with-pyinstaller/
def resource_path(relative_path: str):
    try:
        base_path = sys._MEIPASS
        
    except Exception:
        base_path = os.path.dirname(__file__)
	
    return os.path.join(base_path, relative_path)

def main():
    print(pyfiglet.figlet_format("gmailcrack" , justify = 'center'))
    print("Welcome To Gmailcracker,This Script Coding By Python\nScript Is Running Now...")
    print('#'*50)
    
    with open("data.json", "r") as file:
        credentials = json.load(file)
        username = credentials["username"]
        password = credentials["password"]

    config = ConfigParser()
    config.read("info.ini")
    DURATION = config.getint("delay", "seconds")
    URL = config.get("website", "url")
    
    driver = uc.Chrome()
    driver.delete_all_cookies()
    
    while True:
        driver.get(URL)
        time.sleep(DURATION + 2)
        
        wait = WebDriverWait(driver , timeout = 1)
        email = wait.until(EC.element_to_be_clickable((By.XPATH , '//input[@type="email"]')))
        email.send_keys(username)
        time.sleep(DURATION)
        
        # wait.until(EC.element_to_be_clickable((By.XPATH , '//*[@id="identifierNext"]')))
        # time.sleep(DURATION + 1)
        
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH , '//input[@type="password"]'))).send_keys(password)
            
        except:
            continue
        
        wait.until(EC.element_to_be_clickable((By.XPATH , '//*[@id="passwordNext"]')))
        time.sleep(DURATION + 1)
        
        if URL == driver.current_url:
            mynum = open('C:\my\mynum.txt','a')
            mynum.write(username + '\n')
            driver.close()
            driver.delete_all_cookies()

if __name__ == "__main__":
    main()