from ..locators import REGISTER_BUTTON, ENTER_BUTTON, ACCOUNT_LINK, EXIT_BUTTON, PASSWORD_FIELD, EMAIL_FIELD, PASSWORD_INPUT_ERROR_CONTAINER, PASSWORD_ERROR_MESSAGE
from ..helper import registration, authorization
from ..data import registration_page, main_page, cabinet_page

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestRegistration:
    def test_registration_with_valid_data_succeeds(self, driver, user_valid_data_registration, wait):
        self.driver = driver
        # Открытие страницы регистрации
        self.driver.get(registration_page())

        name = user_valid_data_registration['name']
        email = user_valid_data_registration['email']
        password = user_valid_data_registration['pasword']
        wait.until(expected_conditions.visibility_of_element_located(REGISTER_BUTTON))
        registration(self.driver, name, email, password)

        wait.until(expected_conditions.visibility_of_element_located(ENTER_BUTTON))

        # Авторизация
        authorization(self.driver, email, password)
        wait.until(expected_conditions.url_contains(main_page()))

        # Переход в кабинет для проверки успешной авторизации
        self.driver.find_element(*ACCOUNT_LINK).click()
        wait.until(expected_conditions.visibility_of_element_located(EXIT_BUTTON))
        assert cabinet_page() in driver.current_url

    def test_registration_with_invalid_password_length_shows_error(self, driver,  create_invalid_password):    
        self.driver = driver
        # Открытие страницы регистрации 
        self.driver.get(registration_page())
  
        # Заполнение только поля пароля
        driver.find_element(*PASSWORD_FIELD).send_keys(create_invalid_password)

        # Переход в поле email, для снятия фокуса с поля пароля
        self.driver.find_element(*EMAIL_FIELD).click()
        
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(PASSWORD_INPUT_ERROR_CONTAINER))
        # Проверка наличия красной обводки
        assert driver.find_element(*PASSWORD_INPUT_ERROR_CONTAINER).is_displayed()

        # Проверка видимости и наличия текста ошибки
        assert self.driver.find_element(*PASSWORD_ERROR_MESSAGE).is_displayed()
