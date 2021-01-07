from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from locators.yandex_locators import Locators


class PageHome:
    """Actions for Yandex home page"""
    def __init__(self, driver):
        self.driver = driver

        self.search_input_xpath = Locators.search_input_xpath
        self.suggest_dropdown_xpath = Locators.suggest_dropdown_xpath
        self.search_btn_xpath = Locators.search_btn_xpath

    def get_input_txtbox(self):
        """Gets search input textbox"""
        return self.driver.find_element_by_xpath(self.search_input_xpath)

    def enter_search_text(self, text):
        """Enters a text into the searchbox"""
        self.driver.find_element_by_xpath(self.search_input_xpath).send_keys(text)

    def enter_n_submit_search_text(self, text):
        """Enters a text into the search box and simulate pressing Enter key"""
        self.enter_search_text(text+"\n")

    def suggests_are_visible(self):
        """Tests if suggest dropdown is shown"""
        def visibility(driver):
            return "popup_visible" in driver.find_element_by_xpath(self.suggest_dropdown_xpath).get_attribute('class')

        try:
            WebDriverWait(self.driver, 2, 0.5).until(visibility)
        except TimeoutException:
            return False
        return True

    def click_search_btn(self):
        """Clicks the main search button"""
        self.driver.find_element_by_xpath(self.search_btn_xpath).click()
