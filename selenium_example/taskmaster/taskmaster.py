from selenium_example.taskmaster.models import MoveCarouselResult
from selenium.webdriver.common.keys import Keys
from selenium_example.webdriver.webdriver import WebDriverHandler
from selenium import webdriver 
import time 

class TaskMaster:
    driver_handler = WebDriverHandler()

    def get_site_page(self, query):
        self.driver_handler.driver.get(query)
    
    def get_carousel_len(self):
        time.sleep(10)
        carousel_items = self.driver_handler.driver.find_elements_by_class_name('carousel-item')
        return len(carousel_items)

    def move_carousel(self):
        results = MoveCarouselResult()

        carousel_items = self.driver_handler.driver.find_elements_by_class_name('carousel-item')
        results.initial_active_position = self.get_carousel_active_index(carousel_items)
        next_arrow = self.driver_handler.driver.find_element_by_xpath('//*[@id="carouselExampleControls"]/a[2]/span[1]')
        next_arrow.click()
        time.sleep(5)
        results.last_active_position = self.get_carousel_active_index(carousel_items)

        return results

    def get_carousel_active_index(self, carousel_items):

        position = 0

        for item in carousel_items:
            class_list = item.get_attribute('class')
            for class_name in class_list.split(' '):
                if class_name == 'active':
                    return position
            position += 1
        
        return None
    
    def click_detail_link(self):
        game_link = self.driver_handler.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/div[1]/a')
        game_link.click()
        time.sleep(5)
        
