import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import math
import time
 
def pytest_addoption(parser):    
    parser.addoption('--language', action='store', default='en', help="Choose languages: es, fr, ru, en, ... (etc.)") 
    parser.addoption('--browser_name', action='store', default='chrome', help="Choose browser: chrome or firefox")   

@pytest.fixture(scope="function")    
def browser(request):     
    browser_name = request.config.getoption("browser_name")    
    browser=None    
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")              
        user_language = request.config.getoption("language")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language}) 
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)       
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    time.sleep(20)
    print("\nquit browser..")
    browser.quit()



