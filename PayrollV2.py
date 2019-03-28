from selenium import webdriver
from Login import MainLogin
import time
from selenium.webdriver.common.by import By
from datetime import datetime


class PayrollV2(MainLogin):
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\chromedriver\chromedriver.exe")
        self.driver.maximize_window()
        self.login("https://devlife.gaditek-hrms.sg.plesk-server.com/payroll")
        self.filter_data()
        # self.export_report()
        self.payroll_listing()

    def filter_data(self):
        self.driver.find_element_by_css_selector('input.bgcolor-white.date-range').click()
        self.driver.find_element_by_css_selector("div.daterangepicker div.calendar.left tbody td[data-title='r1c1']").click()
        self.driver.find_element_by_css_selector("div.daterangepicker div.calendar.left tbody td[data-title='r4c5']").click()
        self.driver.find_element_by_xpath('/html/body/main/div/div/div[2]/div/form/div[2]/input').click()

    # def export_report(self):
    #     self.driver.find_element_by_xpath('//*[@id="payroll-listing-table_wrapper"]/div[1]/a').click()

    def payroll_listing(self):
        table_class = self.driver.find_element_by_css_selector('.dataTables_scroll')

        rows = table_class.find_elements_by_tag_name("tr")  # get all of the rows in the table

        payroll_data = []
        for row in rows:
            row_date = row.find_elements_by_tag_name("td")[0].text.strip()
            if row_date:
                # Get the columns (all the column 2)
                d = datetime.strptime(row_date, '%a, %d %B').strftime('2018%m%d')
                print(str(d))
                payroll_data.append({
                    int(d): {
                        "code": row.find_elements_by_tag_name("td")[1].text.strip(),
                        "employee_name": row.find_elements_by_tag_name("td")[2].text.strip(),
                        "designation": row.find_elements_by_tag_name("td")[3].text.strip(),
                        "time_spent": row.find_elements_by_tag_name("td")[4].text.strip(),
                        "department": row.find_elements_by_tag_name("td")[5].text.strip(),
                        "project": row.find_elements_by_tag_name("td")[6].text.strip(),
                        "D.O.J": row.find_elements_by_tag_name("td")[7].text.strip()
                    }
                })
                row.find_elements_by_tag_name("td")[7].text.strip()

        print(payroll_data)  # prints text from the element


payroll = PayrollV2()
