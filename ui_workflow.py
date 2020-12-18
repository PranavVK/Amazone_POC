import json
import os
import time
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

        password_login_textfield = self.common_utilities.wait_for_element(self.ui_hash_map["password_login_textfield"],
                                                                          20)
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

        retry_count = 0
        while not self.common_utilities.is_element_present(self.ui_hash_map["settings_button_in_side_panel"]) and retry_count < 5:
            self.common_utilities.swipe(True)
            time.sleep(2)  # Waiting for loading refreshed contents
            retry_count += 1
        settings_button_in_side_panel = self.common_utilities.wait_for_element(
            self.ui_hash_map["settings_button_in_side_panel"])
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

    def clear_cart_if_items_present(self):
        action_bar_cart = self.common_utilities.wait_for_element(self.ui_hash_map["action_bar_cart"])
        self.common_utilities.click(action_bar_cart)

        while self.common_utilities.is_element_present(self.ui_hash_map["delete_button"]):
            delete_button = self.common_utilities.wait_for_element(self.ui_hash_map["delete_button"])
            self.common_utilities.click(delete_button)

        hamburger_button = self.common_utilities.wait_for_element(self.ui_hash_map["hamburger_button"])
        self.common_utilities.click(hamburger_button)

        home_button_in_side_panel = self.common_utilities.wait_for_element(
            self.ui_hash_map["home_button_in_side_panel"])
        self.common_utilities.click(home_button_in_side_panel)

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

        if self.common_utilities.is_element_present(self.ui_hash_map["enter_pin_code_button"]):
            self.common_utilities.perform_tap()

        product_brand_name = self.common_utilities.wait_for_element(self.ui_hash_map["product_brand_name"])
        product_brand_name_value = self.common_utilities.get_text_of_element(product_brand_name)

        product_description_map = self.common_utilities.get_modified_copy("product_description", "locator", "command",
                                                                          with_name)
        product_description = self.common_utilities.wait_for_element(product_description_map)
        product_description_value = self.common_utilities.get_text_of_element(product_description)

        product_price = self.common_utilities.wait_for_element(self.ui_hash_map["product_price"])
        product_price_value = self.common_utilities.get_text_of_element(product_price)
