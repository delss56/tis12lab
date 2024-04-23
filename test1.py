from selenium import webdriver
from selenium.webdriver.common.by import By
import time
browser=webdriver.Chrome()

browser.get('https://store.steampowered.com')

time.sleep(5)

game=browser.find_element(By.XPATH, """//*[@id="store_nav_search_term"]""")
game.send_keys('Terraria')

time.sleep(2)

button=browser.find_element(By.XPATH, """//*[@id="search_suggestion_contents"]/a[1]/div[1]""")
button.click()

time.sleep(3)

browser.close()
