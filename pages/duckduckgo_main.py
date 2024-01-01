from selenium.webdriver.common.by import By


class DuckduckgoPage:
    URL = 'https://www.duckduckgo.com'
    SEARCH_INPUT = (By.ID, "searchbox_input")
    SEARCH_BUTTON = (By.XPATH, "//*[@id='searchbox_homepage']/div/div/button[2]")

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def search(self, keyword):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(keyword)

        search_btn = self.browser.find_element(*self.SEARCH_BUTTON)
        search_btn.click()