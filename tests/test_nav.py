
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


from url import TestLinks
from locators import TestLocators


class TestNavigation:
    @staticmethod
    # вывел вход ЛК
    def in_profile(driver):
        
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(TestLocators.PERSONAL_BUTTON)).click() # клик по кнопке ЛК 
        WebDriverWait(driver, 10).until(EC.url_to_be(TestLinks.personal_account_page_link))
       
        assert driver.current_url == TestLinks.personal_account_page_link, f'\nЖду URL {TestLinks.personal_account_page_link}, но URL нет перехода ЛК: {driver.current_url}'
        assert WebDriverWait(driver, 10).until(EC.element_to_be_clickable(TestLocators.LOGOUT_BUTTON)), 'Кнопки Выход нет или не кликабельна'

    # 1. Переход в личный кабинет
    def test_go_to_profile(self, driver, authorized_user):
        
        self.in_profile(driver)

    # 2. Переход из личного кабинета в конструктор 
    def test_go_to_constructor_from_profile(self, driver, authorized_user):
        
        self.in_profile(driver) #  переход в ЛК

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(TestLocators.CONSTRUCTOR_BUTTON)).click() # клик «Конструктор»
        WebDriverWait(driver, 10).until(EC.url_to_be(TestLinks.main_page_link))

        assert driver.current_url == TestLinks.main_page_link, 'Нет перехода в конструктор из ЛК'
        assert WebDriverWait(driver, 10).until(EC.element_to_be_clickable(TestLocators.ORDER_BUTTON)), 'Кнопка ОФормить заказ нет или не кликабельна'

    # 3. переход из личного кабинет по лого в конструктор
    def test_go_to_constructor_via_logo(self, driver, authorized_user):

        self.in_profile(driver) #  переход в ЛК
        
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(TestLocators.LOGO_BUTTON)).click() # клик на лого  
        WebDriverWait(driver, 10).until(EC.url_to_be(TestLinks.main_page_link))

        assert driver.current_url == TestLinks.main_page_link,'Нет перехода через логотип'
        assert WebDriverWait(driver, 10).until(EC.element_to_be_clickable(TestLocators.ORDER_BUTTON)), 'Кнопка ОФормить заказ нет или не кликабельна'

    # 4. Выход из аккаунта по кнопке «Выход» в ЛК
    def test_logout_from_profile(self, driver, authorized_user):
        
        self.in_profile(driver) #  переход в ЛК
        
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(TestLocators.LOGOUT_BUTTON)).click() # клик на Выход
        WebDriverWait(driver, 10).until(EC.url_to_be(TestLinks.login_page_link))

        assert driver.current_url == TestLinks.login_page_link, 'Нет выхода из аккаунта'