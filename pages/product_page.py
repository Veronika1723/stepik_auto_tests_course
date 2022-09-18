from selenium.common.exceptions import NoAlertPresentException
from .base_page import BasePage
from .locators import PriseNameLocators
from .locators import MainPageLocators
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import ProductPageLocators
from .locators import BasketPageLocators
import time
import math

class ProductPage(BasePage):
    def should_be_button_add(self):        
        self.should_be_button_add()        
        #solve_quiz_and_get_code(self)
        self.should_be_price()
        self.should_be_name()
        self.should_not_be_success_message()
        self.success_message_should_disappear()
    def should_be_button_add(self):
        assert self.is_element_present(*MainPageLocators.Button_Link), "have not button"
        assert True
    def should_be_price(self):
        product_price = self.browser.find_element(*PriseNameLocators.Price1).text
        basket_price = self.browser.find_element(*PriseNameLocators.Price2).text
        assert product_price == basket_price, "price fail"      
    def should_be_name(self):
        product_name = self.browser.find_element(*PriseNameLocators.Name1).text
        basket_name = self.browser.find_element(*PriseNameLocators.Name2).text
        assert product_name == basket_name, "name failed"
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Success message is presented, but should not be"    
    def success_message_should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Success message is presented, but not disappear"  
    def should_be_empty_message(self):                
        assert self.browser.find_element(*BasketPageLocators.MESSAGE_BASKET), "text empty basket is not presented"
        assert True 
    def should_not_be_product_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_PRODUCT), \
           "Product in basket is presented, but should not be"        