from selenium import webdriver
from selenium.webdriver.common.by import By
import time
browser=webdriver.Chrome()

browser.get('https://store.steampowered.com')

time.sleep(5)

games=browser.find_element(By.XPATH, """//*[@id="store_nav_search_term"]""")
games.send_keys('Головоломки')

time.sleep(2)

button=browser.find_element(By.XPATH, """//*[@id="store_search_link"]/img""")
button.click()

time.sleep(2)

button1=browser.find_element(By.XPATH, """//*[@id="sort_by_trigger"]""")
button1.click()

time.sleep(2)

button2=browser.find_element(By.XPATH, """//*[@id="Reviews_DESC"]""")
button2.click()

time.sleep(2)

button3=browser.find_element(By.XPATH, """//*[@id="search_resultsRows"]/a[1]/div[2]/div[1]/span""")
button3.click()

time.sleep(3)

browser.close()
