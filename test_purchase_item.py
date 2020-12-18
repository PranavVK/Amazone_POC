from base_test import BaseTest


class PuchaseItem(BaseTest):
    def testFirstAutomationTest(self):
        self.ui_workflow.login("pranavtest20@gmail.com", "Test@123")
        self.ui_workflow.select_country_as("India Amazon.in")
        self.ui_workflow.search_for_an_item("65 inch tv")
        self.ui_workflow.select_product_from_search_result("Vu 164 cm (65 inches) 4K Ultra HD Smart Android LED TV")
