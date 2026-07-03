# test_navigation.py

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from nav_help import NavHelp
from url import TestLinks
from locators import TestLocators


class TestNavigation:
    # 1. Переход в личный кабинет
    def test_go_to_profile(self, driver, authorized_user):
        NavHelp.go_to_profile(driver)
        
        assert driver.current_url == TestLinks.personal_account_page_link, 'Неверный URL после перехода в профиль'
        # дополнительно как с ГС, где менятся кнопки Войти и Оформить заказ
        assert WebDriverWait(driver, 15).until(EC.element_to_be_clickable(TestLocators.LOGOUT_BUTTON)), 'Кнопка Выход отсутствует или не кликабельна'

    # 2. Переход из личного кабинета в конструктор 
    def test_go_to_constructor_from_profile(self, driver, authorized_user):
        NavHelp.go_to_profile(driver)  # переход в ЛК
        NavHelp.go_to_constructor(driver)
        
        assert driver.current_url == TestLinks.main_page_link, 'Нет перехода в конструктор из ЛК'
        assert WebDriverWait(driver, 15).until(EC.element_to_be_clickable(TestLocators.ORDER_BUTTON)), 'Кнопка Оформить заказ отсутствует или не кликабельна'

    # 3. переход из личного кабинета по лого в конструктор
    def test_go_to_constructor_via_logo(self, driver, authorized_user):
        NavHelp.go_to_profile(driver)  # переход в ЛК
        NavHelp.go_to_constructor_via_logo(driver)
        
        assert driver.current_url == TestLinks.main_page_link, 'Нет перехода через логотип'
        assert WebDriverWait(driver, 15).until(EC.element_to_be_clickable(TestLocators.ORDER_BUTTON)), 'Кнопка Оформить заказ отсутствует или не кликабельна'

    # 4. Выход из аккаунта по кнопке «Выход» в ЛК
    def test_logout_from_profile(self, driver, authorized_user):
        NavHelp.go_to_profile(driver)  # переход в ЛК
        NavHelp.logout(driver)
        assert driver.current_url == TestLinks.login_page_link, 'Нет выхода из ЛК'
