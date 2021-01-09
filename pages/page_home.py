from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from locators.yandex_locators import Locators


class PageHome:
    """Actions for Yandex home page"""

    def __init__(self, driver):
        self.driver = driver

    def get_input_txtbox(self):
        """Returns the search input textbox if available or False"""
        try:
            self.driver.find_element_by_name(Locators.search_input_name)
        except NoSuchElementException:
            return False
        return True


    def enter_search_text(self, text):
        """Enters a text into the searchbox"""
        self.driver.find_element_by_name(Locators.search_input_name).send_keys(text)


    def enter_n_submit_search_text(self, text):
        """Enters a text into the search box and simulate pressing Enter key"""
        self.enter_search_text(text+"\n")


    def suggests_are_visible(self):
        """Tests if suggest dropdown is shown"""
        def visibility(driver):
            return "popup_visible" in driver.find_element_by_xpath(Locators.suggest_dropdown_xpath).get_attribute('class')

        try:
            WebDriverWait(self.driver, 2).until(visibility)
        except TimeoutException:
            return False
        return True


    def click_search_btn(self):
        """Clicks the main search button"""
        self.driver.find_element_by_xpath(Locators.search_btn_xpath).click()


    def get_link_with_text(self, text):
        """Returns the link with <text> or returns False if the link is not available"""
        try:
            link = self.driver.find_element_by_link_text(text)
        except:
            return False
        return link


    def click_link_with_text(self, text):
        """Clicks the link with <text> or returns False if the link is not available"""
        link = self.get_link_with_text(text)
        if not link:
            return False
        link.click()
        return True
