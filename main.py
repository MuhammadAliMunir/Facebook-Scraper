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
from csv import writer
import csv
import re 
# from tempfile import NamedTemporaryFile
# import shutil

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 18)

U = "sidra334@hotmail.com"
P = "gangster420"

def login():
    driver.get("https://www.facebook.com/")
    element = wait.until(EC.visibility_of_element_located((By.ID, 'email')))
    element.send_keys(U)
    element2 = wait.until(EC.visibility_of_element_located((By.ID, 'pass')))
    element2.send_keys(P)
    button = wait.until(EC.visibility_of_element_located((By.ID, 'loginbutton')))
    button.click()
def check(email):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if(re.search(regex,email)):  
        return True  
    else:  
        return False
def getEmail(key):
    try:
        wait = WebDriverWait(driver, 18)
        search = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, '_1frb')))
        search.clear()
        search.send_keys(key)
        button1 = wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[2]/div/div[1]/div/div/div/div[1]/div[2]/div/form/button/i')))
        button1.click()
        button2 = wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[3]/div[1]/div/div[2]/div/div/div/div/div/div/div/div/ul/li[6]/a/div/div[1]')))
        button2.click()
        button3 = wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[3]/div[1]/div/div[3]/div[2]/div/div/div[2]/div/div/div/div[1]/div/div/div/div[2]/div/div[1]/div[1]/div/div/div/div/a')))
        button3.click()
        button4 = wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[3]/div[1]/div/div/div[1]/div/div/div[3]/div[3]/a')))
        # button4.click()
        url = driver.current_url
        driver.get(url+"about")
        # wait.until(EC.url_to_be('https://www.facebook.com/parisninetyone/'))
        # driver.get("https://www.facebook.com/pg/parisninetyone/about/?ref=page_internal")
        try:
            email_section1 = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[2]/div/div[3]/div/div/div[2]/div[1]/div/div[1]/div[3]/div[2]/a/div'))).text 
            print(email_section1)
            if check(email_section1) == True:
                return email_section1
        except:
            print('')
        wait = WebDriverWait(driver, 3)
        try:
            email_section2 = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[2]/div/div[3]/div/div/div[2]/div[1]/div/div[2]/div[3]/div[2]/a/div'))).text 
            print(email_section2)
            if check(email_section2) == True:
                return email_section2
        except:
            print('')
        try:
            email_section3 = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[2]/div/div[3]/div/div/div[2]/div[1]/div/div[2]/div[4]/div[2]/div[2]/div/text()[2]'))).text 
            print(email_section3)
            if check(email_section3) == True:
                return email_section3
        except:
            print('')
        try:
            category = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[2]/div/div[3]/div/div/div[2]/div[1]/div/div[2]/div[2]'))).text
            print(category)
        except:
            print('')
        try:
            category1 = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[2]/div/div[3]/div/div/div[2]/div[1]/div/div[3]/div[2]'))).text 
            print(category1)
        except:
            print('')
        
        if category and category1:
            email = wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[2]/div/div[3]/div/div/div[2]/div[1]/div/div[1]/div[3]/div[2]/a/div'))).text 
            # email = wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'_50f4'))).text 
            print(email)
            if check(email) == True:
                return email
        else:
            print("N/A")
            return "N/A"
    except:
        return "N/A"

    time.sleep(2)
def setEamil(data):
    with open('output.csv', 'a+', newline=''  ) as write_obj:
        csv_writer = writer(write_obj,delimiter=",")
        csv_writer.writerow(data)

def loadData():
    # tempfile = NamedTemporaryFile(delete=False)
    # with open('Book1.csv', 'rb') as csvFile, tempfile:
    #     reader = csv.reader(csvFile, delimiter=',', quotechar='"')
    #     writer = csv.writer(tempfile, delimiter=',', quotechar='"')

    # for row in reader:
    #     row[1] = row[1].title()
    #     writer.writerow(row)
    with open('Book1.csv', 'r', errors='ignore') as file:
        reader = csv.reader(file, delimiter=",")
        i = 1
        for row in reader:
            if i > 1:
                print(row[2])
                email = getEmail(row[2])
                row[5] = row[5]+','+email
                setEamil(row)
            i += 1
login()
loadData()