from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium ожидать значения цены дома в 100 долларов

wait1 = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
#Как только цена опустилась кликаем кнопку Book
#if wait1:
buttonbook = browser.find_element_by_id("book")
buttonbook.click()

#Считываем значение x
x_element = browser.find_element_by_id("input_value")
x = int(x_element.text)

#Считаем ответ
answer = browser.find_element_by_id("answer")

#Вводим данные в поле ответа
answer.send_keys(calc(x))

#Ищем кнопку Submit и нажимаем ее
button2 = browser.find_element_by_id("solve")
button2.click()

time.sleep(10)
browser.quit()

