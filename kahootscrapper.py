import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
import random

#intilazing params
os.environ['PATH'] += r'C:\sel'
url = 'https://kahoot.it/'
options = webdriver.ChromeOptions()

# intlizing user inputs
# pin = 7694894
# user_name = 'user name_  _here'

# creating helper functions
def setup_game(pin, user_name):
    # the options keeps the tab open else it will close quickly
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(chrome_options=options)
    #get curr html
    driver.get(url)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    time.sleep(5)
    # re assign game pin and user name here TODO: add params in this function
    
    #
    driver = gamepin_and_clicksubmit(pin, user_name, driver)
    #
    
    #wait for game start url must equal https://kahoot.it/gameblock
    
    WebDriverWait(driver, 100).until(EC.url_contains('gameblock'))
    new_url = driver.current_url
    print(new_url)
    return driver
# add in game pin and user name
def gamepin_and_clicksubmit(discord_gamepin, discord_username, driver):
    form_pin =  driver.find_element_by_name('gameId')
    form_pin.send_keys(discord_gamepin)
    current_url = driver.current_url

    #click button to enter pin
    but_entergame = driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div[3]/div[2]/main/div/form/button')
    but_entergame.click()

    #wait for redirect to kahot.join
    WebDriverWait(driver, 15).until(EC.url_changes(current_url))
    new_url = driver.current_url
    print(new_url)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    
    #new loaded page has been parsed
    #enter name

    form_nickname = driver.find_element_by_name('nickname')
    print(form_nickname)
    form_nickname.send_keys(discord_username)

    #click submit name button
    #TODO: when an entered name is already taken deal with that issue

    but_entername = driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div[3]/div[2]/main/div/form/button')
    but_entername.click()

    return driver

def question_type():
    pass
def deal_with_naming_error():
    pass
   
def make_selection(driver):
    
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    #Interesting things 
    #take in number of quiz questions
    #multiple choice questions are indexed starting at 0
    #multiple types
    #multiple opinion types

    # Get all the elements available with tag name

    elements = driver.find_elements(By.TAG_NAME, 'button')
    print (elements)
    random_selection = random.randint(0, len(elements) - 1)
    print('\n this is the random in\n ')
    print (random_selection)

    for e in range(len(elements)):
        
        if e == random_selection:
            choice = elements[e]
            choice.click()
            print('selection has been made')
    pass