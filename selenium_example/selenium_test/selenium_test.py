from os import system
from flask_test_site.models.mock_db import MockDb
from selenium_example.taskmaster.taskmaster import TaskMaster
import unittest
from selenium.webdriver.common.keys import Keys

class TestSelenium(unittest.TestCase):
    taskmaster = TaskMaster()

    def setUp(self):
        self.taskmaster.get_site_page('http://127.0.0.1:5000/')

    def test_main_page_exist(self):
        self.assertIn('http://127.0.0.1:5000/', self.taskmaster.driver_handler.driver.current_url)
    
    def test_carousel_movement(self):
        results = self.taskmaster.move_carousel()
        self.assertNotEqual(results.initial_active_position, results.last_active_position)

    def test_carousel_elements(self):
       #here we simulate database access, with this we can assert the query results get painted on the page
       db =  MockDb().db
       self.assertEqual(len(db["games"]), self.taskmaster.get_carousel_len())

    def test_detail_link(self): 
        self.taskmaster.click_detail_link()
        self.assertIn('http://127.0.0.1:5000/detail/0', self.taskmaster.driver_handler.driver.current_url)


