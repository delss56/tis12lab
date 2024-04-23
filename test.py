from selenium import webdriver
from selenium.webdriver.common.by import By
import time
browser=webdriver.Chrome()

browser.get('https://store.steampowered.com/login')

time.sleep(8)

username=browser.find_element(By.XPATH, """//*[@id="responsive_page_template_content"]/div[3]/div[1]/div/div/div/div[2]/div/form/div[1]/input""")
username.send_keys('example123')

password=browser.find_element(By.XPATH, """//*[@id="responsive_page_template_content"]/div[3]/div[1]/div/div/div/div[2]/div/form/div[2]/input""")
password.send_keys('321elpmaxe')

button=browser.find_element(By.XPATH, """//*[@id="responsive_page_template_content"]/div[3]/div[1]/div/div/div/div[2]/div/form/div[4]/button""")
button.click()

time.sleep(3)

browser.close()
