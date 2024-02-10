# Registration_login: регистрация аккаунта

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.select import Select
#
# driver = webdriver.Chrome(executable_path='C:\chromedriver.exe')
# driver.implicitly_wait(5)
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# my_account_btn = driver.find_element_by_link_text("My Account").click()
# email_field = driver.find_element_by_css_selector("[name='email']")
# email_field.send_keys("ares1999@yandex.ru")
# password_field = driver.find_element_by_css_selector("#reg_password:nth-child(2)")
# password_field.send_keys("Qaswerty123!")
# register_btn = driver.find_element_by_css_selector("[name='register']").click()

# Registration_login: логин в систему

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path='C:\chromedriver.exe')
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
my_account_btn = driver.find_element_by_link_text("My Account").click()
email_field = driver.find_element_by_css_selector("[name='username']")
email_field.send_keys("ares1999@yandex.ru")
password_field = driver.find_element_by_id("password")
password_field.send_keys("Qaswerty123!")
login_btn = driver.find_element_by_css_selector("[name='login']").click()
logout_check = WebDriverWait(driver, 20).until(
EC.text_to_be_present_in_element((By.TAG_NAME, "html"), 'Logout'))
print('Its Ok!')