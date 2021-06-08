from selenium import webdriver 

class WebDriverHandler:
    driver_location = r"C:\/Users\/javie\/Desktop\/experiments\/Selenium\/selenium_example\/webdriver\/chromedriver.exe"
    driver = None

    def create_driver_instance(self):
        self.driver = webdriver.Chrome(executable_path= self.driver_location)
        return self.driver
    
    def close_driver_instance(self):
        if(self.driver != None):
            self.driver.close()

    def get_current_location(self):
         if(self.driver != None):
            return self.driver.current_url
         else:
            return None

    