from ..locators import ACCOUNT_LINK, CONSTRUCTOR_LINK, LOGO_LINK
from ..helper import authorization
from ..data import LOGIN_PAGE, MAIN_PAGE, CABINET_PAGE, LOGIN_DATA
import pytest

from selenium.webdriver.support import expected_conditions

class TestConstructorFromPersonalCabinet:

    @pytest.mark.parametrize(
        'link',
        [CONSTRUCTOR_LINK, LOGO_LINK],
        ids=["By button Constructor", "By logo 'Stellar Burgers'"]
    )
    def test_personal_cabinet_navigation_with_authorization(self, driver, wait, link):
        self.driver = driver
        email = LOGIN_DATA['email']
        password = LOGIN_DATA['password']
        # Страница входа
        driver.get(LOGIN_PAGE)
        authorization(self.driver, email, password)

        # Ожидание открытия главной страницы
        wait.until(expected_conditions.url_contains(MAIN_PAGE))

        # Клик по кнопке "Личный кабинет"
        driver.find_element(*ACCOUNT_LINK).click()
        wait.until(expected_conditions.url_contains(CABINET_PAGE))

        # Проверка перехода по клику на "Конструктор" и логотип
        driver.find_element(*link).click()
        wait.until(expected_conditions.url_contains(MAIN_PAGE))

        assert MAIN_PAGE == driver.current_url
