import pytest
import allure
from allure_commons.types import Severity
from pages.page_home import PageHome
from pages.page_results import PageResults
from pages.page_images import PageImages
from base.base import Base
from images.images import ImagesCompare
import sys, os
my_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, my_path + '/../')



@pytest.mark.usefixtures('set_up')
class TestYandexSearch(Base):

    # @allure.title("01 Testing for textBox and suggests dropdown")
    # @allure.severity(Severity.NORMAL)
    # def test_suggest(self):
    #
    #     with allure.step("Verify if the search textbox is available"):
    #         page_home = PageHome(self.driver)
    #         if not page_home.get_input_txtbox():
    #             raise AssertionError("The search textbox wasn't found")
    #
    #     text = "Тензор"
    #     with allure.step(f"Enter {text}"):
    #         page_home.enter_search_text(text)
    #
    #     with allure.step("Verify if suggests dropdown is shown"):
    #         if not page_home.suggests_are_visible():
    #             raise AssertionError("The suggests dropdown didn't appear")
    #
    #
    # @allure.title('02 Testing for search results')
    # @allure.severity(Severity.CRITICAL)
    # def test_search_results(self):
    #
    #     text = "Тензор"
    #     with allure.step(f"Enter {text} and simulate pressing Enter key"):
    #         page_home = PageHome(self.driver)
    #         page_home.enter_n_submit_search_text(text)
    #
    #     with allure.step("Verify that the result page is loaded"):
    #         page_results = PageResults(self.driver)
    #         if not page_results.results_page_has_loaded():
    #             raise AssertionError("Results didn't load")
    #
    #     with allure.step("Verify that results are loaded"):
    #         if not page_results.results_are_loaded():
    #             raise AssertionError("Results didn't load")
    #
    #     link = "https://tensor.ru/"
    #     number_of_results = 5
    #     with allure.step("Count links number"):
    #         counter = page_results.links_number_in_results(link, number_of_results, self.implicitly_wait)
    #         if counter != number_of_results:
    #             # FIXME take a screenshot
    #             raise AssertionError(f"Only {counter} of {number_of_results} result rows contain the link {link}")


    def open_images_page(self, page_home, page_images):
        """Opens the yandex image page with testing"""
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

        with allure.step(f'Verify that the opened page is "https://yandex.ru/images/...'):
            if not page_images.image_page_has_loaded():
                raise AssertionError("Images page didn't load")


    # @allure.title("03 Testing Yandex search for mismatch between a clicked category and a text in the opened page")
    # @allure.severity(Severity.NORMAL)
    # def test_picture_category(self):
    #     page_home = PageHome(self.driver)
    #     page_images = PageImages(self.driver)
    #
    #     with allure.step("Open page Images"):
    #         self.open_images_page(page_home, page_images)
    #
    #     with allure.step('Open the first category'):
    #         category_text = page_images.click_first_category()
    #         if not category_text:
    #             raise AssertionError("There is no categories")
    #
    #     with allure.step("Compare the input text to a clicked category"):
    #         if not (page_images.compare_input_text(category_text)):
    #             raise AssertionError(f'The input text is not compared to the clicked category "{category_text}"')


    @staticmethod
    def _download_image(page_images, images, name):
        """Downloads the image with testing"""
        url = page_images.get_image_url()
        if not url:
            raise AssertionError("Can't open the first image")
        if not images.download_image(url, name):
            raise AssertionError(f"Can't download from the url: {url}")


    @allure.title("04 Testing clicking forward and backwards between images and comparing them")
    @allure.severity(Severity.CRITICAL)
    def test_title_yandex_image(self):

        page_home = PageHome(self.driver)
        page_images = PageImages(self.driver)
        images = ImagesCompare()

        with allure.step("Open page Images"):
            self.open_images_page(page_home, page_images)

        with allure.step("Open the first category"):
            if not page_images.click_first_category():
                raise AssertionError("There is no categories")

        with allure.step("Open the first image"):
            image_text = page_images.click_first_image()
            if not image_text:
                raise AssertionError("There is no images")

        with allure.step("Verify that the opened image is displayed"):
            if not page_images.open_image_is_displayed():
                raise AssertionError("The opened image is not displayed")

        first_img_name = "img_first"
        forward_img_name = "img_forw"
        backwards_img_name = "img_backw"
        images.delete_images((first_img_name, forward_img_name, backwards_img_name))

        with allure.step("Download first image"):
            self._download_image(page_images, images, first_img_name)

        with allure.step("Click forward button"):
            if not page_images.click_forward_btn():
                raise AssertionError("Can't find forward button")

        with allure.step("Download the image that appears after clicking the forward button"):
            self._download_image(page_images, images, forward_img_name)

        with allure.step("Verify that the first and forward images are different"):
            name1, name2 = first_img_name, forward_img_name
            comparison = images.images_are_even(name1, name2)
            if comparison == images.ERROR:
                raise AssertionError("Can't compare two images."
                                     f"See the {name1}.jpg and {name2}.jpg in /images folder")
            elif comparison == images.EVEN:
                raise AssertionError("After clicking the forward button the image didn't change. "
                                     f"See the {name1}.jpg and {name2}.jpg in /images folder")

        with allure.step("Click backwards button"):
            if not page_images.click_backward_btn():
                raise AssertionError("Can't find backwards button")

        with allure.step("Download the image that appears after clicking the backwards button"):
            self._download_image(page_images, images, backwards_img_name)

        with allure.step("Verify that the first and backwards images are even"):
            name1, name2 = first_img_name, backwards_img_name
            comparison = images.images_are_even(name1, name2)
            if comparison == images.ERROR:
                raise AssertionError("Can't compare two images."
                                     f"See the {name1}.jpg and {name2}.jpg in /images folder")
            elif comparison == images.UNEVEN:
                raise AssertionError("After clicking the backwards button we didn't get the same image. "
                                     f"See the {name1}.jpg and {name2}.jpg in /images folder")
