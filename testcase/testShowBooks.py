# -*- coding: UTF-8 -*-
import time
import unittest

import config
from conf import elementLocation
from lib import webDriver


class Test(unittest.TestCase):

    def setUp(self):
        self.driverFactory = webDriver.DriverFactory()
        self.driver = self.driverFactory.creater('FireFox').getDriver()
        self.driver.implicitly_wait(30)
        self.driver.get(config.URL)
        time.sleep(2)

    def testShowBooks(self):
        driver = self.driver
        driver.find_element_by_xpath(elementLocation.BOOKMANAGER).click()
        time.sleep(2)
        driver.find_element_by_xpath(elementLocation.BUTTON_BOOKADD)


    def tearDown(self):
        self.driver.close()
