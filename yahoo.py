from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

BASE_URL = 'https://answers.yahoo.com'

def search(q):
    driver = webdriver.Firefox()
    answer = None
    try:
        driver.get(BASE_URL)
        input = driver.find_element_by_id('UHSearchBox')
        input.clear()
        input.send_keys(q)
        input.send_keys(Keys.RETURN)
        WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located((By.CSS_SELECTOR, '.first .AnswrsV2 a')))
        result = driver.find_element_by_css_selector('.first .AnswrsV2 a')
        driver.get(result.get_attribute('href'))
        WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located((By.CSS_SELECTOR, '#ya-best-answer')))
        answer = driver.find_element_by_css_selector('#ya-best-answer .ya-q-full-text')
        answer = answer.text
    except:
        pass
    driver.quit()
    return answer
