# reg_help.py
import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from url import TestLinks
from generator import Generator
from locators import TestLocators

class Reg:
    @staticmethod # простое заполнение
    def registration(driver, email, password, name):
    
            name_field= WebDriverWait(driver, 10).until(EC.element_to_be_clickable(TestLocators.NAME_FIELD))
            name_field.clear()
            name_field.send_keys(name)

            email_field= WebDriverWait(driver, 10).until(EC.element_to_be_clickable(TestLocators.EMAIL_FIELD))
            email_field.clear()
            email_field.send_keys(email)

            password_field= WebDriverWait(driver, 10).until(EC.element_to_be_clickable(TestLocators.PASSWORD_FIELD))
            password_field.clear()
            password_field.send_keys(password)

            WebDriverWait(driver, 10).until(EC.element_to_be_clickable(TestLocators.REGISTER_BUTTON)).click()

    @staticmethod # успешная регистрация добавил ограничения по кол_во попыток(долго) -забил быстро, пока логины делал
    def registered_user_ok( driver, email, password):
        name='Андрей'
        max_attempts=5

        password_1 = Generator.generate_password()  

        for attempt in range(1, max_attempts + 1):
            
            driver.delete_all_cookies() # чистка
            driver.refresh()
            driver.get(TestLinks.registration_page_link)

            # форму регистрации
            Reg.registration(driver, email, password_1, name=name)
                    
            # проверил на дубль
            if Reg.is_user_already_exists(driver):
                old_email = email
                email=Generator.generate_email() # след. email
                continue
                    
            WebDriverWait(driver, 10).until(lambda d: TestLinks.login_page_link in d.current_url)
            return email, password_1  # вернул
        
    #  для проверки сообщения уже есть 
    @staticmethod
    def is_user_already_exists(driver, timeout=10):
        wait = WebDriverWait(driver, timeout)
        try:
            wait.until(EC.visibility_of_element_located(TestLocators.REGISTRATION_ERROR_MESSAGE))
            # print(f"\nОшибка дубля")
            return True
        except Exception:
            return False
        
    # успешная регистрация
    @staticmethod
    def confirm_registration_success(driver):
        WebDriverWait(driver, 10).until(EC.url_to_be(TestLinks.login_page_link))

    # зполнил login
    @staticmethod
    def login(driver, email, password):
        email_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(TestLocators.EMAIL_FIELD))
        email_field.clear()
        email_field.send_keys(email)

        password_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(TestLocators.PASSWORD_FIELD))
        password_field.clear()
        password_field.send_keys(password)
        
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(TestLocators.LOGIN_BUTTON_IN)).click()
        
    # успешный логин
    @staticmethod
    def confirm_login_success(driver):
        WebDriverWait(driver, 10).until(EC.url_to_be(TestLinks.main_page_link)) #url_contains url_to_be
        
            
        