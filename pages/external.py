""""""
"""
This module contains external sites,
reached by clicking result links in DuckDuckGo result page
"""
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class ExternalPage:
    def __init__(self, browser):
        self.browser = browser
        self.wait_driver = WebDriverWait(browser, 10)

    def title(self, phrase):
        self.wait_driver.until(EC.title_contains(phrase))
        return self.browser.title
