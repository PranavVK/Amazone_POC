import unittest
import logging
import json
import os
from appium import webdriver
from CommonUtilities import CommonUtilities


class BaseTest(unittest.TestCase):
    desired_caps = {}
    driver = None
    ui_hash_map = None

    def setUp(self):
        self.desired_caps['app'] = "/Users/pranavvarerikuniyil/Documents/Amazone_POC/Amazon_shopping.apk"
        self.desired_caps['appPackage'] = "com.amazon.mShop.android.shopping"
        self.desired_caps['appActivity'] = "com.amazon.mShop.home.HomeActivity"
        self.desired_caps['platformName'] = 'Android'
        self.desired_caps['deviceName'] = 'emulator-5554'

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", self.desired_caps)

        self.ui_hash_map = self.init_ui_hash_map()
        self.CommonUtilities = CommonUtilities(self.driver, self.ui_hash_map)

    def testFirstAutomationTest(self):
        sign_in_button = self.CommonUtilities.find_elements(self.ui_hash_map["sign_in_button"])
        self.CommonUtilities.click(sign_in_button)

    def init_ui_hash_map(self):
        location = os.path.join(os.path.dirname(__file__), "UiHashMap.json")
        with open(location) as data_file:
            data = json.load(data_file)
            return data

    def tearDown(self):
        self.driver.quit()
