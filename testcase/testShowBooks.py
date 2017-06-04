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
        bookList = driver.find_element_by_xpath(elementLocation.TABLE_BOOKLIST)
        books = bookList.find_elements_by_tag_name('tr')
        assert len(books) >= 0

    def tearDown(self):
        self.driver.close()
