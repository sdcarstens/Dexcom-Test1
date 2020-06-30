
from selenium.webdriver.common.by import By

class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""
    GO_BUTTON = (By.ID, 'submit')
    HOME_BUTTON = (By.CLASS_NAME, 'btn-primary')
   

class LoginPageLocators(object):
    """A class for login page locators. All login page locators should come here"""
    USERNAME = (By.ID, 'username')
    PASSWORD = (By.ID, 'password')
    SUBMIT =   (By.NAME, 'op')
                   

class SearchResultsPageLocators(object):
    """A class for search results locators. All search results locators should come here"""
    pass



