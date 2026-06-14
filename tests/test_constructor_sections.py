from ..locators import ENTER_BUTTON, BUNS, SAUCES, TOPPINGS, BUNS_HEADER, SAUCES_HEADER, TOPPINGS_HEADER, ACTIVE_TAB
from ..helper import authorization
from ..data import login_page, main_page

import pytest

from selenium.webdriver.support import expected_conditions


class TestConstructorSections:
    # Авторизация
    def setup_authorization(self, driver, wait, data):
        self.driver = driver
        self.driver.get(login_page())
        wait.until(expected_conditions.presence_of_element_located(ENTER_BUTTON))

        email = data['email']
        password = data['password']
        authorization(self.driver, email, password)
        wait.until(expected_conditions.url_to_be(main_page()))

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
    def test_constructor_tab_activation_from_inactive(self, driver, login_data, wait, tab_locator, tab_text, tab_header):
        self.driver = driver
        # Авторизация
        self.setup_authorization(self.driver, wait, login_data)
        # Клик по табу
        click_result = self.click_on_tab(wait, tab_locator, tab_header)
        active_tab = click_result[0]
        header_element = click_result[1]

        # Проверка
        assert (tab_text in active_tab.text.strip() and header_element.is_displayed())

    @pytest.mark.parametrize(
        'tab_text, tab_locator, tab_header, inactiv_tab_locator',
        [("Булки", BUNS, BUNS_HEADER, SAUCES)],
        ids=["Tab Buns"])
    def test_constructor_tab_reactivation(self, driver, login_data, wait, tab_locator, tab_text, tab_header, inactiv_tab_locator):
        self.driver = driver
        # Авторизация
        self.setup_authorization(self.driver, wait,  login_data)
        # Переключение на соседний таб
        self.click_on_tab(wait, inactiv_tab_locator, SAUCES_HEADER)
        # Клик по табу
        click_result = self.click_on_tab(wait, tab_locator, tab_header)
        active_tab = click_result[0]
        header_element = click_result[1]

        # Проверка
        assert (tab_text in active_tab.text.strip() and header_element.is_displayed())