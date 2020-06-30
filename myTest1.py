import time
import unittest
import configparser
from selenium import webdriver


import locators
import element
import page


#
# Read in config options for URL, Username, Password
#
config = configparser.RawConfigParser()
config.read('myTest1.conf')

config_url       = config.get('options', 'url')
config_username  = config.get('options', 'username')
config_password  = config.get('options', 'password')

print(config.sections())
print("Config option URL: ",config_url)
print("Config option Username: ",config_username)
print("Config option Password: ",config_password)



class PythonOrgSearch(unittest.TestCase):
    """Use the Page object class and unittest framework to verify login to Clarity home page."""

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(config_url)

    def test_search_in_python_org(self):
        """
        Tests the ability to login to Dexcom Home page from https://clarity.dexcom.com
        """
        print("Title:  ", self.driver.title)

        # Define the main page and login page from Dexcom.com.
        main_page  = page.MainPage(self.driver)
        login_page  = page.LoginPage(self.driver)
        
        time.sleep(1)
        # Checks if the word "Dexcom" is in title
        assert main_page.is_title_matches(), "Dexcom title doesn't match."
        
        # Choos the button to login to Home page
        main_page.click_home_button()

        time.sleep(1)

        # Enter the provided Username and Password
        login_page.enter_username(config_username)
        login_page.enter_password(config_password)
        login_page.click_submit()
        
        time.sleep(1) 

        
        #Verifies that the results page is not empty
        search_results_page = page.SearchResultsPage(self.driver)
        assert search_results_page.is_results_found(), "No results found."

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()


