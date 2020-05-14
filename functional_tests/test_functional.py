from selenium import webdriver
import unittest, time, os
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase
class FunctionalTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        staging_server = os.environ.get('STAGING_SERVER')  
        if staging_server:            
            self.live_server_url = 'http://' + staging_server
        self.browser.get(self.live_server_url)
        # self.browser.get('http://localhost:8000')
    
    def tearDown(self):
        self.browser.quit()
    
    def test_new_sigle_user_visit_site(self):
        inputbox = self.browser.find_element_by_id('id_new_item')
        placeholder = inputbox.get_attribute('placeholder')
        self.assertEqual(placeholder, 'Enter new item')

        inputbox.send_keys('Get chicken')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(2)

        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Get Masala')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(2)

        ul = self.browser.find_element_by_id('id_list_table')
        li = ul.find_elements_by_tag_name('li')

        self.assertIn('Get chicken', [row.text for row in li])
        self.assertIn('Get Masala', [row.text for row in li])
        # self.assertRegex(self.browser.current_url, '/lists/.+')

    def test_multiple_user_can_start_list(self):
        pass

    # def test_title_correct(self):
    #     self.assertEqual(self.browser.title, 'Notes') 
        
    #     header = self.browser.find_element_by_tag_name('h1').text
    #     self.assertEqual(header, 'My Notes')

    #     self.fail('Finished Test!')

   


# if __name__ == '__main__':
#     unittest.main()