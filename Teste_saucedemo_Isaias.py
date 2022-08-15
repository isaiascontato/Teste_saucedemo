from http.server import executable
from sys import maxsize
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Chrome()



#Acessar https://www.saucedemo.com

browser.maximize_window()

browser.get("https://www.saucedemo.com/")

#login

name = browser.find_element(By.ID , "user-name")
name.send_keys("standard_user")

password = browser.find_element(By.ID,"password")
password.send_keys("secret_sauce")

botton = browser.find_element(By.ID,"login-button")
botton.submit()

#Ordenação

select_low_to_high = browser.find_element(By.XPATH, "//span/select/option[3]")
select_low_to_high.click()

#Seleção de produtos

product_1 = browser.find_element(By.ID,"add-to-cart-sauce-labs-onesie")
product_1.click()

product_2 = browser.find_element(By.ID,"add-to-cart-test.allthethings()-t-shirt-(red)")
product_2.click()

#Carrinho de Compras

browser.get("https://www.saucedemo.com/cart.html")

#Concluir compra

checkout = browser.find_element(By.ID , "checkout")
checkout.click()

my_first_name = browser.find_element(By.ID , "first-name")
my_first_name.send_keys("ISAIAS")

my_last_name = browser.find_element(By.ID , "last-name")
my_last_name.send_keys("GOULARTE")

zip_code = browser.find_element(By.ID , "postal-code")
zip_code.send_keys("38400-000")

button_continue = browser.find_element(By.ID ,"continue")
button_continue.submit()

finish = browser.find_element(By.ID ,"finish")
finish.click()

browser.close()