from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium.webdriver.common.action_chains
from selenium.webdriver.common.action_chains import ActionChains
import selenium.webdriver.common.actions
import time
import os
from selenium.webdriver.common.by import By


chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(options=chrome_options)

U = "sidra334@hotmail.com"
P = "gangster420"

def login():
    driver.get("https://www.facebook.com/")
    wait = WebDriverWait(driver, 18)
    element = wait.until(EC.visibility_of_element_located((By.ID, 'email')))
    element.send_keys(U)
    element2 = wait.until(EC.visibility_of_element_located((By.ID, 'pass')))
    element2.send_keys(P)
    button = wait.until(EC.visibility_of_element_located((By.ID, 'loginbutton')))
    button.click()
    search = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, '_1frb')))
    search.send_keys("paris91")
    button1 = wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[2]/div/div[1]/div/div/div/div[1]/div[2]/div/form/button/i')))
    button1.click()
    # time.sleep(20)
    button2 = wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[3]/div[1]/div/div[2]/div/div/div/div/div/div/div/div/ul/li[6]/a/div/div[1]')))
    button2.click()
    # time.sleep(20)
    button3 = wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[3]/div[1]/div/div[3]/div[2]/div/div/div[2]/div/div/div/div[1]/div/div/div/div[2]/div/div[1]/div[1]/div/div/div/div/a')))
    button3.click()
    # time.sleep(20)
    button4 = wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[3]/div[1]/div/div/div[1]/div/div/div[3]/div[3]/a')))
    button4.click()
    # time.sleep(20)
    # wait.until(EC.url_to_be('https://www.facebook.com/parisninetyone/'))
    # driver.get("https://www.facebook.com/pg/parisninetyone/about/?ref=page_internal")
    category = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[2]/div/div[3]/div/div/div[2]/div[1]/div/div[2]/div[2]'))).text
    print(category)
    category1 = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[2]/div/div[3]/div/div/div[2]/div[1]/div/div[3]/div[2]'))).text 
    print(category1)
    if category and category1:
        email = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[2]/div/div[3]/div/div/div[2]/div[1]/div/div[1]/div[3]/div[2]/a/div'))).text 
        print(email)
    else:
        print("N/A")
    time.sleep(2)
    
login() 