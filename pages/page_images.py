from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException, NoSuchAttributeException
from locators.yandex_locators import Locators
from selenium.webdriver.support import expected_conditions as EC


class PageImages:
    """Actions for Yandex home page"""

    url_beginning = 'https://yandex.ru/images'

    def __init__(self, driver):
        self.driver = driver


    def image_page_has_loaded(self):
        """Waits and verifies that the images page is loaded"""
        try:
            WebDriverWait(self.driver, 5).until(EC.url_contains(self.url_beginning))
        except TimeoutException:
            return False
        return True


    def click_first_category(self):
        """
        Opens the first category of images.
        Returns the link text or False, if there's no element
        """
        try:
            link = self.driver.find_element_by_xpath(Locators.categories_link_xpath)
        except NoSuchElementException:
            return False
        link.click()
        return link.text


    def compare_input_text(self, text):
        """Compares the text from the input textbox to a <text>.
        Returns True if they match or False if don't
        """
        def wait_for_input_to_load(driver):
            return driver.find_element_by_name(Locators.search_input_name).get_attribute("value") == text

        try:
            WebDriverWait(self.driver, 5).until(wait_for_input_to_load)
        except TimeoutException:
            return False

        return True


    def click_first_image(self):
        """
        Opens the first image.
        Returns the image text or False, if there's no element
        """
        try:
            link = self.driver.find_element_by_xpath(Locators.images_link_xpath)
            image_text = link.find_element_by_xpath(Locators.link_img_xpath).get_attribute("alt")
        except (NoSuchElementException, NoSuchAttributeException):
            return False
        link.click()
        return image_text


    def open_image_is_displayed(self):
        """Verifies if the image is displayed to a user"""
        def wait_image_to_display(driver):
            try:
                img = self.driver.find_element_by_class_name(Locators.preview_bigimg_class)
            except NoSuchElementException:
                return False
            return img.is_displayed()

        try:
            WebDriverWait(self.driver, 5).until(wait_image_to_display)
        except TimeoutException:
            return False
        return True


    def get_image_url(self):
        """Returns the url of the opened yandex search img. Or returns False, if can't"""
        try:
            url = self.driver.find_element_by_class_name(Locators.link_bigimg_class).get_attribute("src")
        except (NoSuchElementException, NoSuchAttributeException):
            return False
        return url


    def click_forward_btn(self):
        """Clicks the forward circle button. Returns false, if cannot find it"""
        try:
            self.driver.find_element_by_class_name(Locators.forward_circlebtn_class).click()
        except NoSuchElementException:
            return False
        return True


    def click_backward_btn(self):
        """Clicks the backwards circle button. Returns false, if cannot find it"""
        try:
            self.driver.find_element_by_class_name(Locators.backwards_circlebtn_class).click()
        except NoSuchElementException:
            return False
        return True

