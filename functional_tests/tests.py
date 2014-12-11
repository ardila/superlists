from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


CHROME_PATH = '/Users/ardila/src/tdd_tutorial/chromedriver'
print super(LiveServerTestCase)

class NewVisitorTest(LiveServerTestCase):
        
        def setUp(self):
            self.browser = webdriver.Chrome(CHROME_PATH)
            self.browser.implicitly_wait(3)
        
        def tearDown(self):
            self.browser.quit()

        def check_for_row_in_list_table(self, row_text):
            table = self.browser.find_element_by_id('id_list_table')
            rows = table.find_elements_by_tag_name('tr')
            self.assertIn(row_text, [row.text for row in rows])

        def test_layout_and_styling(self):
            # Edith goes to the home page
            self.browser.get(self.live_server_url)
            self.browser.set_window_size(1024, 768)

            inputbox = self.browser.find_element_by_id('id_new_item')
            self.assertAlmostEqual(
                inputbox.location['x'] + inputbox.size['width'] / 2,
                512,
                delta=5
            )
            
            inputbox.send_keys('testing\n')
            inputbox = self.browser.find_element_by_id('id_new_item')
            self.assertAlmostEqual(
                inputbox.location['x'] + inputbox.size['width'] / 2,
                512,
                delta=5
            )

        def test_can_start_a_list_and_retrieve_it_later(self):
            # Bob has heard about a cool new online to-do app. He goes to check out 
            # its homepage
            self.browser.get(self.live_server_url)

            
            #He notices the page title and header mention to-do lists
            self.assertIn('To-Do', self.browser.title)
            header_text = self.browser.find_element_by_tag_name('h1').text
            self.assertIn('To-Do', header_text)

            #He is invited to enter a to-do item straight away
            inputbox = self.browser.find_element_by_id('id_new_item')
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
            inputbox = self.browser.find_element_by_id('id_new_item')
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
            self.browser.get(self.live_server_url)
            page_text = self.browser.find_element_by_tag_name('body').text
            self.assertNotIn('Remember the milk', page_text)
            self.assertNotIn('take the cannoli', page_text)

            #Francis starts anew list by entering a new item. He is pretty
            #Boring as well
            inputbox = self.browser.find_element_by_id('id_new_item')
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


            #Satisfied, they both go back to sleep
