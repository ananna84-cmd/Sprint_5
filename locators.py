from selenium.webdriver.common.by import By


# Поле для ввода имени
NAME_FIELD = (By.XPATH, "//label[text()='Имя']/following-sibling::input")

# Поле для ввода email/логин
EMAIL_FIELD = (By.XPATH, "//label[text()='Email']/following-sibling::input")

# Поле для ввода пароля
PASSWORD_FIELD = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")

# Обводка поля пароля при ошибке
PASSWORD_INPUT_ERROR_CONTAINER  = (By.CSS_SELECTOR, ".input_status_error")

# Текст ошибки при некорректном пароле
PASSWORD_ERROR_MESSAGE = (By.XPATH, "//p[contains(text(), 'Некорректный пароль')]")

# Кнопка "Зарегистрироваться" на странице регистрации (register)
REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")

# Кнопка "Войти в аккаунт" (главная страница)
ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")

# Кнопка-ссылка "Личный кабинет" (хэдер)
ACCOUNT_LINK = (By.XPATH, "//p[@class='AppHeader_header__linkText__3q_va ml-2' and text()='Личный Кабинет']")

# Кнопка "Войти" на странице "Вход" (login)
ENTER_BUTTON = (By.XPATH, "//button[text()='Войти']")

# Ссылка "Востановить пароль" на странице Вход (login)
FORGET_PASSWORT_LINK = (By.XPATH, "//a[@href='/forgot-password']")

# Ссылка "Зарегистрироваться" на странице Вход (login)
REGISTER_LINK = (By.XPATH, "//a[@href='/register']")

# Ссылка "Войти" на странице "Регистрация" (register)
LOGIN_FROM_REGISTER_PAGE_LINK = (By.XPATH, "//p[contains(text(), 'Уже зарегистрированы?')]//a[@href='/login']")

# Ссылка "Войти" на странице "Восстановить пароль" (forgot-password)
LOGIN_FROM_FORGET_PASSWORD_PAGE_LINK = (By.XPATH, "//p[contains(text(), 'Вспомнили пароль?')]//a[@href='/login']")

# Кнопка-ссылка "Конструктор" (хэдер)
CONSTRUCTOR_LINK = (By.XPATH, "//ul/li/a[@href='/']")

# Логотип-ссылка "stellar burgers" (хэдер)
LOGO_LINK = (By.XPATH, "html/body/div/div/header/nav/div/a[@href='/']")

# Кнопка "Выйти" в личном кабинете (account/profile)
EXIT_BUTTON = (By.XPATH, "//button[text()='Выход']")

# Раздел булки
BUNS = (By.XPATH, "//*[@id='root']/div/main/section[1]/div[1]/div[1]/span")
# Раздел слусы
SAUCES = (By.XPATH, "//*[@id='root']/div/main/section[1]/div[1]/div[2]/span")
# Раздел начинки
TOPPINGS = (By.XPATH, "//*[@id='root']/div/main/section[1]/div[1]/div[3]/span") 


# Локаторы для заголовков
BUNS_HEADER = (By.CSS_SELECTOR, "//*[@id='root']/div/main/section[1]/div[2]/h2[1]")
SAUCES_HEADER = (By.CSS_SELECTOR, "//*[@id='root']/div/main/section[1]/div[2]/h2[2]")
TOPPINGS_HEADER = (By.CSS_SELECTOR, "//*[@id='root']/div/main/section[1]/div[2]/h2[3]")
