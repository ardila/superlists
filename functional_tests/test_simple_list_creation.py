from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from .base import FunctionalTest, CHROME_PATH


class NewVisitorTest(FunctionalTest):

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Bob has heard about a cool new online to-do app. He goes to check out 
        # its homepage
        self.browser.get(self.server_url)

        
        #He notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        #He is invited to enter a to-do item straight away
        inputbox = self.get_item_input_box()
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )
         

        #He types 'Remember the milk' into a text box
        inputbox.send_keys('Remember the milk')
        
        #When he hits enter the page he is taken to a new URL, 
        #and now the page lists
        #"1: 'Remember the milk' as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)
        bob_list_url = self.browser.current_url
        self.assertRegexpMatches(bob_list_url, '/lists/.+')
        self.check_for_row_in_list_table('1: Remember the milk')



        #There is still a text box inviting her to add another item.
        #he enters "take the cannoli'
        inputbox = self.get_item_input_box()
        inputbox.send_keys('take the cannoli')
        inputbox.send_keys(Keys.ENTER)

        #The page updates again, and now shows both items on her list
        self.check_for_row_in_list_table('1: Remember the milk')
        self.check_for_row_in_list_table('2: take the cannoli')

        # Now a new user, Francis, comes along to the site.

        ## We use a new browser session to make sure that no information
        ## of bob's is coming thoguht from cookies etc #
        self.browser.quit()
        self.browser = webdriver.Chrome(CHROME_PATH)

        # Francis visits the home page. There is no sign of Bob's list
        self.browser.get(self.server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Remember the milk', page_text)
        self.assertNotIn('take the cannoli', page_text)

        #Francis starts anew list by entering a new item. He is pretty
        #Boring as well
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)

        # Francis gets his own unique URL
        francis_list_url = self.browser.current_url
        self.assertRegexpMatches(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, bob_list_url)

        # Again, there is no trace of Bob's list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Remember the milk', page_text)
        self.assertNotIn('take the cannoli', page_text)
