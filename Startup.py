from selenium import webdriver
from Login import MainLogin


class Example(MainLogin):
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\chromedriver\chromedriver.exe")
        self.login()
        self.run()

    def run(self):
        # code here
        print('Run')

    def stop(self):
        print("stop")

    def __del__(self):
        self.driver.quit()
        print('Finish')


example = Example()
