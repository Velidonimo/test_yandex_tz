from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from locators.yandex_locators import Locators
from selenium.webdriver.support import expected_conditions as EC


class PageImages:
    """Actions for Yandex home page"""

    url_beginning = 'https://yandex.ru/images'

    def __init__(self, driver):
        self.driver = driver

        self.search_input_xpath = Locators.search_input_xpath
        self.categories_link_xpath = Locators.categories_link_xpath
        self.images_link_xpath = Locators.images_link_xpath
        self.link_img_xpath = Locators.link_img_xpath
        self.openimg_title_xpath = Locators.openimg_title_xpath


    def image_page_has_loaded(self):
        """Waits and verifies that the images page is loaded"""
        try:
            WebDriverWait(self.driver, 5, 0.5).until(EC.url_contains(self.url_beginning))
        except TimeoutException:
            print('\n\n\n')
            print(self.driver.current_url)
            print('\n\n\n')
            return False
        return True


    def click_first_category(self):
        """
        Opens the first category.
        Returns the link text or False, if there's no element
        """
        try:
            link = self.driver.find_element_by_xpath(self.categories_link_xpath)
        except NoSuchElementException:
            return False
        link.click()
        return link.text


    def compare_input_text(self, text):
        """Compares the text from the input textbox to a <text>.
        Returns True if they match or False if don't
        """
        def wait_for_input_to_load(driver):
            return driver.find_element_by_xpath(self.search_input_xpath).get_attribute("value") == text

        try:
            WebDriverWait(self.driver, 5, 0.5).until(wait_for_input_to_load)
        except TimeoutException:
            return False

        return True


    def click_first_image(self):
        """
        Opens the first image.
        Returns the image text or False, if there's no element
        """
        try:
            link = self.driver.find_element_by_xpath(self.images_link_xpath)
            image_text = link.find_element_by_xpath(self.link_img_xpath).get_attribute("alt")
        except NoSuchElementException:
            return False
        link.click()
        return image_text


    def compare_image_text(self, image_text):
        """Compares the title image text to a <text>.
        Returns True if they match or False if don't
        """
        def wait_for_img_to_load(driver):
            return driver.find_element_by_xpath(self.openimg_title_xpath).text == image_text

        try:
            WebDriverWait(self.driver, 5, 0.5).until(wait_for_img_to_load)
        except TimeoutException:
            return False

        return True
