import logging
import json
import os


class CommonUtilities:
    def __init__(self, driver, ui_hash_map):
        self.driver = driver
        self.ui_hash_map = ui_hash_map

    def find_elements(self, element_hash_map):
        return self.driver.find_element_by_id(element_hash_map["resource_id"])

    def click(self, element):
        element.click()

