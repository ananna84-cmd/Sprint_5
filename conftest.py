import random
import pytest
from .helper import generate_nums, create_password

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

# Ожидание
@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, 10)

@pytest.fixture
# Создание email
def create_email():
    prefix = "anna_an_48"
    nums = generate_nums()
    domain = "yandex.ru"
    return f"{prefix}_{nums}@{domain}"

@pytest.fixture
def create_invalid_password():
    length = random.randint(1, 5)
    return create_password(length)

@pytest.fixture
# Генерация данных для регистрации
def user_valid_data_registration(create_email):
        name = "Anna"
        email = create_email
        password = create_password()

        return {
            'name': name,
            'email': email,
            'pasword': password
        }
