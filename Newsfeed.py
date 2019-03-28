from selenium import webdriver
import time
from Login import MainLogin


class Newsfeed(MainLogin):
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\chromedriver\chromedriver.exe")
        self.login()
        self.run()
        self.stop()

    def run(self):
        image_button = '//*[@id="pagelet_composer"]/div[3]/ul/li[1]/div/a/i'
        post_text_field = '//html/body/main/div/section/div/form/div[1]/div[1]/div[2]/div[2]/div'
        self.driver.find_element_by_xpath(image_button).click()
        self.driver.find_element_by_id('media').send_keys("C:\\Users\Gaditek\PycharmProjects\Life\sample.JPG")
        self.driver.find_element_by_xpath('//*[@id="myModal"]/div/div/div[1]/div[3]/button').click()
        time.sleep(30)
        self.driver.find_element_by_xpath(post_text_field).click()
        time.sleep(30)
        self.driver.find_element_by_xpath(post_text_field).send_keys("Sample Image upload test - Automation ")
        self.driver.find_element_by_id('submitPost').click()


newsfeed = Newsfeed()

