# Whatsapp Automation
"""
This script automates WhatsApp messaging.
The message,time and the chat to which it is to be sent are stored in input_file.
Uses Chrome webdriver. can be changed .
Events are tracked into log_file.
"""
__author__  =   "Aathil"

import logging
from datetime import datetime
import json
import time
import pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# use inspect element to check if the given values have changed.
# it has been found to have changed, causing 'element not found' errors
# 'data-tab' value corresponds to the number of Tab key presses required to navigate to the element
searchbox_xpath = '//div[@contenteditable="true"][@data-tab="3"]'
input_textbox_xpath = '//div[@contenteditable="true"][@data-tab="6"]'
input_textbox_classname = '_2A8P4'
sendbutton_classname = '_1E0Oz'
sendbutton_xpath = '//button[@class="_1E0Oz"]'

webdriver_path = "chromedriver.exe"
input_file = "input.json"
log_file = 'Logs.log'


# setting up logging
# to clear the contents. Comment this out to preserve previous logs.
open(log_file, 'w').close()
logging.basicConfig(filename='.\Logs.log',
                    encoding='utf-8', level=logging.DEBUG)

# get msg list from "input.json"
with open(input_file, 'r', encoding='utf-8') as file:
    input_list = json.load(file)
    file.close()
    logging.info(f"{input_file} read successfully\n")


# Load web.whatsapp.com and authenticate
driver = webdriver.Chrome(webdriver_path)
driver.get("https://web.whatsapp.com")
logging.info("webdriver loaded")
logging.info("loaded web.whatsapp.com")
# TODO: Log here


def is_past_time(t):
    """Checks if the time is past already"""
    if t < datetime.now():
        return True
    else:
        return False


def send_message(target_chat, msg):
    """Sends msg to target_chat"""
    # locatiing chat:
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

    # sending message text:
    input_textbox = driver.find_element_by_xpath(input_textbox_xpath)
    pyperclip.copy(msg)
    input_textbox.send_keys(Keys.CONTROL+'v')
    input_textbox.send_keys(Keys.ENTER)


###############################################


for message_data in input_list:
    # message_data=[chat,msg,time]

    # convert 'time' from str to datetime-object
    message_data[2] = datetime.strptime(message_data[2], "%Y-%m-%d %H:%M:%S")
    # time check
    if is_past_time(message_data[2]) == True:
        err_str = f"Given time is in the past. Time:{message_data[2]}"
        logging.warning(err_str)
        raise ValueError(err_str)

    else:
        # wait till time reached
        while(is_past_time(message_data[2]) == False):
            pass
        send_message(message_data[0], message_data[1])
        info_str = f"Message sent. To:{message_data[0]} . Time:{message_data[2]} . Content:{message_data[1]}"
        logging.info(info_str)

driver.close()
