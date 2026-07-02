
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from url import TestLinks
from locators import TestLocators

#класс для проверки переходов 
class TestTadInConstructor:

    # 1.актив булки
    def test_tabs_buns(self, driver):

        driver.get(TestLinks.main_page_link) # главную

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(TestLocators.CONST_TAB_TOPING)).click() # клик начинки ушел с Булки
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(TestLocators.CONST_TAB_BUN)).click() # Клик на Булки

        active_buns_tab=WebDriverWait(driver, 10).until(EC.presence_of_element_located(TestLocators.ACTIVE_TAB_BUN))
        attr= active_buns_tab.get_attribute("class") 

        assert 'tab_tab_type_current' in attr, 'булка не активна'

    # 2. актив соус
    def test_tabs_sauce(self, driver):

        driver.get(TestLinks.main_page_link) # главную
        
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(TestLocators.CONST_TAB_SAUCE)).click() # клик на Соусы
        
        active_sause_tab=WebDriverWait(driver, 10).until(EC.presence_of_element_located(TestLocators.ACTIVE_TAB_SAUCE))
        attr= active_sause_tab.get_attribute("class") 

        assert 'tab_tab_type_current' in attr, 'соусы не активна'

    # 3. актив начинки
    def test_tabs_toping(self, driver):

        driver.get(TestLinks.main_page_link) # главную
       
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(TestLocators.CONST_TAB_TOPING)).click() # клик начинки
       
        active_toping_tab=WebDriverWait(driver, 20).until(EC.presence_of_element_located(TestLocators.ACTIVE_TAB_TOPING))
        attr= active_toping_tab.get_attribute("class") 

        assert 'tab_tab_type_current' in attr, 'начинки не активна'    