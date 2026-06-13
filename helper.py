from .locators import NAME_FIELD, EMAIL_FIELD, PASSWORD_FIELD, ENTER_BUTTON, REGISTER_BUTTON


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
