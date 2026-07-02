# test_reg.py

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from url import TestLinks
from locators import TestLocators

    # 1. для проверки регистрации
class TestRegistration:
    # # 1. тест регистрации валид.
    def test_successful_registration(self, driver, registered_user):
        
        assert driver.current_url == TestLinks.login_page_link, f"Нет перехода на /login URL: {driver.current_url}"
        assert WebDriverWait(driver, 10).until(EC.element_to_be_clickable(TestLocators.LOGIN_BUTTON_IN)), "Кнопка 'Войти' на логине нет или не кликабельна"

    # 2. добавил тест для зарегистрироваться с email существующего польз.
    def test_is_user_already_exists(self, driver, registered_user):
        email, password, name = registered_user
        
        driver.get(TestLinks.registration_page_link)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(TestLocators.NAME_FIELD))

        
        driver.find_element(*TestLocators.NAME_FIELD).send_keys(name)
        driver.find_element(*TestLocators.EMAIL_FIELD).send_keys(email)
        driver.find_element(*TestLocators.PASSWORD_FIELD).send_keys(password)

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(TestLocators.REGISTER_BUTTON)).click()

        expected_text = "Такой пользователь уже существует"
        actual_text= WebDriverWait(driver, 10).until(EC.visibility_of_element_located(TestLocators.REGISTRATION_ERROR_MESSAGE)).text.strip()

        assert expected_text in actual_text, (f"Ожидалось: '{expected_text}', Получено: '{actual_text}'")

    # 3. тест регистрации невалид. пароль
    def test_invalid_password_error(self, driver, test_email):
       
        driver.get(TestLinks.registration_page_link)

        # форма с некорр. паролем
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(TestLocators.NAME_FIELD))

        driver.find_element(*TestLocators.NAME_FIELD).send_keys('Андрей')
        driver.find_element(*TestLocators.EMAIL_FIELD).send_keys(test_email)
        driver.find_element(*TestLocators.PASSWORD_FIELD).send_keys('12345')  # 5 символов
        driver.find_element(*TestLocators.REGISTER_BUTTON).click()

        error_message = WebDriverWait(driver,10).until(EC.visibility_of_element_located(TestLocators.ERROR_MESSAGE_PASSWORD)).text.strip()

        assert 'Некорректный пароль' in error_message, (f'сообщение об ошибке нет')