from selenium import webdriver
from Login import MainLogin
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
start_time = time.time()
from datetime import datetime


class Attendancev2(MainLogin):
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\chromedriver\chromedriver.exe")
        self.driver.maximize_window()
        self.login("https://devlife.gaditek-hrms.sg.plesk-server.com/attendance/v2")
        self.leave_count()
        self.calculation()
        self.add_slot()
        self.logout()
        self.login_admin()
        self.discrepancy()
        time.sleep(3)
        self.quit()

    def leave_count(self):
        self.driver.find_element_by_xpath('/html/body/aside/section/ul/li[4]/a/span[1]').click()
        self.driver.find_element_by_xpath('/html/body/aside/section/ul/li[4]/ul/li[1]/a').click()
        sick_count = self.driver.find_element_by_xpath('/html/body/main/div/section/div[1]/div[2]/div/div[2]/span[1]').text
        casual_count = self.driver.find_element_by_xpath("/html/body/main/div/section/div[1]/div[3]/div/div[2]/span[1]").text
        paid_count = self.driver.find_element_by_xpath("/html/body/main/div/section/div[1]/div[4]/div/div[2]/span[1]").text
        overeall_time = self.driver.find_element_by_xpath("/html/body/main/div/section/div[1]/div[1]/div/div[2]/span[1]").text
        print('Overeall Difference ' + overeall_time, '\n Sick Leaves ' + sick_count, '\n Casual Leaves ' + casual_count, '\n Paid Leaves ' + paid_count)

    def calculation(self):
        table_id = self.driver.find_element_by_id("table-body")
        rows = table_id.find_elements_by_tag_name("tr")  # get all of the rows in the table

        attendance = []
        for row in rows:
            row_date = row.find_elements_by_tag_name("td")[0].text.strip()
            if row_date:
                # Get the columns (all the column 2)
                d = datetime.strptime(row_date, '%a, %d %B').strftime('2018%m%d')
                print(str(d))
                attendance.append({
                    int(d): {
                        "status": row.find_elements_by_tag_name("td")[1].text.strip(),
                        "time_in": row.find_elements_by_tag_name("td")[2].text.strip(),
                        "time_out": row.find_elements_by_tag_name("td")[3].text.strip(),
                        "time_spent": row.find_elements_by_tag_name("td")[4].text.strip(),
                        "break": row.find_elements_by_tag_name("td")[5].text.strip(),
                        "work_hours": row.find_elements_by_tag_name("td")[6].text.strip(),
                        "difference": row.find_elements_by_tag_name("td")[7].text.strip()
                    }
                })
                row.find_elements_by_tag_name("td")[7].text.strip()

        print(attendance)  # prints text from the element
        # print(attendance[20181030]['time_in'])  # prints text from the element

    def add_slot(self):
        date = self.driver.find_element_by_css_selector("#table-body > tr:nth-child(1) > td:nth-child(1)").text
        print(date)
        self.driver.find_element_by_css_selector("#table-body > tr:nth-child(1) > td:nth-child(1)").click()
        # clicking on Add Slot option
        self.driver.find_element_by_css_selector("#table-body > tr:nth-child(2) > td:nth-child(3) > span").click()
        # selecting hours in punch in time
        self.driver.find_element_by_css_selector("td.punchin-time div.hour input.select-dropdown").click()
        time.sleep(1)
        # Selecting punch in time 10:20 a.m.
        self.driver.find_element_by_css_selector("td.punchin-time div.hour ul.select-dropdown li:nth-child(7)").click()
        # selecting minutes from punch in time
        self.driver.find_element_by_css_selector("td.punchin-time div.minute input.select-dropdown").click()
        time.sleep(1)
        self.driver.find_element_by_css_selector("td.punchin-time div.minute ul.select-dropdown li:nth-child(21)").click()

        # Selecting punch out time
        self.driver.find_element_by_css_selector("td.punchout-time div.hour input.select-dropdown").click()
        time.sleep(1)
        self.driver.find_element_by_css_selector("td.punchout-time div.hour ul.select-dropdown li:nth-child(9)").click()
        self.driver.find_element_by_css_selector("td.punchout-time div.minute input.select-dropdown").click()
        time.sleep(1)
        self.driver.find_element_by_css_selector("td.punchout-time div.minute ul.select-dropdown li:nth-child(41)").click()
        # Selecting p.m.
        self.driver.find_element_by_css_selector("td.punchout-time div.meridiem input.select-dropdown").click()
        time.sleep(1)
        self.driver.find_element_by_css_selector("td.punchout-time div.meridiem ul.select-dropdown li:nth-child(2)").click()
        # reason field
        self.driver.find_element_by_css_selector("input.discrepancy-reason").click()
        self.driver.find_element_by_css_selector("input.discrepancy-reason").send_keys("Automation - Adding first slot")
        # clicking on submit icon
        self.driver.find_element_by_xpath('//*[@id="table-body"]/tr[2]/td[4]/div/a[1]/i').click()
        time.sleep(5)

    def discrepancy(self):
        self.driver.find_element_by_xpath('/html/body/aside/section/ul/li[4]/a/span[1]').click()
        self.driver.find_element_by_xpath('/html/body/aside/section/ul/li[4]/ul/li[3]/a').click()
        try:
            approved_discrepancy = self.driver.find_element_by_css_selector('#leave_list_tbody tr:nth-child(1) span.discre_user_info')
            hover = ActionChains(self.driver).move_to_element(approved_discrepancy)
            hover.perform()
            self.driver.find_element_by_css_selector('#leave_list_tbody tr:nth-child(1) span.des-atten-act #approve').click()
            print("Discrepancy approved")
        except NoSuchElementException:
            # print(error.msg)
            print("Element Not Found")

    def quit(self):
        end_time = time.time()
        print("Total execution time: {}".format(end_time - start_time))
        self.driver.close()


attendancev2 = Attendancev2()
