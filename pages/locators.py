from selenium.webdriver.common.by import By

class MainPageLocators():
    Button_Link = (By.CLASS_NAME, "btn-add-to-basket")  
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
  

class PriseNameLocators():
    Price1 = (By.CSS_SELECTOR, "div.col-sm-6.product_main>p.price_color")
    Price2 = (By.CSS_SELECTOR, ".alertinner>p>strong")
    Name1 = (By.CSS_SELECTOR, "div.col-sm-6.product_main>h1")
    Name2 = (By.CSS_SELECTOR, "#messages > div:nth-child(1)>.alertinner>strong")

class ProductPageLocators():    
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alertinner>p>strong")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "span >a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    MESSAGE_BASKET = (By.CSS_SELECTOR, "#content_inner>p")
    BASKET_PRODUCT = (By.CSS_SELECTOR, "div.basket-title.hidden-xs")

class RegistreUser():
    EMAIL = (By.ID, "id_registration-email")
    PASSWORD = (By.ID, "id_registration-password1")
    CONFIRM_PASSWORD = (By.ID, "id_registration-password2")
    BUTTON_REGISTRE = (By.NAME , "registration_submit")    

class LoginPageLocators():
    Vhod = (By.CSS_SELECTOR, "#login_form")
    Reg = (By.CSS_SELECTOR, "#register_form")