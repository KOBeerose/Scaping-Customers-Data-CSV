#importing all the necessary libaries
from re import search
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import string
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import keyboard 
import csv


# define your keyword right here:

search_sentence = "telephone"

phone_numbers = []

# defining the webdriver and config btw this code will be almost the same in all of your selenium scripts
chrome_options = webdriver.ChromeOptions()

# !!! blocking browser notifications !!!
prefs = {"profile.default_content_setting_values.notifications" : 2} 
chrome_options.add_experimental_option("prefs", prefs)

# starting in maximized window
chrome_options.add_argument("start-maximized")
chrome_options.add_argument("--disable-default-apps")
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="C:\\Users\\taha_\\Downloads\\chromedriver_win32\\chromedriver.exe")


class infine_scroll(object):
   
  def __init__(self, last):
    
    self.last = last

  def __call__(self, driver):
    new = driver.execute_script('return document.body.scrollHeight')  
    if new > self.last:
        return new
    else:
        return False

# https://camo.githubusercontent.com/cf92f585acf6b96e18ea219b5d6ed2792ffb355e65d5f4d15dabc9112ba170b9/68747470733a2f2f6b6f6d617265762e636f6d2f67687076632f3f757365726e616d653d6b6f626565726f7365266c6162656c3d50726f66696c65253230766965777326636f6c6f723d306537356236267374796c653d666c6174

driver.get("https://www.topannonces.fr/")
time.sleep(1)

print(WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="step1"]/div[3]/button[2]'))).text)

cookies_button = driver.find_element_by_xpath('//*[@id="step1"]/div[3]/button[2]')
cookies_button.click()
time.sleep(0.1)

log_icon = driver.find_element_by_xpath('/html/body/app-root/app-header/mat-toolbar/mat-toolbar-row/div[2]/button')
log_icon.click()
time.sleep(0.3)

mail_input = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/mat-dialog-container/app-loadable-modal/ngx-loadable/app-authentification/div[2]/form/mat-form-field[1]/div/div[1]/div/input')
mail_input.click()

time.sleep(0.1)
mail_input.send_keys("test@gmail.com")

login_button = driver.find_element_by_xpath('//*[@id="mat-dialog-0"]/app-loadable-modal/ngx-loadable/app-authentification/div[2]/form/button')
login_button.click()
time.sleep(0.3)

pwd_input = driver.find_element_by_xpath('//*[@id="login-pass"]')
pwd_input.send_keys("test")
time.sleep(0.1)

connect = driver.find_element_by_xpath('//*[@id="mat-dialog-0"]/app-loadable-modal/ngx-loadable/app-authentification/div[2]/form/button')
connect.click()
time.sleep(0.1)
"""
search_bar = driver.find_element_by_xpath('/html/body/app-root/app-header/mat-toolbar/mat-toolbar-row/form/input')
search_bar.click()
search_bar.send_keys(search_sentence)"""

used_button = driver.find_element_by_xpath("/html/body/app-root/main/app-home/div[1]/div[1]/ul/li[1]")
used_button.click()
time.sleep(0.5)

"""first_search = driver.find_element_by_xpath('/html/body/app-root/app-header/mat-toolbar/mat-toolbar-row/form/div/ul/li[2]/a')
first_search.click()
time.sleep(0.3)"""


scheight = 2
"""while scheight < 9.9:
    
    
    scheight += .01"""


driver.execute_script("window.scrollTo(0, document.body.scrollHeight/%s);" % scheight)
see_more = driver.find_element_by_xpath("/html/body/app-root/main/app-home/div/section/button")
see_more.click()

# driver.execute_script("document.body.style.zoom='25%'")
time.sleep(0.3)

items_urls = []
cards_links = driver.find_elements_by_xpath("//section[@class='annonces ng-star-inserted']//a")
while len(items_urls) < 5:
    cards_links = driver.find_elements_by_xpath("//section[@class='annonces ng-star-inserted']//a")
    # keyboard.press_and_release('down arrow')
    
    
    for card in cards_links:
        item_url = card.get_attribute('href')
        items_urls.append(item_url)
    cards_links = []
    print(len(items_urls))
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight/.1);")
    time.sleep(0.2)


# open the file in the write mode
header = ['full_name', 'phone_number']
f = open('customer_data.csv', 'w', encoding='UTF8', newline='')
writer = csv.writer(f)

# write the header
writer.writerow(header)

for item_url in items_urls:
    driver.get(item_url)
    time.sleep(1)
    try :
        phone_button = driver.find_element_by_xpath("//a[@class='mat-focus-indicator btn_phone mat-raised-button mat-button-base mat-primary ng-star-inserted']")
        phone_button.click()
        time.sleep(0.1)
        keyboard.press_and_release('enter')
        phone_number = driver.find_element_by_xpath("//span[@class='ng-star-inserted']").text
        name = driver.find_element_by_xpath("//body//div[@class='container product-vendor']//div//div[1]").text
        if phone_number != "Téléphone":
            # write the data
            writer.writerow([name, phone_number])
    except:
        continue
    time.sleep(1)


print("phone numbers are:")
for num in phone_numbers:
    print(num)


