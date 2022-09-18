from .base_page import BasePage
from .locators import MainPageLocators
from .locators import PriseNameLocators
from .product_page import ProductPage
from .locators import BasketPageLocators
from selenium.webdriver.common.by import By

class MainPage(BasePage):     
    def price_name_do(self):
        price_name = self.browser.find_element(*PriseNameLocators.Price1)        
        price_name = self.browser.find_element(*PriseNameLocators.Name1)       
    def go_to_button_add(self):
        login_link = self.browser.find_element(*MainPageLocators.Button_Link)
        login_link.click()
        #link = self.browser.find_element(*MainPageLocators.Button_Link)
        #link.click()   
    def price_name_posle(self):
        price_name = self.browser.find_element(*PriseNameLocators.Price2)        
        price_name = self.browser.find_element(*PriseNameLocators.Name2)       
    def should_be_button_add(self):
        assert self.is_element_present(*MainPageLocators.Button_Link), "button_add is not presented"
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
