import time
import pyperclip
from functools import singledispatch
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("chromedriver.exe")

driver.get("https://web.whatsapp.com")

message_text = "Test message"
receipent = "WA test"
message_count = 1
textbox_classname = '_2A8P4'  # classname of textbox obtained from inspecting Elements
sendbutton_classname = '_1E0Oz'  # classname of sendbutton
searchbox_xpath='//div[@contenteditable="true"][@data-tab="3"]' #classname of searchbox
chat_xpath=f'//span[@title="{receipent}"]'

def msg():
    #find searchbox
    searchbox = WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.XPATH,searchbox_xpath))
    )
    searchbox.clear()
    time.sleep(2)
    pyperclip.copy(receipent)
    searchbox.send_keys(Keys.CONTROL+'v')
    time.sleep(2)

    # find the receipent
    chat=driver.find_element_by_xpath(chat_xpath)
    chat.click()
    # user = driver.find_element_by_xpath(
    #     '//span[@title = "{}"]'.format(receipent))
    # user.click()
    text_box = driver.find_element_by_class_name(textbox_classname)
    
    #Sending
    for i in range(message_count):
       text_box.send_keys(message_text)
       driver.find_element_by_class_name(sendbutton_classname).click()

#time.sleep(20)

msg()
driver.close()