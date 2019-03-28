import unittest


class MainLogin(unittest.TestCase):
    def login(self, url):
        if url:
            self.driver.get(url)
        else:
            self.driver.get("https://devlife.gaditek-hrms.sg.plesk-server.com/")
        self.driver.find_element_by_xpath("//*[@id='employee_id']").send_keys("mojiz.mehdi@gaditek.com")
        self.driver.find_element_by_xpath("//*[@id='password']").send_keys("mojizmehdi1")
        self.driver.find_element_by_xpath("//*[@id='emp_login']").click()

    def logout(self):
        self.driver.find_element_by_xpath('//*[@id="my-other-element"]/ul/li[4]/a/img').click()
        self.driver.find_element_by_xpath('//*[@id="my-other-element"]/ul/li[4]/ul/li[3]/a').click()

    def login_admin(self):
        self.driver.find_element_by_xpath("//*[@id='employee_id']").send_keys("mojiz.gaditek@gmail.com")
        self.driver.find_element_by_xpath("//*[@id='password']").send_keys("mojizmehdi1")
        self.driver.find_element_by_xpath("//*[@id='emp_login']").click()

# if __name__ == '__main__':
#     unittest.main(failfast=True, exit=False)
