# test_reg.py
import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from url import TestLinks
from locators import TestLocators

# 1. для проверки регистрации
class TestRegistration:
    # тест регистрации валид.
    def test_successful_registration(self, driver, registered_user):
        
        WebDriverWait(driver, 10).until(EC.url_to_be(TestLinks.login_page_link))
        # проверка на странице логина
        assert driver.current_url == TestLinks.login_page_link, f'\nОжидался URL {TestLinks.login_page_link}, но URL: {driver.current_url}'

    # 2. тест регистрации невалид.
    def test_invalid_password_error(self, driver, test_email):
       
        driver.get(TestLinks.registration_page_link)

        # заполненяю форму с некорр. паролем
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(TestLocators.NAME_FIELD))
        driver.find_element(*TestLocators.NAME_FIELD).send_keys('Андрей')
        driver.find_element(*TestLocators.EMAIL_FIELD).send_keys(test_email)
        driver.find_element(*TestLocators.PASSWORD_FIELD).send_keys('12345')  # 5 символов
        driver.find_element(*TestLocators.REGISTER_BUTTON).click()

        # жду ошибку
        error_message = WebDriverWait(driver,15).until(EC.visibility_of_element_located(TestLocators.ERROR_MESSAGE_PASSWORD)).text

        assert 'Некорректный пароль' in error_message, 'сообщение об ошибке нет'