#Whatsapp Automation


#wait till time reached
#locate the chat, input text field and send the message
#iterate through all messages


import json
from selenium import webdriver

#get msg list from "input.json"
input_file="input.json"
with open(input_file,'r',encoding='utf-8') as file:
    input_list=json.load(file)
    
#Load web.whatsapp.com and authenticate
driver = webdriver.Chrome("..\\chromedriver.exe")
driver.get("https://web.whatsapp.com")



for message_item in input_list:
    #check_time(message_item)
    # send_message(message_item)