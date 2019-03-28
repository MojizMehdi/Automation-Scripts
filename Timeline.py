import unittest
from selenium import webdriver

url = "http://devlife.gaditek-hrms.sg.plesk-server.com/"
Email = "mojiz.mehdi@gaditek.com"
password = "mojizmehdi1"


ids = {'EmailTxtBox': "employee_id",
       'passwordTxtBox': "password",
       'submitButton': "emp_login"}

driver = webdriver.Firefox()
driver.get(url)

driver.find_element_by_id(ids['EmailTxtBox']).clear()
driver.find_element_by_id(ids['EmailTxtBox']).send_keys(Email)
driver.find_element_by_id(ids['passwordTxtBox']).clear()
driver.find_element_by_id(ids['passwordTxtBox']).send_keys(password)
driver.find_element_by_id(ids['submitButton']).click()
