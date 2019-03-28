from selenium import webdriver
from Login import MainLogin
import time


class Lunch(MainLogin):
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\chromedriver\chromedriver.exe")
        self.driver.maximize_window()
        self.login("https://devlife.gaditek-hrms.sg.plesk-server.com/lunch/menu")
        self.run()

    def run(self):
        first_order_click = '#menu-listing > tbody > tr:nth-child(1) > td:nth-child(7) > button > i'
        place_order_button = '/html/body/main/div/section/div[1]/div[1]/div[2]/div[2]/input'
        confirm_button_popup = 'div.modal-content input.btn-green.make-order-btn'
        history_option = "/html/body/aside/section/ul/li[15]/ul/li[2]/a"
        self.driver.find_element_by_css_selector(first_order_click).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(place_order_button).click()
        time.sleep(3)
        self.driver.find_element_by_css_selector(confirm_button_popup).click()
        time.sleep(3)
        self.driver.find_element_by_xpath(history_option).click()
        rb = self.driver.find_element_by_xpath('/html/body/main/div/section/div/div[4]/div[4]/div[1]/strong').text
        amount = self.driver.find_element_by_xpath('/html/body/main/div/section/div/div[4]/div[4]/div[2]').text
        print(rb)
        print(amount)

    def __del__(self):
        print('End of lunch script')


lunch = Lunch()
