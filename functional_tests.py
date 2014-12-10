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

            
            #He notices the page titela and header mention to-do lists
            self.assertIn('To-Do', self.browser.title)
            self.fail('Finish the test!')

            #He is invited to enter a to-do item straight away

            #He types 'forget the milk' into a text box

            #When he hits enter the page updates and now the page lists
            #"1: 'forget the milk' as an item in a to-do list

            #There is still a text box inviting her to add another item.
            #he enters "take the cannoli'

            #The page updates again, and now shows both items on her list

            #Bob wonders whether the site will remember her list. Then he sees
            #That the site has generated a unique URL for her -- there is some
            #Explanatory text to that effect.

            #He visits that URL - his todo list is still there

            #Satisfied, he goes back to sleep
if __name__ == '__main__':
    unittest.main(warnings='ignore')


