# Shop: отображение страницы товара

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
# email_field = driver.find_element_by_css_selector("[name='username']")
# email_field.send_keys("ares1999@yandex.ru")
# password_field = driver.find_element_by_id("password")
# password_field.send_keys("Qaswerty123!")
# login_btn = driver.find_element_by_css_selector("[name='login']").click()
# shop_btn = driver.find_element_by_id("menu-item-40").click()
# html_book_btn = driver.find_element_by_css_selector("[src='https://practice.automationtesting.in/wp-content/uploads/2017/01/Mastering-HTML5-Forms-300x300.jpg']").click()
# book_title_check = WebDriverWait(driver, 20).until(
# EC.text_to_be_present_in_element((By.CLASS_NAME, "product_title.entry-title"), 'HTML5 Forms'))
# print('Its ok')

# Shop: количество товаров в категории

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

# driver = webdriver.Chrome(executable_path='C:\chromedriver.exe')
# driver.implicitly_wait(5)
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# my_account_btn = driver.find_element_by_link_text("My Account").click()
# email_field = driver.find_element_by_css_selector("[name='username']")
# email_field.send_keys("ares1999@yandex.ru")
# password_field = driver.find_element_by_id("password")
# password_field.send_keys("Qaswerty123!")
# login_btn = driver.find_element_by_css_selector("[name='login']").click()
# shop_btn = driver.find_element_by_id("menu-item-40").click()
# html_category = driver.find_element_by_css_selector("[href='https://practice.automationtesting.in/product-category/html/']").click()
# time.sleep(2)
# item = driver.find_element_by_class_name("woocommerce-LoopProduct-link")
# time.sleep(2)
# if len(item) == 3:
#     print("Все ок")
# else:
#     print("Не проходит")
# time.sleep(2)

# Shop: сортировка товаров

# from selenium import webdriver
# import time
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
# email_field = driver.find_element_by_css_selector("[name='username']")
# email_field.send_keys("ares1999@yandex.ru")
# password_field = driver.find_element_by_id("password")
# password_field.send_keys("Qaswerty123!")
# login_btn = driver.find_element_by_css_selector("[name='login']").click()
# shop_btn = driver.find_element_by_id("menu-item-40").click()
# selector_check = WebDriverWait(driver, 20).until(
#  EC.text_to_be_present_in_element((By.CSS_SELECTOR, "[selected='selected']"), 'Default sorting'))
# selector = driver.find_element_by_class_name("orderby")
# select = Select(selector)
# select.select_by_value("price-desc")
# selector_check_2 = WebDriverWait(driver, 20).until(
#  EC.text_to_be_present_in_element((By.CLASS_NAME, "orderby"), 'Sort by price: high to low'))
# print('Все ок')

# Shop: отображение, скидка товара

# from selenium import webdriver
# import time
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
# email_field = driver.find_element_by_css_selector("[name='username']")
# email_field.send_keys("ares1999@yandex.ru")
# password_field = driver.find_element_by_id("password")
# password_field.send_keys("Qaswerty123!")
# login_btn = driver.find_element_by_css_selector("[name='login']").click()
# shop_btn = driver.find_element_by_id("menu-item-40").click()
# android_btn = driver.find_element_by_css_selector("[src='https://practice.automationtesting.in/wp-content/uploads/2017/01/Android-Quick-Start-Guide-300x300.png']").click()
# old_price = driver.find_element_by_css_selector("del > .woocommerce-Price-amount")
# old_price_text = old_price.text
# assert old_price_text == "₹600.00"
# new_price = driver.find_element_by_css_selector("ins > .woocommerce-Price-amount")
# new_price_text = new_price.text
# assert new_price_text == "₹450.00"
# img_btn = WebDriverWait(driver, 20).until(
#   EC.element_to_be_clickable((By.CSS_SELECTOR, "[src='https://practice.automationtesting.in/wp-content/uploads/2017/01/Android-Quick-Start-Guide-600x600.png'")))
# img_btn.click()
# close_btn = WebDriverWait(driver, 20).until(
#   EC.element_to_be_clickable((By.CLASS_NAME, "pp_close")))
# close_btn.click()
#
# Shop: проверка цены в корзине

# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.select import Select
#
# driver = webdriver.Chrome(executable_path='C:\chromedriver.exe')
# driver.implicitly_wait(5)
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# shop_btn = driver.find_element_by_id("menu-item-40").click()
# book_buy_btn = driver.find_element_by_css_selector("[href='/shop/?add-to-cart=182']").click()
# time.sleep(3)
# cart_items = driver.find_element_by_class_name("cartcontents")
# cart_items_text = cart_items.text
# assert cart_items_text == "1 Item"
# cart_money = driver.find_element_by_css_selector("a > .amount")
# cart_money_text = cart_money.text
# assert cart_money_text == "₹180.00"
# cast_btn = driver.find_element_by_class_name("cartcontents").click()
# subtotal = WebDriverWait(driver, 20).until(
# EC.text_to_be_present_in_element((By.CSS_SELECTOR, "[data-title='Subtotal'] > .woocommerce-Price-amount.amount"), '₹180.00'))
# total = WebDriverWait(driver, 20).until(
# EC.text_to_be_present_in_element((By.CSS_SELECTOR, "[data-title='Total'] > Strong"), '₹183.60'))

# Shop: работа в корзине

# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.select import Select

# driver = webdriver.Chrome(executable_path='C:\chromedriver.exe')
# driver.implicitly_wait(5)
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# shop_btn = driver.find_element_by_id("menu-item-40").click()
# driver.execute_script("window.scrollBy(0, 500);")
# book_buy_btn = driver.find_element_by_css_selector("[href='/shop/?add-to-cart=182']").click()
# time.sleep(5)
# book_buy_2_btn = driver.find_element_by_css_selector("[href='/shop/?add-to-cart=180']").click()
# time.sleep(2)
# cart_btn = driver.find_element_by_class_name("cartcontents").click()
# time.sleep(3)
# remove_btn = driver.find_element_by_css_selector(".remove:nth-child(1)").click()
# undo_btn = driver.find_element_by_link_text("Undo?").click()
# amount_books = driver.find_element_by_css_selector("[name='cart[045117b0e0a11a242b9765e79cbf113f][qty]']")
# amount_books.clear()
# amount_books.send_keys("3")
# update_basket_btn = driver.find_element_by_css_selector("[name='update_cart']").click()
# amount_books_value = amount_books.get_attribute('value')
# assert amount_books_value == "3"
# time.sleep(3)
# apply_coupon_btn = driver.find_element_by_css_selector("[name='apply_coupon']").click()
# error_message = driver.find_element_by_class_name("woocommerce-error")
# error_message_text = error_message.text
# assert error_message_text == "Please enter a coupon code."

# Shop: покупка товара

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path='C:\chromedriver.exe')
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
shop_btn = driver.find_element_by_id("menu-item-40").click()
driver.execute_script("window.scrollBy(0, 300);")
book_buy_btn = driver.find_element_by_css_selector("[href='/shop/?add-to-cart=182']").click()
time.sleep(3)
cart_btn = driver.find_element_by_class_name("cartcontents").click()
proceed_to_checkout = WebDriverWait(driver, 20).until(
 EC.element_to_be_clickable((By.CSS_SELECTOR, "[href='https://practice.automationtesting.in/checkout/']")))
proceed_to_checkout.click()
first_name = WebDriverWait(driver, 20).until(
 EC.element_to_be_clickable((By.ID, "billing_first_name")))
first_name.send_keys("Anton")
last_name = driver.find_element_by_id("billing_last_name")
last_name.send_keys("Andeev")
email_name = driver.find_element_by_id("billing_email")
email_name.send_keys("aaaa@yandex.ru")
phone = driver.find_element_by_id("billing_phone")
phone.send_keys("89266572891")
country_click = driver.find_element_by_id("s2id_billing_country").click()
country_send_keys = driver.find_element_by_id("s2id_autogen1_search")
country_send_keys.send_keys("Russia")
country_choose = driver.find_element_by_class_name("select2-result-label").click()
address = driver.find_element_by_id("billing_address_1")
address.send_keys("Pushkino Street")
city = driver.find_element_by_id("billing_city")
city.send_keys("Moscow")
state = driver.find_element_by_id("billing_state")
state.send_keys("Russia")
postecode = driver.find_element_by_id("billing_postcode")
postecode.send_keys("127549")
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(3)
payment = driver.find_element_by_id("payment_method_cheque").click()
place_order = driver.find_element_by_id("place_order").click()
check_text = WebDriverWait(driver, 20).until(
 EC.text_to_be_present_in_element((By.CLASS_NAME, "woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))
check_payment = WebDriverWait(driver, 20).until(
 EC.text_to_be_present_in_element((By.CSS_SELECTOR, "Check Payments:nth-child(2)"), "Check Payments"))
print("Все ок")
