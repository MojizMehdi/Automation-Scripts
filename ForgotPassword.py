import unittest
from selenium import webdriver


class Forgotpassword(unittest.TestCase):
    def test_TC_2_Forgot_password(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://devlife.gaditek-hrms.sg.plesk-server.com/")
        self.driver.find_element_by_xpath('/html/body/section/div/div/div/form/a').click()
        self.driver.find_element_by_xpath("//*[@id='email']").send_keys("zahid.friend123@gmail.com")
        self.driver.find_element_by_xpath('//*[@id="emp_login"]').click()
        sucess_message = self.driver.find_element_by_xpath('/html/body/section/div/div/div/div/div/div').text
        print(sucess_message)


if __name__ == '__main__':
    unittest.main(failfast=True, exit=False)
