"""
This module contains shared fixtures
"""

import json
import pytest
import selenium.webdriver


@pytest.fixture
def config(scope="session"):
    # Read the file
    with open("/home/emilka/Desktop/tests/selenium_search_engine_tests/tau-intro-selenium-py/config.json") as config_file:
        config = json.load(config_file)

    # Assert values are acceptable
    assert config["browser"] in ["Firefox", "Chrome", "Headless Chrome"]

    # Return config
    return config


@pytest.fixture
def browser(config):
    # Initialize the WebDriver instance
    if config["browser"] == "Firefox":
        b = selenium.webdriver.Firefox()
    elif config["browser"] == "Chrome":
        b = selenium.webdriver.Chrome()
    elif config["browser"] == "Headless Chrome":
        opts = selenium.webdriver.ChromeOptions()
        opts.add_argument("headless")
        b = selenium.webdriver.Chrome(options=opts)
    else:
        raise Exception(f"Browser {config['browser']} is not supported")

    # Return the WebDriver instance for the setup
    yield b

    # Quit the WebDriver instance for the cleanup
    b.quit()
