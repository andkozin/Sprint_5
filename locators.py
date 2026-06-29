# locators.py
from selenium.webdriver.common.by import By

class TestLocators:
    
    NAME_FIELD = (By.XPATH, ".//label[text()='Имя']/following-sibling::input[1]") # поле Имя формы регистрации

    EMAIL_FIELD = (By.XPATH, ".//label[text()='Email']/following-sibling::input[1]") # поле Email формы регистрации

    PASSWORD_FIELD = (By.XPATH, ".//label[text()='Пароль']/following-sibling::input[1]") # поле Пароль формы регистрации

    REGISTER_BUTTON = (By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']") # кнопка Зарегистрироваться в форме регистрации

    ERROR_MESSAGE_PASSWORD = (By.XPATH, "//p[contains(text(), 'Некорректный пароль')]") # для сообщение Некорректный пароль

    REGISTER_LINK_NEW_USER = (By.XPATH, "//a[contains(@class, 'Auth_link__1fOlj') and contains(text(), 'Зарегистрироваться')]") # ссылка Зарегистрироваться на /login

    REGISTRATION_ERROR_MESSAGE = (By.XPATH,  "//p[contains(text(), 'Такой пользователь уже существует')]") # для сообщения Такой пользователь уже существует при регистрации

    LOGIN_BUTTON_MAIN = (By.XPATH, "//button[normalize-space()='Войти в аккаунт']") # кнопка Войти в аккаунт на главной страницы
    
    ORDER_BUTTON = (By.XPATH, "//button[normalize-space()='Оформить заказ']") # кнопка Оформить заказ на главной после логина

    FORGOT_PASSWORD_BUTTON=(By.XPATH, '//button[contains(text(), "Восстановить")]') # ссылка на страницу Восстановления пароля

    LOGIN_BUTTON_IN = (By.CSS_SELECTOR, "button[data-test='login-button'], .button_button__33qZ0") # кнопка Войти на login
    
    LOGIN_LINK = (By.CSS_SELECTOR, 'a.Auth_link__1fOlj') # ссылка Войти на странице Регистрации и Восстан. пароля

    PERSONAL_BUTTON = (By.XPATH, "//*[contains(text(), 'Личный Кабинет')]") # кнопка ЛК

    CONSTRUCTOR_BUTTON = (By.XPATH, "//*[contains(text(), 'Конструктор')]") # кнопка Конструктор

    LOGOUT_BUTTON = (By.XPATH, "//*[contains(@class, 'Account_button')]") # кнопка Выход в ЛК

    LOGO_BUTTON = (By.XPATH, "//*[contains(@class, 'AppHeader_header__logo')]") # лого на ГС

    CONST_TAB_BUN = (By.XPATH, "*//span[contains(text(), 'Булки')]") # вкладка Булки
    CONST_TAB_SAUCE = (By.XPATH, "*//span[contains(text(), 'Соусы')]") # вкладка Соусы
    CONST_TAB_TOPING = (By.XPATH, "*//span[contains(text(), 'Начинки')]") # вкладка Начинки

    ACTIVE_TAB_BUN = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current') and .//span[text()='Булки']]") # вкладка Булки актив. 
    ACTIVE_TAB_SAUCE = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current') and .//span[text()='Соусы']]") # вкладка Соусы актив. 
    ACTIVE_TAB_TOPING = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current') and .//span[text()='Начинки']]") # вкладка Начинки актив. 