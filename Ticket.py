from selenium import webdriver
from Login import MainLogin


class Ticket(MainLogin):
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\chromedriver\chromedriver.exe")
        self.driver.maximize_window()
        self.login("https://devlife.gaditek-hrms.sg.plesk-server.com/ticket/create")
        self.run()
        self.stop()

    def run(self):
        # ticket_option = "/html/body/aside/section/ul/li[13]/a/span[1]"
        # create_new = "/html/body/aside/section/ul/li[13]/ul/li[2]/a"
        subject_field = "subject"
        description_field = "description"
        submit_button = "form_submit"
        # self.driver.find_element_by_xpath(ticket_option).click()
        # self.driver.find_element_by_xpath(create_new).click()
        self.driver.find_element_by_name(subject_field).send_keys("Test Ticket")
        self.driver.find_element_by_name(description_field).send_keys("This is a test ticket for automation")
        self.driver.find_element_by_id(submit_button).click()

    def stop(self):
        self.driver.get("https://devlife.gaditek-hrms.sg.plesk-server.com/tickets/admin/in-progress")
        # ticket_admin = "/html/body/aside/section/ul/li[13]/ul/li[3]/a"
        first_ticket = "/html/body/main/div/section/div/div[3]/div/div/table/tbody/tr[1]/td[3]/a"
        comment_box = "comment"
        status_dropdown = "/html/body/main/div/section/div/form/div[2]/div[1]/div/div/input"
        complete_option = "/html/body/main/div/section/div/form/div[2]/div[1]/div/div/ul/li[3]/span"
        submit_admin = "submit_comment"
        # self.driver.find_element_by_xpath(ticket_admin).click()
        self.driver.find_element_by_xpath(first_ticket).click()
        self.driver.find_element_by_id(comment_box).send_keys("Test Ticket --- Completing this ticket")
        self.driver.find_element_by_xpath(status_dropdown).click()
        self.driver.find_element_by_xpath(complete_option).click()
        self.driver.find_element_by_id(submit_admin).click()

    def __del__(self):
        print('New ticket has been created')


ticket = Ticket()
