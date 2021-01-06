from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from locators.yandex_locators import Locators


class PageResults:
    """Actions for Yandex results page"""

    url_beginning = 'https://yandex.ru/search'

    def __init__(self, driver):
        self.driver = driver

        self.results_row_xpath = Locators.results_row_xpath


    def results_page_has_loaded(self):
        """Wait and verify that the results page is loaded"""
        try:
            WebDriverWait(self.driver, 5, 0.5).until(EC.url_contains(self.url_beginning))
        except TimeoutException:
            return False
        return True


    def results_are_loaded(self):
        """Wait and verify that result rows are loaded"""
        def results_number_10(driver):
            return len(driver.find_elements_by_xpath(self.results_row_xpath)) >= 10

        try:
            WebDriverWait(self.driver, 5, 0.5).until(results_number_10)
        except TimeoutException:
            return False
        return True


    def results_contain_links(self, link, number_of_results):
        """Verify that the first <number_of_results> of results contain <link>"""
        result_rows = self.driver.find_elements_by_xpath(self.results_row_xpath)
        if not result_rows:
            return False

        for result in result_rows[0:number_of_results]:
            try:
                result.find_element_by_xpath(f'.//a[@href="{link}"]')
            except NoSuchElementException:
                return False
        return True
