""""""
"""
This module contains DuckDuckGoResultPage,
the page object for the DuckDuckGo result page
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class DuckDuckGoResultPage:
    RESULT_LINKS = (By.CSS_SELECTOR, "a.result__a")
    SEARCH_INPUT = (By.ID, "search_form_input")
    MORE_RESULTS = (By.CSS_SELECTOR, "#rld-1")

    def __init__(self, browser):
        self.browser = browser
        self.wait_driver = WebDriverWait(browser, 10)

    def result_link_titles(self):
        links = self.wait_driver.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "a.result__a")))
        titles = [link.text for link in links]
        return titles

    def search_input_value(self):
        search_input_field = self.browser.find_element(*self.SEARCH_INPUT)
        field_value = search_input_field.get_attribute("value")
        return field_value

    def title(self):
        return self.browser.title

    def click_nth_result(self, index):
        links = self.wait_driver.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "a.result__a")))
        links[index].click()

    def click_more_results(self):
        self.browser.execute_script("window.scrollTo(0, 3000)")
        self.wait_driver.until(EC.presence_of_element_located((By.ID, "rld-1"))).click()
