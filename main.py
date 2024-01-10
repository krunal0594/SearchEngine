import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchEngineTest:
    def __init__(self, driver):
        self.driver = driver

    def visit_search_engine(self, search_engine_url):
        self.driver.get(search_engine_url)

    def submit_search_term(self, search_term):
        search_input = self.driver.find_element(By.NAME, "q")
        search_input.send_keys(search_term)
        search_input.send_keys(Keys.RETURN)

    def assert_results_present(self):
        # Check if any search result is present
        wait = WebDriverWait(self.driver, 10)  # Wait up to 10 seconds
        search_results = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "h3")))
        assert len(search_results) > 0, "No search results found on the page"

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_google_search(setup):
    google_test = SearchEngineTest(setup)
    google_test.visit_search_engine("https://www.google.com")
    google_test.submit_search_term("test framework site:wikipedia.org")
    google_test.assert_results_present()

def test_bing_search(setup):
    bing_test = SearchEngineTest(setup)
    bing_test.visit_search_engine("https://www.bing.com")
    bing_test.submit_search_term("selenium webdriver")
    bing_test.assert_results_present()

if __name__ == "__main__":
    pytest.main(["-v", "test_framework.py"])
