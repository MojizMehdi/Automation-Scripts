from selenium import webdriver
from Login import MainLogin


class Members(MainLogin):
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\chromedriver\chromedriver.exe")
        self.login("https://devlife.gaditek-hrms.sg.plesk-server.com/members")
        self.run()

    def run(self):
        # member_option = "/html/body/aside/section/ul/li[2]/a/span"
        search_field_member = "employee_listing_search"
        search_button_memeber = "employee_listing_submit"
        first_option_member = "/html/body/main/div/section/div/div[2]/div/div[1]/div[2]/h4/a"
        # self.driver.find_element_by_xpath(member_option).click()
        self.driver.find_element_by_id(search_field_member).send_keys("Mojiz")
        self.driver.find_element_by_id(search_button_memeber).click()
        search_result = self.driver.find_element_by_xpath(first_option_member).text
        print('Name is ', search_result)
        field_radio_button = "/html/body/main/div/section/div/form/div[1]/span[2]/div/label"
        self.driver.find_element_by_xpath(field_radio_button).click()
        select_search_dropdown = "/html/body/main/div/section/div/form/div[2]/div[1]/div/div/input"
        self.driver.find_element_by_xpath(select_search_dropdown).click()
        designation_option = "/html/body/main/div/section/div/form/div[2]/div[1]/div/div/ul/li[2]/span"
        self.driver.find_element_by_xpath(designation_option).click()
        self.driver.find_element_by_id(search_field_member).send_keys('Assistant Manager')
        self.driver.find_element_by_id(search_button_memeber).click()
        title_desg = '/html/body/main/div/section/div/div[2]/div/div[1]/div[2]/div[1]/table/tbody/tr[1]/td[2]'
        designation = self.driver.find_element_by_xpath(title_desg).text
        print('designation is', designation)
        print('Search is working fine')

    def __del__(self):
        print('End of Members script')


members = Members()

