from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from selenium.webdriver.common.by import By
import pytest
from pages.login_page import LoginPage

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
    page = MainPage(browser, link)
    page.open()        
    page.go_to_button_add()
    button_add = ProductPage(browser, browser.current_url)
    button_add.should_be_button_add()
    
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser): 
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = MainPage(browser, link)
    page.open()               
    page.go_to_button_add()
    button_add = ProductPage(browser, browser.current_url)
    button_add.should_be_button_add()
    success_page = ProductPage(browser, browser.current_url)
    success_page.should_not_be_success_message()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser): 
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    success_page = ProductPage(browser,link)
    success_page.open()
    success_page.should_not_be_success_message()
    #page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"               
    page = MainPage(browser, link)
    page.open()               
    page.go_to_button_add()
    success_page = ProductPage(browser, browser.current_url) 
    success_page.success_message_should_disappear()
    page.success_message_should_disappear()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/"
    page = BasketPage(browser, link)
    page.open()  
    page.go_to_basket_page()
    page.should_not_be_product_basket()
    page.should_be_text_empty_message()
    

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/studyguide-for-counter-hack-reloaded_205/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.should_not_be_product_basket()
    page.should_be_text_empty_message() 

class TestUserAddToBasketFromProductPage(): 
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user()
        page.should_be_authorized_user()          
    def test_user_cant_see_success_message(self, browser): 
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        success_page = ProductPage(browser, link)
        success_page.open()
        success_page.should_not_be_success_message()
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
        page = MainPage(browser, link)
        page.open()        
        page.go_to_button_add()
        button_add = ProductPage(browser, browser.current_url)
        button_add.should_be_button_add()
    
     