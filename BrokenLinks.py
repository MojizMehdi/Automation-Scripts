import requests
from selenium import webdriver
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=r"C:\chromedriver\chromedriver.exe")
driver.maximize_window()
driver.get('http://devlife.gaditek-hrms.sg.plesk-server.com/')

Email = "mojiz.mehdi@gaditek.com"
password = "mojizmehdi1"


ids = {'EmailTxtBox': "employee_id",
       'passwordTxtBox': "password",
       'submitButton': "emp_login"}

driver.find_element_by_id(ids['EmailTxtBox']).clear()
driver.find_element_by_id(ids['EmailTxtBox']).send_keys(Email)
driver.find_element_by_id(ids['passwordTxtBox']).clear()
driver.find_element_by_id(ids['passwordTxtBox']).send_keys(password)
driver.find_element_by_id(ids['submitButton']).click()

timeout = 20
try:
    element_present = EC.presence_of_element_located((By.ID, 'element_id'))
    WebDriverWait(driver, timeout).until(element_present)
except TimeoutException:
    print("Timed out waiting for page to load")

links = driver.find_elements_by_css_selector("a")
for link in links:
    if hasattr(link, "href") and link.get_attribute('href') not in 'javascript:void':
        r = requests.head(link.get_attribute('href'))
        print(link.get_attribute('href'), r.status_code)
    else:
        print(link.get_attribute('href'), "200")

# code for fetching all links in a URL
# elems = driver.find_elements_by_xpath("//a[@href]")
# for elem in elems:
# print(elem.get_attribute("href"))
