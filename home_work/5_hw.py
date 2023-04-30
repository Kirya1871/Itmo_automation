from selenium import webdriver
def find_elements():
    driver = webdriver.Chrome()
    driver.get ("https://www.saucedemo.com/")

    username = driver.find_element_by_id("user-name")
    driver.find_element(By.CSS_SELECTOR,"user-name")
    password = driver.find_element_by_id("password")
    driver.find_element(By.CSS_SELECTOR, "password")
    submit.button = driver.find_element_by_id('login-button')
    driver.find_element(By.CSS_SELECTOR, "login-button")

    if username and password and submit.button:
        print("элемент найден")
    else:
        print("элемент не найден")


find_elements()