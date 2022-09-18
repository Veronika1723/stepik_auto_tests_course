from .base_page import BasePage
from .locators import RegistreUser
from random_word import RandomWords
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):        
        assert "login" in self.url, "link is not login"  
        assert True

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.Vhod), "have not vhod"
        assert True

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.Reg), "have not reg"
        assert True

    def register_new_user(self):
        r = RandomWords()
        self.email = r.get_random_word() + "@fakemail.org"
        self.password = r.get_random_word() + "123"
        a = self.password
        email = self.browser.find_element(*RegistreUser.EMAIL).send_keys(self.email)
        print(self.email)
        print(a)
        password = self.browser.find_element(*RegistreUser.PASSWORD).send_keys(self.password)
        password_two = self.browser.find_element(*RegistreUser.CONFIRM_PASSWORD).send_keys(a)
        button_registre = self.browser.find_element(*RegistreUser.BUTTON_REGISTRE)
        button_registre.click()