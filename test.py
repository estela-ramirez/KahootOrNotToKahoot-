import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup

os.environ['PATH'] += r'C:\sel'
url = 'https://kahoot.it/'

# the options keeps the tab open else it will close quickly
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_options=options)
#get curr html
driver.get(url)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# enter game pin 
time.sleep(5)
pin = 1049787
form_pin =  driver.find_element_by_name('gameId')
form_pin.send_keys(pin)

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
user_name = 'user name_here'
form_nickname = driver.find_element_by_name('nickname')
print(form_nickname)
form_nickname.send_keys(user_name)

#click submit name button
but_entername = driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div[3]/div[2]/main/div/form/button')
but_entername.click()

#wait for game start url must equal https://kahoot.it/gameblock
current_url = driver.current_url
WebDriverWait(driver, 15).until(EC.url_contains('gameblock'))
new_url = driver.current_url
print(new_url)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
#this is just to check html in txt file
with open('html.txt', 'w') as f:
    f.write(html)
# close web browser
#driver.close()