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

    def login(self, user_name, password):
        sign_in_button = self.common_utilities.wait_for_element(self.ui_hash_map["sign_in_button"])
        self.common_utilities.click(sign_in_button)

        email_login_textfield = self.common_utilities.wait_for_element(self.ui_hash_map["email_login_textfield"])
        self.common_utilities.type_text_in_element(email_login_textfield, user_name)

        continue_button = self.common_utilities.wait_for_element(self.ui_hash_map["continue_button"])
        self.common_utilities.click(continue_button)

        password_login_textfield = self.common_utilities.wait_for_element(self.ui_hash_map["password_login_textfield"])
        self.common_utilities.click(password_login_textfield)
        self.common_utilities.type_text_in_element(password_login_textfield, password)

        sign_in_submit_button = self.common_utilities.wait_for_element(self.ui_hash_map["sign_in_submit_button"])
        self.common_utilities.click(sign_in_submit_button)

        if self.common_utilities.is_element_present(self.ui_hash_map["add_mobile_number_label"]):
            not_now_button = self.common_utilities.wait_for_element(self.ui_hash_map["not_now_button"])
            self.common_utilities.click(not_now_button)

        self.common_utilities.wait_for_element(self.ui_hash_map["action_bar_cart"])

    def select_country_as(self, country):
        hamburger_button = self.common_utilities.wait_for_element(self.ui_hash_map["hamburger_button"])
        self.common_utilities.click(hamburger_button)

        settings_button_in_side_panel = self.common_utilities.wait_for_element(self.ui_hash_map["settings_button_in_side_panel"])
        self.common_utilities.click(settings_button_in_side_panel)

        select_country_button = self.common_utilities.wait_for_element(self.ui_hash_map["select_country_button"])
        self.common_utilities.click(select_country_button)

        country_region_selector = self.common_utilities.wait_for_element(self.ui_hash_map["country_region_selector"])
        self.common_utilities.click(country_region_selector)

        tmp_map = self.common_utilities.get_modified_copy("country_select_radio_button", "locator", "command", country)
        country_select_radio_button = self.common_utilities.wait_for_element(tmp_map)
        self.common_utilities.click(country_select_radio_button)

        done_button = self.common_utilities.wait_for_element(self.ui_hash_map["done_button"])
        self.common_utilities.click(done_button)

        self.common_utilities.wait_for_element(self.ui_hash_map["action_bar_cart"])

    def search_for_an_item(self, with_text):
        item_search_field = self.common_utilities.wait_for_element(self.ui_hash_map["item_search_field"])
        self.common_utilities.click(item_search_field)
        # full screen search option is seen once tap on search field
        item_search_field = self.common_utilities.wait_for_element(self.ui_hash_map["item_search_field"])
        self.common_utilities.type_text_in_element(item_search_field, with_text)

        tmp_map = self.common_utilities.get_modified_copy("dropdown_search_result", "locator", "command", with_text)
        dropdown_search_result = self.common_utilities.wait_for_element(tmp_map)
        self.common_utilities.click(dropdown_search_result)

    def select_product_from_search_result(self, with_name):
        tmp_map = self.common_utilities.get_modified_copy("product_title", "locator", "command", with_name)
        product_search_result = self.common_utilities.wait_for_element(tmp_map)
        self.common_utilities.click(product_search_result)


