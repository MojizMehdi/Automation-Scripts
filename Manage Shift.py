from selenium import webdriver
from Login import MainLogin
import time
from selenium.webdriver.common.keys import Keys


class ManageShift(MainLogin):
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\chromedriver\chromedriver.exe")
        self.driver.maximize_window()
        self.login("https://devlife.gaditek-hrms.sg.plesk-server.com/attendance/shifts")
        self.listing()
        self.create_shift()

    def listing(self):
        data = self.driver.find_element_by_css_selector("body > main > div > section").text
        print(data)
        print("\n ---------------------------------------------------------- \n")

    def create_shift(self):
        create_button = "act_btn"
        shift_code_field = "ats_code"
        shift_name_field = "ats_name"
        day_radio = "#target_create_form>div>div:nth-child(1)>div:nth-child(3)>div>span.cre-tea-radio.m-l-none>label"
        arrival_allow_time = "ats_aa_time"
        start_time = "ats_start_time"
        end_time = "ats_end_time"
        shift_late = "ats_shift_late_time"
        overtime = "ats_overtime_start_at"
        remarks_field = "ats_remarks"
        submit_button = "form_submit"
        success_message = "/html/body/main/div/section/div[1]"

        # self.driver.find_element_by_xpath("//*[contains(text(), 'Attendance')]").click()

        # / html / body / aside / section / ul / li[1] / a / span

        self.driver.find_element_by_class_name(create_button).click()
        self.driver.find_element_by_name(shift_code_field).send_keys("BB")
        self.driver.find_element_by_name(shift_name_field).send_keys("Demo Shift ")
        self.driver.find_element_by_css_selector(day_radio).click()
        self.driver.find_element_by_id(arrival_allow_time).click()
        time.sleep(1)
        i = 1
        while i < 6:
            self.driver.find_element_by_id(arrival_allow_time).send_keys(Keys.BACK_SPACE)
            i += 1
        self.driver.find_element_by_id(arrival_allow_time).send_keys("11:00")
        self.driver.find_element_by_id(start_time).click()
        time.sleep(1)
        i = 1
        while i < 6:
            self.driver.find_element_by_id(start_time).send_keys(Keys.BACK_SPACE)
            i += 1
        self.driver.find_element_by_id(start_time).send_keys("11:30")
        self.driver.find_element_by_id(end_time).click()
        time.sleep(1)
        i = 1
        while i < 6:
            self.driver.find_element_by_id(end_time).send_keys(Keys.BACK_SPACE)
            i += 1
        self.driver.find_element_by_id(end_time).send_keys("20:30")
        self.driver.find_element_by_id(shift_late).click()
        time.sleep(1)
        i = 1
        while i < 6:
            self.driver.find_element_by_id(shift_late).send_keys(Keys.BACK_SPACE)
            i += 1
        self.driver.find_element_by_id(shift_late).send_keys("12:00")
        self.driver.find_element_by_id(overtime).click()
        time.sleep(1)
        i = 1
        while i < 6:
            self.driver.find_element_by_id(overtime).send_keys(Keys.BACK_SPACE)
            i += 1
        self.driver.find_element_by_id(overtime).send_keys("21:00")
        self.driver.find_element_by_id(remarks_field).send_keys("Test Automation shift sample")
        self.driver.find_element_by_id(submit_button).click()
        message = self.driver.find_element_by_xpath(success_message).text
        print(message)


manageshift = ManageShift()

