from .base import FunctionalTest
import unittest

class ItemValidationTest(FunctionalTest):

    @unittest.skip("demonstrate skip")
    def test_cannot_add_empty_list_items(self):
        #Bob goes to the home page and accidentally tries to submit
        # an empty list item. He hits enter on the empty input box
        self.browser.get(self.server_url)
        self.browser.find_element_by_id('id_new_item').send_keys('\n')

        # The home page refreshes, and there is an error message
        # saying that list items cannot be blank
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")

        # He tries again with some text for the item, which now works
        self.browser.find_element_by_id('id_new_item').send_keys('Buy milk\n')
        self.check_for_row_in_list_table('1: Buy milk')

        # Perversely, he now decides to submit a second blank list item
        self.browser.find_element_by_id('id_new_item').send_keys('\n')

        # He receives a similar warning on the list page
        self.check_for_row_in_list_table('1: Buy milk')
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")

        # And she can correct it by filling some text in
        self.browser.find_element_by_id('id_new_item').send_keys('Make tea\n')
        self.check_for_row_in_list_table('1: Buy milk')
        self.check_for_row_in_list_table('2: Make Tea')
