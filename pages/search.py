"""
This module contains DuckDuckGoSearchPage,
the page object for the DuckDuckGo search page
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class DuckDuckGoSearchPage:
    URL = "https://duckduckgo.com"
    SEARCH_INPUT = (By.ID, "search_form_input_homepage")
    SEARCH_BUTTON = (By.ID, "search_button_homepage")
    AUTOCOMPLETE_SUGGESTIONS = (By.CSS_SELECTOR, ".acp")

    def __init__(self, browser):
        self.browser = browser
        self.wait_driver = WebDriverWait(browser, 10)

    def load(self):
        self.browser.get(self.URL)

    def search(self, phrase):
        search_input_field = self.browser.find_element(*self.SEARCH_INPUT)
        search_input_field.send_keys(phrase + Keys.RETURN)

    def input_phrase(self, phrase):
        search_input_field = self.browser.find_element(*self.SEARCH_INPUT)
        search_input_field.send_keys(phrase)

    def search_and_click_button(self, phrase):
        search_input_field = self.browser.find_element(*self.SEARCH_INPUT)
        search_input_field.send_keys(phrase)
        self.browser.find_element(*self.SEARCH_BUTTON).click()

    def check_autocomplete_suggestions(self):
        autocomplete_suggestions = self.wait_driver.until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".acp")))
        suggestions_text = [suggestion.text for suggestion in autocomplete_suggestions]
        return suggestions_text
