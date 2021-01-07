import pytest
import allure
from allure_commons.types import Severity
import time
from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.page_home import PageHome
from pages.page_results import PageResults
from pages.page_images import PageImages
from base.base import Base
import sys, os
my_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, my_path + '/../')



@pytest.mark.usefixtures('set_up')
class TestYandexSearch(Base):


    @allure.title("01 Testing for textBox and suggests dropdown")
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


    @allure.title('02 Testing for search results')
    @allure.severity(Severity.CRITICAL)
    def test_search_results(self):

        text = "Тензор"
        with allure.step(f"Enter {text} and simulate pressing Enter key"):
            page_home = PageHome(self.driver)
            page_home.enter_n_submit_search_text(text)

        with allure.step("Verify that the result page is loaded"):
            page_results = PageResults(self.driver)
            if not page_results.results_page_has_loaded():
                raise AssertionError("Results didn't load")

        with allure.step("Verify that results are loaded"):
            if not page_results.results_are_loaded():
                raise AssertionError("Results didn't load")

        link = "https://tensor.ru/"
        number_of_results = 5
        with allure.step("Count links number"):
            counter = page_results.links_number_in_results(link, number_of_results, self.implicitly_wait)
            if counter != number_of_results:
                # FIXME take a screenshot
                raise AssertionError(f"Only {counter} of {number_of_results} result rows contain the link {link}")

        time.sleep(1) # FixMe to observe



    def open_images_page(self, page_home, page_images):
        """Part one of tests until clicking the category"""
        text = "Картинки"
        with allure.step(f'Verify that "{text}" is available '):
            if not page_home.get_link_with_text(text):
                raise AssertionError(f'No link with text "{text}" is available on the page')

        old_handles = self.driver.window_handles
        with allure.step(f'Click the link "{text}"'):
            if not page_home.click_link_with_text(text):
                raise AssertionError(f'No link with text "{text}" is available on the page')

        with allure.step("Switch to a new handle"):
            for handle in self.driver.window_handles:
                if handle not in old_handles:
                    self.driver.switch_to.window(handle)
                    break
            else:
                raise AssertionError("Can't switch to a new handle")

        with allure.step(f'Verify that the images page is loaded'):
            if not page_images.image_page_has_loaded():
                raise AssertionError("Images page didn't load")

    @allure.title("03 Testing Yandex search for mismatch between a clicked category and a text in opened page")
    @allure.severity(Severity.CRITICAL)
    def test_picture_category(self):
        page_home = PageHome(self.driver)
        page_images = PageImages(self.driver)

        with allure.step("Open page Images"):
            self.open_images_page(page_home, page_images)

        with allure.step('Open the first category'):
            category_text = page_images.click_first_category()
            if not category_text:
                raise AssertionError("There is no categories")

        with allure.step("Compare the input text to a clicked category"):
            if not (page_images.compare_input_text(category_text)):
                raise AssertionError(f'The input text is not compared to the clicked category "{category_text}"')

        time.sleep(1) # FixMe to observe


    @allure.title("04 Testing opening the first page and moving forward and backward")
    @allure.severity(Severity.CRITICAL)
    def test_open_yandex_image(self):
        page_home = PageHome(self.driver)
        page_images = PageImages(self.driver)

        with allure.step("Open page Images"):
            self.open_images_page(page_home, page_images)





