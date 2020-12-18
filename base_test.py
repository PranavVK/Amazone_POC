import unittest
from appium import webdriver
from ui_workflow import UIWorkflow


class BaseTest(unittest.TestCase):
    desired_caps = {}
    ui_workflow = None

    def setUp(self):
        self.desired_caps['app'] = "/Users/pranavvarerikuniyil/Documents/Amazone_POC/Amazon_shopping.apk"
        self.desired_caps['appPackage'] = "com.amazon.mShop.android.shopping"
        self.desired_caps['appActivity'] = "com.amazon.mShop.home.HomeActivity"
        self.desired_caps['platformName'] = 'Android'
        self.desired_caps['deviceName'] = 'emulator-5554'

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", self.desired_caps)

        self.ui_workflow = UIWorkflow(self.driver)

    def tearDown(self):
        self.driver.quit()
