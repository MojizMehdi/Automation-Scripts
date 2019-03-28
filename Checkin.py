from selenium import webdriver
from Login import MainLogin
from selenium.webdriver.common.by import By

class Checkin(MainLogin):
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\chromedriver\chromedriver.exe")
        self.driver.maximize_window()
        self.login("https://devlife.gaditek-hrms.sg.plesk-server.com/checkins/give")
        self.run()
        self.checkin_history()

    def run(self):
        # checkin_option = '/html/body/aside/section/ul/li[8]/a'
        search_employee_field_id = 'employees'
        checkin_type_good = '//*[@id="checkin-create-form"]/div/div[1]/div[2]/div[1]/label'
        checkin_type_bad = '//*[@id="checkin-create-form"]/div/div[1]/div[2]/div[2]/label'
        checkin_reason_proactive = '//*[@id="checkin-create-form"]/div/div[3]/div[1]/div[1]/label'
        checkin_description_field = 'description'
        checkin_button = 'form_submit'
        checkin_name_suggestion = 'dropdown-item'
        # self.driver.find_element_by_xpath(checkin_option).click()
        self.driver.find_element_by_id(search_employee_field_id).send_keys("zahid")
        self.driver.find_element_by_class_name(checkin_name_suggestion).click()
        self.driver.find_element_by_xpath(checkin_type_good).click()
        self.driver.find_element_by_xpath(checkin_reason_proactive).click()
        self.driver.find_element_by_id(checkin_description_field).send_keys("Test checkin - Good ")
        self.driver.find_element_by_id(checkin_button).click()
        success_message = self.driver.find_element_by_xpath('//*[@id="checkin-create-form"]/div/div[5]/div/div[3]').text
        print("Good ", success_message)
        self.driver.find_element_by_id(search_employee_field_id).send_keys("zahid")
        self.driver.find_element_by_class_name(checkin_name_suggestion).click()
        self.driver.find_element_by_xpath(checkin_type_bad).click()
        self.driver.find_element_by_xpath(checkin_reason_proactive).click()
        self.driver.find_element_by_id(checkin_description_field).send_keys("Test checkin - bad ")
        self.driver.find_element_by_id(checkin_button).click()
        success_message = self.driver.find_element_by_xpath('//*[@id="checkin-create-form"]/div/div[5]/div/div[3]').text
        print("Bad ", success_message)

    def checkin_history(self):
        self.driver.find_element_by_xpath('/html/body/main/div/div/div/ul/li[2]/a').click()
        history = self.driver.find_element_by_xpath('//*[@id="checkin-history"]/div[2]/div').text
        print("\n Checkin History \n")
        print(history)

    def __del__(self):
        print('End of checkin script')


checkin = Checkin()
