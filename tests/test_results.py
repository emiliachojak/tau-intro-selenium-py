"""
These tests cover DuckDuckGo result page interactions.
"""
import pytest
from pages.search import DuckDuckGoSearchPage
from pages.result import DuckDuckGoResultPage
from pages.external import ExternalPage


def test_duckduckgo_results_click_nth_link(browser):
    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoResultPage(browser)
    external_page = ExternalPage(browser)

    SEARCH_ENGINE_NAME = "DuckDuckGo"
    phrase = "Beatles"
    index = 0

    search_page.load()
    search_page.search(phrase)
    result_page.click_nth_result(index)

    assert phrase in external_page.title(phrase)
    assert SEARCH_ENGINE_NAME not in external_page.title(phrase)


def test_duckduckgo_results_more_results(browser):
    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoResultPage(browser)

    phrase = "Golden retriever"

    search_page.load()
    search_page.search(phrase)
    first_set_of_links = result_page.result_link_titles()
    result_page.click_more_results()
    second_set_of_links = result_page.result_link_titles()

    assert len(second_set_of_links) > len(first_set_of_links)
