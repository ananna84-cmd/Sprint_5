from .locators import NAME_FIELD, EMAIL_FIELD, PASSWORD_FIELD, ENTER_BUTTON, REGISTER_BUTTON
import random

# Генирация 3-х случайных цифр и возвращение их в виде строки
def generate_nums():
    num_1 = str(random.randint(0, 9))
    num_2 = str(random.randint(0, 9))
    num_3 = str(random.randint(0, 9))
    return num_1 + num_2 + num_3

# Создание пароля заданой длины
def create_password(password_length = 8):
    digits = '0123456789'
    return ''.join(random.choice(digits) for _ in range(password_length))

# Авторизация
def authorization(driver, email, password):

    # Заполнение формы
    driver.find_element(*EMAIL_FIELD).send_keys(email)
    driver.find_element(*PASSWORD_FIELD).send_keys(password)

    # Клик по кнопке "Войти"
    driver.find_element(*ENTER_BUTTON).click()


# Заполнение формы и регистрация
def registration(driver, name, email, password):
    
    # Заполнение формы
    driver.find_element(*NAME_FIELD).send_keys(name)
    driver.find_element(*EMAIL_FIELD).send_keys(email)
    driver.find_element(*PASSWORD_FIELD).send_keys(password)

    # Клик по кнопке "Зарегистрировать"
    driver.find_element(*REGISTER_BUTTON).click()
