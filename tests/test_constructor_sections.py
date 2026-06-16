from ..locators import ENTER_BUTTON, BUNS, SAUCES, TOPPINGS, BUNS_HEADER, SAUCES_HEADER, TOPPINGS_HEADER, ACTIVE_TAB
from ..helper import authorization
from ..data import LOGIN_PAGE, MAIN_PAGE, LOGIN_DATA

import pytest

from selenium.webdriver.support import expected_conditions


class TestConstructorSections:
    # Авторизация
    def setup_authorization(self, driver, wait, data):
        self.driver = driver
        self.driver.get(LOGIN_PAGE)
        wait.until(expected_conditions.presence_of_element_located(ENTER_BUTTON))

        email = data['email']
        password = data['password']
        authorization(self.driver, email, password)
        wait.until(expected_conditions.url_to_be(MAIN_PAGE))

    # Клик по вкладке
    def click_on_tab(self, wait, tab_locator, tab_header):
        target_tab = wait.until(expected_conditions.element_to_be_clickable(tab_locator))
        target_tab.click()

        # Ожидание элементов
        active_tab = wait.until(expected_conditions.visibility_of_element_located(ACTIVE_TAB))
        header_element = wait.until(expected_conditions.visibility_of_element_located(tab_header))
        return active_tab, header_element

    @pytest.mark.parametrize(
        'tab_text, tab_locator, tab_header',
        [
        ("Соусы", SAUCES, SAUCES_HEADER),
        ("Начинки", TOPPINGS, TOPPINGS_HEADER)
        ],
        ids=["Tab Sauces", "Tab Toppings"])
    def test_constructor_tab_activation_from_inactive(self, driver, wait, tab_locator, tab_text, tab_header):
        self.driver = driver
        # Авторизация
        self.setup_authorization(self.driver, wait, LOGIN_DATA)
        # Клик по табу
        click_result = self.click_on_tab(wait, tab_locator, tab_header)
        active_tab = click_result[0]
        header_element = click_result[1]

        # Проверка
        assert (tab_text in active_tab.text.strip() and header_element.is_displayed())

    def test_constructor_tab_reactivation(self, driver, wait):
        self.driver = driver
        # Авторизация
        self.setup_authorization(self.driver, wait, LOGIN_DATA)
        # Переключение на соседний таб
        self.click_on_tab(wait, SAUCES, SAUCES_HEADER)
        # Клик по табу
        click_result = self.click_on_tab(wait, BUNS, BUNS_HEADER)
        active_tab = click_result[0]
        header_element = click_result[1]

        # Проверка
        assert ("Булки" in active_tab.text.strip() and header_element.is_displayed())