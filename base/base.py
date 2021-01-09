import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
import allure


class Base:
    """A base class to create and configure a WebDriver"""

    CHROMEDRIVER_PATH = 'D:/AQA/chromedriver.exe'

    implicitly_wait = 10

    @pytest.fixture(autouse=True)
    def set_up(self):
        url = 'https://yandex.ru/'
        self.driver = WebDriver(executable_path=self.CHROMEDRIVER_PATH)
        self.driver.implicitly_wait(self.implicitly_wait)
        with allure.step(f"Open {url}"):
            self.driver.get(url)

        yield self.driver

        if self.driver is not None:
            self.driver.close()
            self.driver.quit()
