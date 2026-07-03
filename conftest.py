#conftest.py
import pytest

from selenium import webdriver

from reg_help import Reg
from url import TestLinks
from generator import Generator

# фикстура драйвера
@pytest.fixture()
def driver():
    chrome_options = webdriver.ChromeOptions()  
    chrome_options.add_argument('--window-size=1920,1080')  #  размер окна
    driver = webdriver.Chrome(options=chrome_options)  # сам драйвер
    yield driver  #  в тесты
    driver.quit()  # закрыл

# фикстура для регистрации
@pytest.fixture
def registered_user(driver):
    name ='Андрей'
    email= Generator.generate_email()
    password=Generator.generate_password()
    driver.get(TestLinks.registration_page_link)
    Reg.registration(driver, email, password,name)
    yield email,password,name

    # для  логина
@pytest.fixture
def authorized_user(driver, registered_user):
    email, password,_= registered_user
    driver.get(TestLinks.login_page_link)
    Reg.login(driver, email, password)
    yield email,password