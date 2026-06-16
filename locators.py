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

# Активный раздел
ACTIVE_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]")
#parent_element = (By.XPATH, f".//div[contains(@class, 'tab_tab')]")

# Раздел булки
BUNS = (By.XPATH, "//section[contains(@class, 'BurgerIngredients_ingredients')]//div[contains(@class, 'tab_tab')]//span[text()='Булки']")
# Раздел слусы
SAUCES = (By.XPATH, "//section[contains(@class, 'BurgerIngredients_ingredients')]//div[contains(@class, 'tab_tab')]//span[text()='Соусы']")
# Раздел начинки
TOPPINGS = (By.XPATH, "//section[contains(@class, 'BurgerIngredients_ingredients')]//div[contains(@class, 'tab_tab')]//span[text()='Начинки']")

# Локаторы для заголовков
BUNS_HEADER = (By.XPATH, "//div[contains(@class, 'BurgerIngredients_ingredients')]/h2[contains(text(), 'Булки')]")
SAUCES_HEADER = (By.XPATH, "//div[contains(@class, 'BurgerIngredients_ingredients')]/h2[contains(text(), 'Соусы')]")
TOPPINGS_HEADER = (By.XPATH, "//div[contains(@class, 'BurgerIngredients_ingredients')]/h2[contains(text(), 'Начинки')]")
