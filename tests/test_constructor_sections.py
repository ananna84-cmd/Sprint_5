from ..locators import ENTER_BUTTON, BUNS, SAUCES, TOPPINGS, BUNS_HEADER, SAUCES_HEADER, TOPPINGS_HEADER
from ..helper import authorization

import pytest

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

class TestConstructorSections:

    @pytest.mark.parametrize(
        'tab_text, tab_locator, tab_header',
        [
        ("булки", BUNS, BUNS_HEADER),
        ("соусы", SAUCES, SAUCES_HEADER), 
        ("начинки", TOPPINGS, TOPPINGS_HEADER)
        ],
        ids=["Tab Buns", "Tab Sauces", "Tab Topping"]
    )
    def test_constructor_section_navigation(self, driver, login_page, wait, login_data, main_page, tab_locator, tab_text, tab_header):
        self.driver = driver
        # Авторизация
        self.driver.get(login_page)
        wait.until(expected_conditions.presence_of_element_located(ENTER_BUTTON))

        email = login_data['email']
        password = login_data['password']

        authorization(self.driver, email, password)
        wait.until(expected_conditions.url_contains(main_page))

        
        target_tab = wait.until(expected_conditions.element_to_be_clickable(tab_locator))
        parent_element = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, f".//div[contains(@class, 'tab_tab')]")))

        # Проверка на состояние (активен/не активен)
        is_active = "tab_tab_type_current" in parent_element.get_attribute("class")

        if is_active:
            return
        # Если не активен, клик(активация)
        target_tab.click()

        wait.until(expected_conditions.text_to_be_present_in_element_attribute(
                tab_locator, 
                "class",
                "tab_tab_type_current"
            )
        )

       # Проверка что элемент активен
        active_tab_text = parent_element.text.strip()
        assert tab_text in active_tab_text

        wait.until(expected_conditions.visibility_of_element_located(tab_header))

        # Проверка что заголовок виден
        assert tab_header.is_displayed()
