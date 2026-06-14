from ..locators import ACCOUNT_LINK, CONSTRUCTOR_LINK, LOGO_LINK
from ..helper import authorization
import pytest

from selenium.webdriver.support import expected_conditions

class TestConstructorFromPersonalCabinet:

    @pytest.mark.parametrize(
        'link',
        [CONSTRUCTOR_LINK, LOGO_LINK],
        ids=["By button Constructor", "By logo 'Stellar Burgers'"]
    )
    def test_personal_cabinet_navigation_with_authorization(self, driver, login_data, login_page, wait, main_page, cabinet_page, link):
        self.driver = driver
        email = login_data['email']
        password = login_data['password']
        # Страница входа
        driver.get(login_page)
        authorization(self.driver, email, password)

        # Ожидание открытия главной страницы
        wait.until(expected_conditions.url_contains(main_page))

        # Клик по кнопке "Личный кабинет"
        driver.find_element(*ACCOUNT_LINK).click()
        wait.until(expected_conditions.url_contains(cabinet_page))

        # Проверка перехода по клику на "Конструктор" и логотип
        driver.find_element(*link).click()
        wait.until(expected_conditions.url_contains(main_page))

        assert main_page == driver.current_url
