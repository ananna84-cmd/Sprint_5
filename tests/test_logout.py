from ..locators import ACCOUNT_LINK, EXIT_BUTTON
from ..helper import authorization
from ..data import LOGIN_PAGE, MAIN_PAGE, CABINET_PAGE, LOGIN_DATA

from selenium.webdriver.support import expected_conditions

class TestLogout:
    def test_exit_by_exit_button(self, driver, wait):
        self.driver = driver        
        # Авторизация
        self.driver.get(LOGIN_PAGE)

        wait.until(expected_conditions.url_contains(LOGIN_PAGE))
        email = LOGIN_DATA['email']
        password = LOGIN_DATA['password']

        authorization(self.driver, email, password)

        # Ожидание открытия главной страницы
        wait.until(expected_conditions.url_contains(MAIN_PAGE))

        # Переход в кабинет для проверки успешной авторизации
        self.driver.find_element(*ACCOUNT_LINK).click()
        wait.until(expected_conditions.url_contains(CABINET_PAGE))

        # Клик по кнопке "Выход"
        self.driver.find_element(*EXIT_BUTTON).click()
        wait.until(expected_conditions.url_contains(LOGIN_PAGE))

        assert LOGIN_PAGE in self.driver.current_url        
