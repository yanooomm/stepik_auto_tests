import pytest
import time

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver

# импортируем класс By, который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By

def test_run_browser():
    # инициализируем драйвер браузера, открываем браузер
    driver = webdriver.Chrome()
    time.sleep(5)

    # открываем окно по указанной ссылке
    driver.get("https://suninjuly.github.io/text_input_task.html")
    time.sleep(5)

    # ищем элемент по указанному способу и значению
    textarea = driver.find_element(By.CSS_SELECTOR, ".textarea")
    # пишем текст ответа в найденное поле
    textarea.send_keys("get()")
    time.sleep(5)

    # найдем кнопку 
    submit_button = driver.find_element(By.CSS_SELECTOR, ".submit-submission")
    # нажмем на кнопку
    submit_button.click()
    time.sleep(5)

    # закрываем окно браузера
    driver.quit()