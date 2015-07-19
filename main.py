from time import sleep
from log_in import vk_log_in

vk = vk_log_in ()

MY_ID = '19943918' #Your id (only for Aim search)
USER_ID = 'ALL' #Aim ID OR 'ALL'

AIM_SEARCH = USER_ID != 'ALL'

DEBUG = False #|| True

output = open ('data\my_messages_with_' + USER_ID + '.txt', 'w', encoding='utf-8')

COUNT = 200

size = COUNT
i = 0
while i < size:
    if AIM_SEARCH: result = vk.messages.getHistory (offset=i, count=min(COUNT, size - i), user_id=USER_ID)
    else:          result = vk.messages.get        (out=1, offset=i, count=min(COUNT, size - i), time_offset=0, filters=0)

    if DEBUG: print(result)

    size = result['count']
    result = result['items']

    if DEBUG: print(result)

    for message in result:
        if (not AIM_SEARCH) or (message['from_id'] == int(MY_ID)): #lazy hack
            text = message['body']
            output.write(message['body'] + '\n')

    i += COUNT

    sleep(0.3) #Fucking time limit

    print((str)((int)(i / size * 100)) + '% done')

    if DEBUG: input("Press Enter to continue...")

print(str(size) + ' items processed')

output.close()
