"""
These tests cover DuckDuckGo searches.
"""
import pytest
from pages.search import DuckDuckGoSearchPage
from pages.result import DuckDuckGoResultPage


@pytest.mark.parametrize("phrase", ["panda", "python", "polar bear"])
def test_basic_duckduckgo_search(browser, phrase):
    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoResultPage(browser)

    search_page.load()

    search_page.search(phrase)

    assert phrase == result_page.search_input_value()

    titles = result_page.result_link_titles()
    matches = [title for title in titles if phrase.lower() in title.lower()]
    assert len(matches) > 0

    assert phrase in result_page.title()


def test_click_search_button_leads_to_results(browser):
    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoResultPage(browser)
    phrase = "Antarctica"

    search_page.load()

    search_page.search_and_click_button(phrase)

    assert phrase in result_page.title()


def test_autocomplete_suggestions(browser):
    search_page = DuckDuckGoSearchPage(browser)

    phrase = "Vincent"
    phrase_to_find = "Vincent Van Gogh"

    search_page.load()

    search_page.input_phrase(phrase)
    autocomplete_suggestions = search_page.check_autocomplete_suggestions()
    assert phrase_to_find.lower() in list(map(lambda x: x.lower(), autocomplete_suggestions))
