#!/usr/bin/env python
#-*- coding:utf-8  -*-
#base on Python2.7 PhantomJS

import os
import sys
import time
import unittest

from selenium import webdriver

class TestAso(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.PhantomJS()

	def test_url(self):
		self.driver.get("https://aso100.com/search?country=cn&search=qq")
		self.driver.save_screenshot('screen.png')

	def tearDown(self):
		self.driver.quit()

if __name__ == '__main__':
	unittest.main()