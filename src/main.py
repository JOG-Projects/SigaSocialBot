from cmath import e
import pyautogui
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def main(driver):
    driver.get("http://sigasocial.com.br")
    
    login(driver)

    open_extension_tab(driver)

    XPATH_AGREE_EXTENSION = "/html/body/center/div/div/form/div/label[2]/input"
    get_element_by_xpath(driver, XPATH_AGREE_EXTENSION)

    agree_checkbox = get_element_by_xpath(driver,  XPATH_AGREE_EXTENSION)
    agree_checkbox.click()

    add_conta(driver, get_contas()[5])
    # adicionar_contas(driver)

    driver.quit()

def adicionar_contas(driver):
    for conta in get_contas():
        add_conta(driver, conta)

def add_conta(driver, conta):
    driver.get("https://www.instagram.com/accounts/edit/")

    XPATH_USER_INSTAGRAM = "/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[1]/div/label/input"
    input_login = get_element_by_xpath(driver, XPATH_USER_INSTAGRAM)
    input_login.send_keys(conta[0])

    XPATH_PASSWORD_INSTAGRAM = "/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[2]/div/label/input"
    input_password = get_element_by_xpath(driver, XPATH_PASSWORD_INSTAGRAM)
    input_password.send_keys(conta[1])

    while True:
        try:
            gozar_nas_calcas(driver)
            break
        except:
            pass

    # sexo_games(driver)

    pyautogui.alert()

def gozar_nas_calcas(driver):
    pyautogui.click("data\\extensions.png")
    time.sleep(1)
    pyautogui.click("data\\siga_social_extension_icon.png")
    time.sleep(1)
    pyautogui.click("data\\add_profile.png")
    time.sleep(1)
    XPATH_SLIDER_ACOES = "/html/body/div[2]/div[2]/div[1]/div/div/div/div[2]/div/div/div[2]/div/input"
    slider_acoes = get_element_by_xpath(driver, XPATH_SLIDER_ACOES)
    driver.execute_script("arguments[0].setAttribute('value', arguments[1])", slider_acoes, 7)

def sexo_games(driver):
    time.sleep(2)
    print("abrindo extensao")
    open_extension_tab(driver)
    time.sleep(10)
    click_add_profile(driver)
    driver.switch_to.window(driver.window_handles[-1])

    time.sleep(2)
    print("movendo slider")

def click_add_profile(driver):
    XPATH_ADD_ACCOUNT = "/html/body/center/div/a"
    add_account_button = get_element_by_xpath(driver, XPATH_ADD_ACCOUNT)
    add_account_button.click()

def get_contas():
    with open('contas.txt') as f:
        lines = f.readlines()

    contas = [l.split(" ") for l in lines]
    return contas

def open_extension_tab(driver):
    driver.get("chrome-extension://pkhnfifgabjphjbbmamiodhdmajceeen/scripts/popup.html")

def get_element_by_xpath(driver, xpath):
    ec = EC.presence_of_element_located((By.XPATH, xpath))
    return WebDriverWait(driver, 3).until(ec)

def login(driver):
    ec = EC.presence_of_element_located((By.XPATH, "/html/body/nav/div[2]/ul[2]/li[2]/a/img"))
    alert_login()
    try:
        WebDriverWait(driver, 300).until(ec)
    except:
        alert_login()
        login(driver, ec)

def alert_login():
    return pyautogui.alert("Voce precisa logar!!!")

def init_driver():
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_extension("data\siga_social_extensao.crx")

    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    driver = init_driver()
    main(driver)
except e:
    print(e)
    pyautogui.alert("fechar")
    driver.quit()