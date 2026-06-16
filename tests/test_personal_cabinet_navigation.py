from ..locators import ACCOUNT_LINK
from ..helper import authorization
from ..data import MAIN_PAGE, LOGIN_PAGE, CABINET_PAGE, LOGIN_DATA

from selenium.webdriver.support import expected_conditions


class TestPersonalCabinetNavigation:
    def test_personal_cabinet_navigation_without_autorization(self, driver, wait):
        self.driver = driver
        # Отрытие главной страницы
        self.driver.get(MAIN_PAGE)

        # Клик по кнопке "Личный кабинет"
        self.driver.find_element(*ACCOUNT_LINK).click()

        # Ожидание открытия страницы входа
        wait.until(expected_conditions.url_contains(LOGIN_PAGE))

        assert LOGIN_PAGE == driver.current_url

    def test_personal_cabinet_navigation_with_autorization(self, driver, wait):
        self.driver = driver

        # Страница входа
        self.driver.get(LOGIN_PAGE)

        email = LOGIN_DATA['email']
        password = LOGIN_DATA['password'] 
        
        # Авторизация
        authorization(self.driver, email, password)

        # Ожидание открытия главной страницы
        wait.until(expected_conditions.url_contains(MAIN_PAGE))

        # Клик по кнопке "Личный кабинет"
        self.driver.find_element(*ACCOUNT_LINK).click()

        wait.until(expected_conditions.url_contains(CABINET_PAGE))
        assert CABINET_PAGE == self.driver.current_url
