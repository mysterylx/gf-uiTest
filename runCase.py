# -*- coding: UTF-8 -*-
import unittest

from lib import HTMLTestRunner
from testcase import *

#用例文件列表
def getCaselist():
    allTestNames = [
        testShowBooks.Test,
        testAddBook.Test,
        testUpdateBook.Test,
        testDelBook.Test
        ]
    print('success read case list!')
    return allTestNames



if __name__ == '__main__':
    testunit = unittest.TestSuite()
    caseList = getCaselist()
    for case in caseList:
        testunit.addTest(unittest.makeSuite(case))
    runner = unittest.TextTestRunner()
    fp = open('./result.html', 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='webTestReport', description='webTestReport')
    runner.run(testunit)
    fp.close()
