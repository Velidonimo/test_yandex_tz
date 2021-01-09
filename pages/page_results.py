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


    def results_page_has_loaded(self):
        """Waits and verifies that the results page is loaded"""
        try:
            WebDriverWait(self.driver, 5).until(EC.url_contains(self.url_beginning))
        except TimeoutException:
            return False
        return True


    def results_are_loaded(self):
        """Waits and verifies that result rows are loaded"""
        def results_number_10(driver):
            return len(driver.find_elements_by_xpath(Locators.results_row_xpath)) >= 10

        try:
            WebDriverWait(self.driver, 5).until(results_number_10)
        except TimeoutException:
            return False
        return True


    def results_contain_links(self, link, number_of_results):
        """Verifies that the first <number_of_results> of results contain <link>"""
        result_rows = self.driver.find_elements_by_xpath(Locators.results_row_xpath)
        if not result_rows:
            return False

        for result in result_rows[0:number_of_results]:
            try:
                result.find_element_by_xpath(f'.//a[@href="{link}"]')
            except NoSuchElementException:
                return False
        return True


    def links_number_in_results(self, link, number_of_results, default_implicitly_wait):
        """
        Counts result rows with <link> in first <number_of_results> search results
        :param link: the link to look for
        :param number_of_results: number of first rows in results to look in
        :param default_implicitly_wait: the base driver implicitly wait value for test
        """
        result_rows = self.driver.find_elements_by_xpath(Locators.results_row_xpath)
        if not result_rows:
            return False

        # speed up test, because the page is already loaded
        self.driver.implicitly_wait(0)

        counter = 0
        for result in result_rows[0:number_of_results]:
            try:
                result.find_element_by_xpath(f'.//a[@href="{link}"]')
                counter += 1
            except NoSuchElementException:
                continue

        # return back the implicitly_wait value
        self.driver.implicitly_wait(default_implicitly_wait)
        return counter
