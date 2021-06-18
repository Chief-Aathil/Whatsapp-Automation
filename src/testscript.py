"""
This file is to make testing easier
Features:
    -change target chat and message time of all entries in input file.
    -message time is set to offset from the current time to avoid error
"""        





import json
from json import encoder
import time
import datetime
from datetime import datetime, timedelta



file_name = 'test.json' #not using input.json, to do experiment



with open(file_name, 'r', encoding='utf-8') as file:
    output = json.load(file)
    file.close()

for index,item in enumerate(output):
    item[0]='SFA'
    offset=timedelta(minutes=index+1) # offset = 1,2,3,4,...
    item[2] = datetime.now()  # to offset from current time
    item[2] = item[2]+offset  # add offset min
    item[2] = datetime.strftime(item[2], "%Y-%m-%d %H:%M:%S")
    item[1]= "msg @ "+item[2]

json.dumps(output,indent=4)

with open('input.json','w',encoding='utf8',) as file_out:
    json.dump(output,file_out,ensure_ascii=False, indent=4)
    file_out.close()

