from selenium.webdriver.common.keys import Keys
import urllib.request
from selenium_example.webdriver.webdriver import WebDriverHandler
from selenium import webdriver 
import time 

class TaskMaster:
    driver_handler = WebDriverHandler()

    def search_bing(self, query):
        self.driver_handler.create_driver_instance()
        self.driver_handler.driver.get(f'https://www.bing.com/search?q={query}')

    
    def get_big_yoshi(self):
        self.search_bing('big+yoshi')
        google_options_row  = self.driver_handler.driver.find_element_by_xpath('//*[@id="b-scopeListItem-images"]/a')
       #image_link =  google_options_row.find_element_by_xpath('//*[@id="b-scopeListItem-images"]/a')
        google_options_row.click()

        time.sleep(5)

        img =  self.driver_handler.driver.find_element_by_xpath('//*[@id="mmComponent_images_2"]/ul[1]/li[1]/div/div[1]/a/div')
        img.click()
       
        action = webdriver.ActionChains(self.driver_handler.driver)
       
        action.move_to_element(img)
        action.perform()
        time.sleep(5)

        #img = self.driver_handler.driver.find_element_by_xpath('//*[@id="mainImageWindow"]/div[1]/div/div/div/img')

        #src = img.get_attribute('src')
        #urllib.request.urlretrieve(src, "big_yoshi.jpeg")

    def simulate_user_input(self, query):
        search_bar = self.driver_handler.driver.find_element_by_name("q")
        search_bar.clear()
        search_bar.send_keys(query)
        search_bar.send_keys(Keys.RETURN)
        
      

