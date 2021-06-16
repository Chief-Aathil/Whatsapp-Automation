import json
import time
import datetime
from datetime import datetime


# print("Hello world")
# time.sleep(3)
print("Started")
x = ['chat1', 'msg1', 't1']
y = ['chat2', 'msg2', 't2']
list = []
list.append(x)
list.append(y)
# print(list)
print(json.dumps(list, indent=4))

file_name = 'test.json'

# with open( file_name,'w', encoding='utf-8') as file:
#     json.dump(list,file,ensure_ascii=False,indent=4)
#     file.close()

with open(file_name, 'r', encoding='utf-8') as file:
    output = json.load(file)
    # json.dumps(output)
    # print(json.dumps(output))
    print(output)
    file.close()

# output.append('2')
# print('here')
# print(json.dumps(output,indent=2))
# print(output[1])

for item in output:
    x=datetime.strptime(item[2],"%Y-%m-%d %H:%M:%S")
    print(x)
    print(x.month)