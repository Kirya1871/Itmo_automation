from selenium import webdriver
def find_elements():
    driver = webdriver.Chrome()
    driver.get ("https://www.saucedemo.com/")

    username = driver.find_element_by_id("user-name")
    password = driver.find_element_by_id("password")
    submit.button = driver.find_element_by_id("login-button")

    if username and password and submit.button:
        print("ok")
    else:
        print("no")