import random
import pytest

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

# Главная страница
@pytest.fixture
def main_page():
    return "https://stellarburgers.education-services.ru/"

# Страница регистрации
@pytest.fixture
def registration_page():
    return "https://stellarburgers.education-services.ru/register"

# Страница входа
@pytest.fixture
def login_page():
    return "https://stellarburgers.education-services.ru/login"

# Страница профиля
@pytest.fixture
def cabinet_page():
    return "https://stellarburgers.education-services.ru/account/profile"

# Страница восстановления пароля
@pytest.fixture
def forgot_password_page():
    return "https://stellarburgers.education-services.ru/forgot-password"

# Ожидание
@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, 10)

# Генирация 3-х случайных цифр и возвращение их в виде строки
def generate_nums():
    num_1 = str(random.randint(0, 9))
    num_2 = str(random.randint(0, 9))
    num_3 = str(random.randint(0, 9))
    return num_1 + num_2 + num_3

@pytest.fixture
# Создание email
def create_email():
    prefix = "anna_an_48"
    nums = generate_nums()
    domain = "yandex.ru"
    return f"{prefix}_{nums}@{domain}"

@pytest.fixture
# Данные для авторизации
def login_data():
    return {
        "email" : "anna-26@yandex.ru",
        "password" : "123456"
    }

# Создание пароля заданой длины
def create_password(password_length = 8):
    digits = '0123456789'
    return ''.join(random.choice(digits) for _ in range(password_length))

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
