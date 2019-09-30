from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math


link = "http://suninjuly.github.io/selects1.html"

try:
	browser = webdriver.Chrome()
	browser.get(link)
	
	#Считываем значение для переменной x
	x_element = browser.find_element_by_id("num1")#сюда подставить селектор со страницы
	x = int(x_element.text)
	#Считываем значение для переменной y
	y_element = browser.find_element_by_id("num2")
	y = int(y_element.text)
	#Считаем ответ суммы
	answer = str(x+y)

	#Находим select (список) и подставляем значение, вычисленное выше
	select = Select(browser.find_element_by_tag_name("select"))
	select.select_by_value(answer)#сюда вставить ответ выборки текста



	#Ищем кнопку и нажимаем ее
	button = browser.find_element_by_css_selector(".btn")
	button.click()

finally:
	time.sleep(30)
	browser.quit()
