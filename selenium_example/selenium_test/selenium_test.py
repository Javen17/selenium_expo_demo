from selenium_example.taskmaster.taskmaster import TaskMaster
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pathlib as pl

class TestSelenium(unittest.TestCase):

    def setUp(self):
        self.taskmaster = TaskMaster()

    def assertIsFile(self, path):
        if not pl.Path(path).resolve().is_file():
            raise AssertionError("File does not exist: %s" % str(path))

    #def test_search_google(self):
    #    self.taskmaster.search_bing('flutter')
    #    self.assertIn('https://www.google.com/search?q=flutter', self.taskmaster.driver_handler.driver.current_url ) 

    def test_big_yoshi_file(self):
        self.taskmaster.get_big_yoshi()
        self.assertIsFile('C:\\Users\\javie\\Desktop\\experiments\\Selenium\\big_yoshi.jpeg')

    def tearDown(self):
        self.taskmaster.driver_handler.close_driver_instance()

