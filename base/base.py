import pytest
from selenium.webdriver.chrome.webdriver import WebDriver


class Base:
    """A base class to create and configure a WebDriver"""

    @pytest.fixture(autouse=True)
    def set_up(self):
        url = 'https://yandex.ru/'
        self.driver = WebDriver(executable_path='D:/AQA/chromedriver.exe')
        self.driver.implicitly_wait(2)
        self.driver.get(url)

        yield self.driver

        if self.driver is not None:
            self.driver.close()
            self.driver.quit()
