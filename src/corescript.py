# Whatsapp Automation


# wait till time reached
# locate the chat, input text field and send the message
# iterate through all messages


from datetime import datetime
import json
from selenium import webdriver

# get msg list from "input.json"
input_file = "input.json"
with open(input_file, 'r', encoding='utf-8') as file:
    input_list = json.load(file)
# TODO: Log here

# Load web.whatsapp.com and authenticate
driver = webdriver.Chrome("..\\chromedriver.exe")
driver.get("https://web.whatsapp.com")
# TODO: Log here

def is_past_time(t):
    if t < datetime.now():
        return True
    else:
        return False


for message_item in input_list:
    # message_time=[chat,msg,time]
    if is_past_time(message_item[2]) == True:
        raise ValueError("Given time is in the past")
        # TODO: Log here
    else:
        while(is_past_time(message_item[2])==False):
            pass
        
        # send_message(message_item)
