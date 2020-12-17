import json
import os
from common_utilities import CommonUtilities


class UIWorkflow:
    driver = None
    ui_hash_map = None

    def __init__(self, driver):
        self.driver = driver
        self.ui_hash_map = self.init_ui_hash_map()
        self.CommonUtilities = CommonUtilities(self.driver, self.ui_hash_map)

    def init_ui_hash_map(self):
        location = os.path.join(os.path.dirname(__file__), "ui_hash_map.json")
        with open(location) as data_file:
            data = json.load(data_file)
            return data

    def login(self):
        sign_in_button = self.CommonUtilities.wait_for_element(self.ui_hash_map["sign_in_button"])
        self.CommonUtilities.click(sign_in_button)
