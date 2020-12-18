import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CommonUtilities:
    def __init__(self, driver, ui_hash_map):
        self.driver = driver
        self.ui_hash_map = ui_hash_map

    def wait_for_element(self, element_hash_map, retries=10):
        """
        To wait for the visibility of element and locate.
        :param element_hash_map:
        :param retries:
        :return:
        """
        for i in range(retries):
            try:
                element = self.find_element(element_hash_map)
                break
            except Exception as element_found_exception:
                if i + 1 == retries:
                    raise element_found_exception
        return element

    def find_element(self, element_hash_map):
        """
        To locate element using differnt types of locators like xpath, id, class name, etc
        :param element_hash_map:
        :return:
        """
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
        elif 'xpath' in element_hash_map:
            WebDriverWait(self.driver, element_timeout).until(
                EC.presence_of_element_located(By.XPATH, element_hash_map['xpath']))
        else:
            raise Exception("Invalid locator")
        time.sleep(default_implicit_wait)
        return element

    def click(self, element):
        """
        To click on element
        :param element:
        :return:
        """
        element.click()

    def type_text_in_element(self, element, text):
        """
        To type text to elements
        :param element:
        :param text:
        :return:
        """
        element.send_keys(text)

    def is_element_present(self, element_hash_map):
        """
        To check element is present
        :param element_hash_map:
        :return:
        """
        element = None
        try:
            element = self.find_element(element_hash_map)
        except:
            pass
        if element is None:
            return False
        return True

    def get_modified_copy(self, selector, member_name, member_text, replacement_text):
        """
        To make a copy of dict and update with parameters
        :param selector:
        :param member_name:
        :param member_text:
        :param replacement_text:
        :return:
        """
        map_copy = dict(self.ui_hash_map[selector])
        map_copy[member_name] = map_copy[member_name].replace(member_text, replacement_text)
        return map_copy

    def perform_tap(self):
        """
        To tap on center of the screen
        :return:
        """
        window_rect = self.driver.get_window_size()
        x = int(window_rect["width"]) / 2
        y = int(window_rect["height"]) / 2
        self.driver.tap(x, y)

    def get_text_of_element(self, element):
        """
        To fetch text from element
        :param element:
        :return:
        """
        return element.get_attribute("name")

    def swipe(self, swipe_up):
        """
        To swipe up/down
            which: Element ui_hash_map.
            swipe_up: True = Swipe up/ False = Swipe down
        """
        window_rect = self.driver.get_window_size()

        width = int(window_rect["width"])
        height = int(window_rect["height"])

        start_y = height * 0.80
        end_y = height * 0.50

        start_x = width / 2

        if swipe_up:
            self.driver.swipe(start_x, start_y, start_x, end_y, 500)
        else:
            self.driver.swipe(start_x, end_y, start_x, start_y, 500)
