Home


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path='C:\chromedriver.exe')
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
driver.execute_script("window.scrollBy(0, 600);")
ruby_btn = driver.find_element_by_css_selector("[src='https://practice.automationtesting.in/wp-content/uploads/2017/01/Selenium-Ruby-300x300.jpg']").click()
driver.execute_script("window.scrollBy(0, 400);")
reviews_btn = driver.find_element_by_class_name("reviews_tab").click()
five_stars_btn = driver.find_element_by_class_name("star-5").click()
comment_field = driver.find_element_by_id("comment")
comment_field.send_keys("Nice book!")
driver.execute_script("window.scrollBy(0, 200);")
name_field = driver.find_element_by_id("author")
name_field.send_keys("Anton")
email_field = driver.find_element_by_id("email")
email_field.send_keys("xxxxdddd@yandex.ru")
submit_btn = driver.find_element_by_id("submit").click()