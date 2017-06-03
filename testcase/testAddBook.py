# -*- coding: UTF-8 -*-
import time
import unittest

import config
from conf import elementLocation
from lib import webDriver


class Test(unittest.TestCase):

    def setUp(self):

        self.driver = webDriver.DriverFactory().creater('FireFox').getDriver()
        self.driver.implicitly_wait(30)
        self.driver.get(config.URL)
        time.sleep(2)

    def beginAdd(self):
        driver = self.driver
        driver.find_element_by_xpath(elementLocation.BOOKMANAGER).click()

        bookTable = driver.find_element_by_xpath(elementLocation.TABLE_BOOKLIST)
        try:
            bookTable.find_element_by_xpath(elementLocation.BOOK_1000)
            book = bookTable.find_element_by_xpath(elementLocation.BOOK_1000)
            book.click()
            time.sleep(2)
            delButton = driver.find_element_by_xpath(elementLocation.BUTTON_BOOKDEL)
            delButton.click()
            time.sleep(2)
            message = driver.find_element_by_xpath(elementLocation.DIV_MESSAGE)
            isdeleted = message.find_element_by_xpath(elementLocation.BUTTON_YES)
            isdeleted.click()
            time.sleep(2)
            driver.find_element_by_xpath(elementLocation.BUTTON_OK).click()
        except Exception, e:
            pass


    def testAddBook(self):
        self.beginAdd()
        driver = self.driver
        driver.refresh()
        time.sleep(2)
        driver.find_element_by_xpath(elementLocation.BOOKMANAGER).click()

        addButton = driver.find_element_by_xpath(elementLocation.BUTTON_BOOKADD)
        addButton.click()
        time.sleep(2)

        bookInfo = driver.find_element_by_xpath(elementLocation.DIV_BOOKADD_INFO);
        bookid = bookInfo.find_element_by_xpath(elementLocation.INPUT_BOOKID)
        bookName = bookInfo.find_element_by_xpath(elementLocation.INPUT_BOOKNAME)
        bookAuthor = bookInfo.find_element_by_xpath(elementLocation.INPUT_BOOKAUTHOR)
        bookYear = bookInfo.find_element_by_xpath(elementLocation.INPUT_BOOKYEAR)
        bookdesc = bookInfo.find_element_by_xpath(elementLocation.INPUT_DESC)

        bookid.send_keys("1000")
        bookName.send_keys("test")
        bookAuthor.send_keys("test")
        bookYear.send_keys("2017")
        bookdesc.send_keys("test")

        submit = driver.find_element_by_xpath(elementLocation.BUTTON_SUBMIT)
        submit.click()
        time.sleep(2)

        message = driver.find_element_by_xpath(elementLocation.DIV_MESSAGE)
        messageValue = message.find_element_by_xpath(elementLocation.DIV_MESSAGE_VALUE)
        assert messageValue.text == u'添加书籍成功'
        driver.find_element_by_xpath(elementLocation.BUTTON_OK).click()

    def testAddSameBook(self):
        driver = self.driver
        driver.find_element_by_xpath(elementLocation.BOOKMANAGER).click()

        addButton = driver.find_element_by_xpath(elementLocation.BUTTON_BOOKADD)
        addButton.click()
        time.sleep(2)

        bookInfo = driver.find_element_by_xpath(elementLocation.DIV_BOOKADD_INFO);
        bookid = bookInfo.find_element_by_xpath(elementLocation.INPUT_BOOKID)
        bookName = bookInfo.find_element_by_xpath(elementLocation.INPUT_BOOKNAME)
        bookAuthor = bookInfo.find_element_by_xpath(elementLocation.INPUT_BOOKAUTHOR)
        bookYear = bookInfo.find_element_by_xpath(elementLocation.INPUT_BOOKYEAR)
        bookdesc = bookInfo.find_element_by_xpath(elementLocation.INPUT_DESC)

        bookid.send_keys("1000")
        bookName.send_keys("test")
        bookAuthor.send_keys("test")
        bookYear.send_keys("2017")
        bookdesc.send_keys("test")

        submit = driver.find_element_by_xpath(elementLocation.BUTTON_SUBMIT)
        submit.click()
        time.sleep(2)

        message = driver.find_element_by_xpath(elementLocation.DIV_MESSAGE)
        messageValue = message.find_element_by_xpath(elementLocation.DIV_MESSAGE_VALUE)
        assert messageValue.text == u'errorNo:1,errorInfo:该id已存在。'

    def tearDown(self):
        self.driver.close()
