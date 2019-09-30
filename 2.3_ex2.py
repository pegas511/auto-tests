from selenium import webdriver
import time
import math

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"
browser.get(link)

#Ищем кнопку и нажимаем ее
button1 = browser.find_element_by_css_selector(".btn")
button1.click()

#Подтверждаем действия на странице
confirm = browser.switch_to.alert
confirm.accept()

#Считываем значение x
x_element = browser.find_element_by_id("input_value")
x = int(x_element.text)

#Считаем ответ
answer = browser.find_element_by_id("answer")

#Вводим данные в поле ответа
answer.send_keys(calc(x))

#Ищем кнопку и нажимаем ее
button2 = browser.find_element_by_css_selector(".btn")
button2.click()
