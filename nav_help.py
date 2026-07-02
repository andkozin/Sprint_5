# nav_help.py

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from locators import TestLocators
from url import TestLinks

class NavHelp: # вывел только навигацию

    # 1. личный кабинет
    @staticmethod
    def go_to_profile(driver): 
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable(TestLocators.PERSONAL_BUTTON)).click()
        WebDriverWait(driver, 15).until(EC.url_to_be(TestLinks.personal_account_page_link))

    # 2. в конструктор 
    @staticmethod
    def go_to_constructor(driver):
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable(TestLocators.CONSTRUCTOR_BUTTON)).click()
        WebDriverWait(driver, 15).until(EC.url_to_be(TestLinks.main_page_link))

    # 3. по лого в конструктор
    @staticmethod
    def go_to_constructor_via_logo(driver):
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable(TestLocators.LOGO_BUTTON)).click()
        WebDriverWait(driver, 15).until(EC.url_to_be(TestLinks.main_page_link))

    # 4. по кнопке «Выход» в ЛК
    @staticmethod
    def logout(driver):
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable(TestLocators.LOGOUT_BUTTON)).click()
        WebDriverWait(driver, 15).until(EC.url_to_be(TestLinks.login_page_link))