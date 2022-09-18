from .base_page import BasePage
from .locators import BasketPageLocators
from .locators import BasePageLocators

class BasketPage(BasePage):
    def should_be_empty_message(self):                
        assert self.browser.find_element(*BasketPageLocators.MESSAGE_BASKET), "text empty basket is not presented"
        assert True 
    def should_not_be_product_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_PRODUCT), \
           "Product in basket is presented, but should not be"     
    def should_be_text_empty_message(self):                
        assert self.browser.find_element(*BasketPageLocators.MESSAGE_BASKET).text == "Your basket is empty. Continue shopping", "text empty basket is not good"
        assert True     