from ..locators import ACCOUNT_LINK, EXIT_BUTTON
from ..helper import authorization

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestLogout:
    def test_exit_by_exit_button(self, driver, login_page,wait, login_data, main_page, cabinet_page):
        self.driver = driver        
        # Авторизация
        self.driver.get(login_page)

        wait.until(expected_conditions.url_contains(login_page))
        email = login_data['email']
        password = login_data['password']

        authorization(self.driver, email, password)

        # Ожидание открытия главной страницы
        wait = WebDriverWait(driver, 10)
        wait.until(expected_conditions.url_contains(main_page))

        # Переход в кабинет для проверки успешной авторизации
        self.driver.find_element(*ACCOUNT_LINK).click()
        wait.until(expected_conditions.url_contains(cabinet_page))

        # Клик по кнопке "Выход"
        self.driver.find_element(*EXIT_BUTTON).click()
        wait.until(expected_conditions.url_contains(login_page))

        assert login_page in self.driver.current_url        
