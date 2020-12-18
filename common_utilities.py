import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CommonUtilities:
    def __init__(self, driver, ui_hash_map):
        self.driver = driver
        self.ui_hash_map = ui_hash_map

    def wait_for_element(self, element_hash_map, retries=5):
        for i in range(retries):
            try:
                element = self.find_element(element_hash_map)
                break
            except Exception as element_found_exception:
                if i + 1 == retries:
                    raise element_found_exception
        return element

    def find_element(self, element_hash_map):
        default_implicit_wait = 2
        element_timeout = 10
        if 'locator' in element_hash_map:
            cmd = element_hash_map['locator']
            element = self.driver.find_element_by_android_uiautomator(cmd)
        elif 'class_name' in element_hash_map:
            element = WebDriverWait(self.driver, element_timeout).until(
                EC.presence_of_element_located((By.CLASS_NAME, element_hash_map["class_name"]))
            )
        elif 'resource_id' in element_hash_map:
            element = WebDriverWait(self.driver, element_timeout).until(
                EC.presence_of_element_located((By.ID, element_hash_map["resource_id"]))
            )
        else:
            raise Exception("Invalid locator")
        time.sleep(default_implicit_wait)
        return element

    def click(self, element):
        element.click()

    def type_text_in_element(self, element, text):
        element.send_keys(text)

    def is_element_present(self, element_hash_map):
        element = None
        try:
            element = self.find_element(element_hash_map)
        except:
            pass
        if element is None:
            return False
        return True

    def get_modified_copy(self, selector, member_name, member_text, replacement_text):
        map_copy = dict(self.ui_hash_map[selector])
        map_copy[member_name] = map_copy[member_name].replace(member_text, replacement_text)
        return map_copy

    def perform_tap(self):
        size = self.driver.get_window_size()
        x = size[0] / 2
        y = size[1] / 2
        self.driver.tap(x, y)