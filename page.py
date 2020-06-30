

from element import BasePageElement
from locators import MainPageLocators
from locators import LoginPageLocators

class SearchTextElement(BasePageElement):
    """This class gets the search text from the specified locator"""

    #The locator for search box where search string is entered
    locator = 'q'


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    """Home page action methods come here. """

    #Declares a variable that will contain the retrieved text
    search_text_element = SearchTextElement()

    def is_title_matches(self):
        """Verifies that the text "Dexcom" appears in page title"""
        return "Dexcom" in self.driver.title

    def click_go_button(self):
        """Triggers the search"""
        element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
        element.click()

    def click_home_button(self):
        element = self.driver.find_element(*MainPageLocators.HOME_BUTTON)
        print(element)
        element.click()

         

   



class LoginPage(BasePage):
    """Login page action methods come here. """

    def enter_username(self,config_username):
        element = self.driver.find_element(*LoginPageLocators.USERNAME)
        print("Username:", element)
        element.send_keys(config_username)


    def enter_password(self,config_password):
        element = self.driver.find_element(*LoginPageLocators.PASSWORD)
        print("Password",element)
        element.send_keys(config_password)

    def click_submit(self):
        element = self.driver.find_element(*LoginPageLocators.SUBMIT)
        print("Submit:",element)
        element.click()




class SearchResultsPage(BasePage):
    """Search results page action methods come here"""

    def is_results_found(self):
        # Probably should search for this text in the specific page
        # element, but as for now it works fine
        return "No results found." not in self.driver.page_source