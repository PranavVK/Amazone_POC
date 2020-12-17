import json
import os
from common_utilities import CommonUtilities


class UIWorkflow:
    driver = None
    ui_hash_map = None
    common_utilities = None

    def __init__(self, driver):
        self.driver = driver
        self.ui_hash_map = self.init_ui_hash_map()
        self.common_utilities = CommonUtilities(self.driver, self.ui_hash_map)

    def init_ui_hash_map(self):
        location = os.path.join(os.path.dirname(__file__), "ui_hash_map.json")
        with open(location) as data_file:
            data = json.load(data_file)
            return data

    def login(self):
        sign_in_button = self.common_utilities.wait_for_element(self.ui_hash_map["sign_in_button"])
        self.common_utilities.click(sign_in_button)

        email_login_textfield = self.common_utilities.wait_for_element(self.ui_hash_map["email_login_textfield"])
        self.common_utilities.type_text_in_element(email_login_textfield, "pranavtest20@gmail.com")

        continue_button = self.common_utilities.wait_for_element(self.ui_hash_map["continue_button"])
        self.common_utilities.click(continue_button)

        password_login_textfield = self.common_utilities.wait_for_element(self.ui_hash_map["password_login_textfield"])
        self.common_utilities.click(password_login_textfield)
        self.common_utilities.type_text_in_element(password_login_textfield, "Test@123")

        sign_in_submit_button = self.common_utilities.wait_for_element(self.ui_hash_map["sign_in_submit_button"])
        self.common_utilities.click(sign_in_submit_button)
