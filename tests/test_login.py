
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from reg_help import Reg
from url import TestLinks
from locators import TestLocators

class TestLogin:

    # 1.вход по кнопке «Войти в аккаунт» на главной
    def test_login_from_main_page(self, driver, authorized_user): # возможно надо через кнопку
       
        assert driver.current_url == TestLinks.main_page_link, f'\nЖду URL {TestLinks.main_page_link}, но URL: {driver.current_url}'
        assert WebDriverWait(driver, 15).until(EC.element_to_be_clickable(TestLocators.ORDER_BUTTON)), "Кнопка 'ОФормить зааказ' нет или не кликабельна"

    # 2. Вход через «Личный кабинет»
    def test_login_via_profile_button(self, driver, registered_user):
        
        test_email, test_password,_ = registered_user
 
        driver.get(TestLinks.main_page_link) # на главную страницу 
       
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable(TestLocators.PERSONAL_BUTTON)).click() # клик на ЛК
        
        Reg.login(driver, test_email, test_password)
         
        assert driver.current_url == TestLinks.main_page_link, f'\nЖду URL {TestLinks.main_page_link}, но URL: {driver.current_url}'    
        assert WebDriverWait(driver, 15).until(EC.element_to_be_clickable(TestLocators.ORDER_BUTTON)), "Кнопка 'ОФормить зааказ' нет или не кликабельна"

    # 3.Вход через форму регистрации
    def test_login_from_registration_form(self, driver, registered_user):
        
        test_email, test_password,_ = registered_user

        driver.get(TestLinks.registration_page_link)  # на страницу регистрации
      
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable(TestLocators.LOGIN_LINK)).click() # клик на ссылку Войти
       
        Reg.login(driver, test_email, test_password)
       
        assert driver.current_url == TestLinks.main_page_link, f'\nЖду URL {TestLinks.main_page_link}, но URL: {driver.current_url}'    
        assert WebDriverWait(driver, 15).until(EC.element_to_be_clickable(TestLocators.ORDER_BUTTON)), "Кнопка 'ОФормить зааказ' нет или не кликабельна"

# 4.Вход через форму восстановления пароля
    def test_login_from_recovery_form(self, driver, registered_user):
            
        test_email, test_password,_ = registered_user
            
        driver.get(TestLinks.forgot_password_page_link) # на страницу восстановления пароля
        
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable(TestLocators.LOGIN_LINK)).click() # клик на ссылку Войти
        
        Reg.login(driver, test_email, test_password)
        
        assert driver.current_url == TestLinks.main_page_link, f'\nЖду URL {TestLinks.main_page_link}, но URL: {driver.current_url}'    
        assert WebDriverWait(driver, 15).until(EC.element_to_be_clickable(TestLocators.ORDER_BUTTON)), "Кнопка 'ОФормить зааказ' нет или не кликабельна"