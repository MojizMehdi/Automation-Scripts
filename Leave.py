from selenium import webdriver
from Login import MainLogin
import time


class Leave(MainLogin):
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\chromedriver\chromedriver.exe")
        self.driver.maximize_window()
        self.login()
        self.run()

    def run(self):
        self.driver.get("https://devlife.gaditek-hrms.sg.plesk-server.com/leaves")
        self.driver.find_element_by_xpath("/html/body/main/div/section/div[1]/div/div[1]/div/a/div/img").click()
        self.driver.find_element_by_id("start_date").click()
        time.sleep(3)
        self.driver.find_element_by_css_selector("$('#start_date_table div.picker__day--today')").click()
        self.driver.find_element_by_id("end_date").click()
        time.sleep(3)
        self.driver.find_element_by_css_selector("$('#start_date_table div.picker__day--today')").click()
        self.driver.find_element_by_id("contactnum").send_keys("03212255641")
        self.driver.find_element_by_id("reason").send_keys("Test sick leave")
        self.driver.find_element_by_id("submit")



    def __del__(self):
        print('New ticket has been created')


leave = Leave()

