# Whatsapp Automation


# locate the chat, input text field and send the message
# iterate through all messages


from datetime import datetime
import json
import time
import pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


searchbox_xpath = '//div[@contenteditable="true"][@data-tab="3"]'
input_textbox_xpath = '//div[@tabindex="-1"]'
input_textbox_classname='_2A8P4'
webdriver_path = "chromedriver.exe"
input_file = "input.json"

def is_past_time(t):
    """Checks if the time is past already"""
    if t < datetime.now():
        return True
    else:
        return False


def send_message(target_chat, msg):
    """Sends msg to target_chat"""
    chat_xpath = f'//span[@title="{target_chat}"]'
    searchbox = WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.XPATH, searchbox_xpath))
    )
    searchbox.clear()
    pyperclip.copy(target_chat)
    searchbox.send_keys(Keys.CONTROL+'v')
    # to let search load. # TODO: try presence_of_element_located()
    time.sleep(2)
    chat = driver.find_element_by_xpath(chat_xpath)
    chat.click()
    input_textbox = driver.find_element_by_class_name(input_textbox_classname)
    pyperclip.copy(msg)
    input_textbox.send_keys(Keys.CONTROL+'v')
    input_textbox.send_keys(Keys.ENTER)
    # TODO: Log here


###############################################


# get msg list from "input.json"
with open(input_file, 'r', encoding='utf-8') as file:
    input_list = json.load(file)
    file.close()
# TODO: Log here

# Load web.whatsapp.com and authenticate
driver = webdriver.Chrome(webdriver_path)
driver.get("https://web.whatsapp.com")
# TODO: Log here


for message_data in input_list:
    # message_data=[chat,msg,time]

    # convert 'time' from str to datetime-object
    message_data[2]=datetime.strptime(message_data[2],"%Y-%m-%d %H:%M:%S")
    # wait till time reached
    if is_past_time(message_data[2]) == True:
        raise ValueError("Given time is in the past")
        # TODO: Log here
    else:
        while(is_past_time(message_data[2]) == False):
            pass
        send_message(message_data[0], message_data[1])



