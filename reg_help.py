# reg_help.py

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from url import TestLinks
from locators import TestLocators


class Reg:
    @staticmethod
    def registration(driver, email, password, name):
        wait = WebDriverWait(driver, 10)

        name_field = wait.until(EC.element_to_be_clickable(TestLocators.NAME_FIELD))
        name_field.clear()
        name_field.send_keys(name)

        email_field = wait.until(EC.element_to_be_clickable(TestLocators.EMAIL_FIELD))
        email_field.clear()
        email_field.send_keys(email)

        password_field = wait.until(EC.element_to_be_clickable(TestLocators.PASSWORD_FIELD))
        password_field.clear()
        password_field.send_keys(password)

        wait.until(EC.element_to_be_clickable(TestLocators.REGISTER_BUTTON)).click()
        wait.until(EC.url_to_be(TestLinks.login_page_link))
       
    @staticmethod
    def login(driver, email, password):
        wait = WebDriverWait(driver, 10)

        email_field = wait.until(EC.element_to_be_clickable(TestLocators.EMAIL_FIELD))
        email_field.clear()
        email_field.send_keys(email)

        password_field = wait.until(EC.element_to_be_clickable(TestLocators.PASSWORD_FIELD))
        password_field.clear()
        password_field.send_keys(password)

        wait.until(EC.element_to_be_clickable(TestLocators.LOGIN_BUTTON_IN)).click()
        wait.until(EC.url_to_be(TestLinks.main_page_link))
