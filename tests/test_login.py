from ..locators import ACCOUNT_BUTTON, ACCOUNT_LINK, LOGIN_FROM_REGISTER_PAGE_LINK, LOGIN_FROM_FORGET_PASSWORD_PAGE_LINK, EXIT_BUTTON
from ..helper import authorization
import data
import pytest

from selenium.webdriver.support import expected_conditions


class TestLogin:
    @pytest.mark.parametrize(
        'link, button',
        [
        (data.main_page, ACCOUNT_BUTTON),
        (data.main_page, ACCOUNT_LINK),
        (data.registration_page, LOGIN_FROM_REGISTER_PAGE_LINK),
        (data.forgot_password_page, LOGIN_FROM_FORGET_PASSWORD_PAGE_LINK)
        ],
        ids=["Main - Enter","Personal cabinet - Enter","Registration - Enter","Password reset - Enter"]
    )

    def test_login(self, driver, link, wait, main_page, button, login_page, login_data, cabinet_page):
        self.driver = driver

        # Страница проверки входа
        self.driver.get(link)
        wait.until(expected_conditions.url_contains(main_page))
        
        # Клик по кнопке входа
        self.driver.find_element(*button).click()

        # Ожидание открытия страницы входа
        wait.until(expected_conditions.url_contains(login_page))
        email = login_data['email']
        password = login_data['password']

        authorization(self.driver, email, password)
        # Ожидание открытия главной страницы
        wait.until(expected_conditions.url_contains(main_page))
        # Переход в кабинет для проверки успешной авторизации
        self.driver.find_element(*ACCOUNT_LINK).click()
        wait.until(expected_conditions.visibility_of_element_located(EXIT_BUTTON))
        assert cabinet_page in driver.current_url
