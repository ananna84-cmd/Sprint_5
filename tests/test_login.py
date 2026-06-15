from ..locators import ACCOUNT_BUTTON, ACCOUNT_LINK, LOGIN_FROM_REGISTER_PAGE_LINK, LOGIN_FROM_FORGET_PASSWORD_PAGE_LINK, EXIT_BUTTON
from ..helper import authorization
from .. import data
import pytest

from selenium.webdriver.support import expected_conditions


class TestLogin:
    @pytest.mark.parametrize(
        'link, button',
        [
        (data.MAIN_PAGE, ACCOUNT_BUTTON),
        (data.MAIN_PAGE, ACCOUNT_LINK),
        (data.REGISTRATION_PAGE, LOGIN_FROM_REGISTER_PAGE_LINK),
        (data.FORGOT_PASSWORD_PAGE, LOGIN_FROM_FORGET_PASSWORD_PAGE_LINK)
        ],
        ids=["Main - Enter","Personal cabinet - Enter","Registration - Enter","Password reset - Enter"]
    )

    def test_login(self, driver, link, wait, button):
        self.driver = driver

        # Страница проверки входа
        self.driver.get(link)
        wait.until(expected_conditions.url_contains(data.MAIN_PAGE))
        
        # Клик по кнопке входа
        self.driver.find_element(*button).click()

        # Ожидание открытия страницы входа
        wait.until(expected_conditions.url_contains(data.MAIN_PAGE))
        email = data.LOGIN_DATA['email']
        password = data.LOGIN_DATA['password']

        authorization(self.driver, email, password)
        # Ожидание открытия главной страницы
        wait.until(expected_conditions.url_contains(data.MAIN_PAGE))
        # Переход в кабинет для проверки успешной авторизации
        self.driver.find_element(*ACCOUNT_LINK).click()
        wait.until(expected_conditions.visibility_of_element_located(EXIT_BUTTON))
        assert data.CABINET_PAGE in driver.current_url
