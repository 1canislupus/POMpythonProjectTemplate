import unittest
from selenium import webdriver
from pages.duckduckgo_main import DuckduckgoPage


class DuckduckgoSearchTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(20)
        self.page = DuckduckgoPage(self.browser)

    def test_search(self):
        self.page.load()
        self.page.search('automation')

        # Assertions
        self.assertIn('automation', self.browser.title)

    def tearDown(self):
        self.browser.quit()


if __name__ == '__main__':
    unittest.main()