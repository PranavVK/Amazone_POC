from base_test import BaseTest


class PuchaseItem(BaseTest):
    def testPurchaseItem(self):
        """
        1. Launch and login to application
        2. Set country as India
        3. Clear cart if any items present
        4. Search for an item
        5. Select the search item and store brand name, description and price
        6. Add item to cart
        7. Validate brand name, description and price in cart screen
        8. Clean up

        """
        self.ui_workflow.login("pranavtest20@gmail.com", "Test@123")
        self.ui_workflow.select_country_as("India Amazon.in")
        self.ui_workflow.clear_cart_if_items_present()
        self.ui_workflow.search_for_an_item("65 inch tv")
        self.ui_workflow.select_product_from_search_result("Vu 164 cm (65 inches) 4K Ultra HD Smart Android LED TV")
