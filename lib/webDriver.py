# -*- coding: UTF-8 -*-
from selenium import webdriver

import config


class DriverFactory():
    def __init__(self):
        pass

    def creater(self,type):
        if type == 'FireFox':
            driver = FireFoxWebDriver()
        else:
            driver = None
        return driver

class Driver():
    def __init__(self):
        self.driver = None


class FireFoxWebDriver(Driver):
    def __init__(self):
        self.driver = webdriver.Firefox(executable_path=config.GECKODRIVER)

    def getDriver(self):
        return self.driver

'''后续可添加chrome driver'''