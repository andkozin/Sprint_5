#conftest.py
import pytest
import time

from selenium import webdriver

from reg_help import Reg
from url import TestLinks
from generator import Generator
from locators import TestLocators

# фикстура драйвера
@pytest.fixture()
def driver():
    chrome_options = webdriver.ChromeOptions()  
    chrome_options.add_argument('--window-size=1920,1080')  #  размер окна
    driver = webdriver.Chrome(options=chrome_options)  # сам драйвер
    yield driver  #  в тесты
    driver.quit()  # закрыл

# фикстура для email
@pytest.fixture
def test_email():
    return Generator.generate_email()

# Фикстура для пароля
@pytest.fixture
def test_password():
    return Generator.generate_password()

# фикстура для регистрации
@pytest.fixture
def registered_user(driver, test_email, test_password):
    
    driver.get(TestLinks.registration_page_link)
    email, password= Reg.registered_user_ok(driver, test_email, test_password)
    Reg.confirm_registration_success(driver)
    return email,password

# для  логина
@pytest.fixture
def authorized_user(driver, registered_user):
    test_email, test_password= registered_user
    Reg.login(driver, test_email, test_password)
    Reg.confirm_login_success(driver)
    return test_email, test_password