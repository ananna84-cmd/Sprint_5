from ..locators import ACCOUNT_LINK
from ..helper import authorization

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestPersonalCabinetNavigation:
    def test_personal_cabinet_navigation_without_autorization(self, driver, main_page, login_page):
        self.driver = driver
        # Отрытие главной страницы
        self.driver.get(main_page)

        # Клик по кнопке "Личный кабинет"
        self.driver.find_element(*ACCOUNT_LINK).click()

        # Ожидание открытия страницы входа
        WebDriverWait(driver, 10).until(expected_conditions.url_contains(login_page))

        assert login_page in driver.current_url

    def test_personal_cabinet_navigation_with_autorization(self, driver, login_page, login_data, wait, main_page, cabinet_page):
        self.driver = driver

        # Страница входа
        self.driver.get(login_page)

        email = login_data['email']
        password = login_data['password'] 
        
        # Авторизация
        authorization(self.driver, email, password)

        # Ожидание открытия главной страницы
        wait.until(expected_conditions.url_contains(main_page))

        # Клик по кнопке "Личный кабинет"
        self.driver.find_element(*ACCOUNT_LINK).click()

        wait.until(expected_conditions.url_contains(cabinet_page))
        assert cabinet_page in self.driver.current_url
