import pytest
import allure
from allure_commons.types import Severity
import time
from selenium.common.exceptions import NoSuchElementException

from pages.page_home import PageHome
from pages.page_results import PageResults
from base.base import Base
import sys, os
my_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, my_path + '/../')



@pytest.mark.usefixtures('set_up')
class TestYandexSearch(Base):


    @allure.title("Testing for textBox and suggests dropdown")
    @allure.severity(Severity.NORMAL)
    def test_suggest(self):

        with allure.step("Verify if search textbox is available"):
            page_home = PageHome(self.driver)
            try:
                page_home.get_input_txtbox()
            except NoSuchElementException:
                raise AssertionError("The search textbox wasn't found")

        text = "Тензор"
        with allure.step(f"Enter {text}"):
            page_home.enter_search_text(text)

        with allure.step("Verify if suggests dropdown is shown"):
            if not page_home.suggests_are_visible():
                raise AssertionError("The suggests dropdown didn't appear")

        time.sleep(1) # FixMe to observe


    @allure.title('Testing for search results')
    @allure.severity(Severity.CRITICAL)
    def test_search_results(self):
        text = "Тензор"
        with allure.step(f"Enter {text} and simulate pressing Enter key"):
            page_home = PageHome(self.driver)
            page_home.enter_n_submit_search_text(text)

        with allure.step("Verify that the result page is loaded"):
            page_results = PageResults(self.driver)
            if not page_results.results_page_has_loaded():
                raise AssertionError("Results page hasn't loaded")

        with allure.step("Verify that results are loaded"):
            if not page_results.results_are_loaded():
                raise AssertionError("Results hasn't loaded")

        link = "https://tensor.ru/"
        number_of_results = 5
        with allure.step("Count links number"):
            counter = page_results.links_number_in_results(link, number_of_results, self.implicitly_wait)
            if counter != number_of_results:
                raise AssertionError(f"Only {counter} of {number_of_results} result rows contain the link {link}")

        time.sleep(1) # FixMe to observe


    # @allure.title("Testing Yandex search for pictures.")
    # def test_picture(self):
    #     pass
