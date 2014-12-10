from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
        
        def setUp(self):
            self.browser = webdriver.Chrome('/Users/ardila/src/tdd_tutorial/chromedriver')
            self.browser.implicitly_wait(3)
        
        def tearDown(self):
            self.browser.quit()

        def test_can_start_a_list_and_retrieve_it_later(self):
            # Bob has heard about a cool new online to-do app. He goes to check out 
            # its homepage
            self.browser.get('http://localhost:8000')

            
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

            #When he hits enter the page updates and now the page lists
            #"1: 'Remember the milk' as an item in a to-do list
            inputbox.send_keys('Buy peacock feathers')

            table = self.browser.find_element_by_id('id_list_table')
            rows = table.find_elements_by_tag_name('tr')
            self.assertTrue(
                any(row.text == '1: Buy peacock feathers' for row in rows),
                "New to-do item did not appear in table"
            )
            #There is still a text box inviting her to add another item.
            #he enters "take the cannoli'
            self.fail('Finish the test!')

            #The page updates again, and now shows both items on her list

            #Bob wonders whether the site will remember her list. Then he sees
            #That the site has generated a unique URL for her -- there is some
            #Explanatory text to that effect.

            #He visits that URL - his todo list is still there

            #Satisfied, he goes back to sleep

if __name__ == '__main__':
    unittest.main()
