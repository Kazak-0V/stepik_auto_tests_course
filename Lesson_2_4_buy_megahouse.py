from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    browser.find_element(By.ID, "book").click()

    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "input_value"))
    )
    time.sleep(0.5)

    x = browser.find_element(By.ID, "input_value").text.strip()
    print("x =", repr(x))

    y = calc(x)
    print("y =", y)

    input_answer = browser.find_element(By.ID, "answer")
    input_answer.clear()
    input_answer.send_keys(y)

    submit = browser.find_element(By.XPATH, "//button[text()='Submit']")
    print("Кнопка:", repr(submit.text))
    browser.execute_script("arguments[0].scrollIntoView(true);", submit)
    time.sleep(0.3)
    submit.click()

    time.sleep(1)

finally:
    time.sleep(30)
    browser.quit()