from telethon import TelegramClient, sync

api_id = '12142448'
api_hash = '818c9a779c3158fd998744bd3eb45d7a'
token = '5177616376:AAFctPDdBKKEycIofFR4weCz-D436mcIF4U'
message = 'Hi this is test bot from Yohannes'
phone = '+15105427747'



# run the below commented section for first time if telegram-send is not authorized
# client = TelegramClient('session', api_id, api_hash)
# client.connect()
# if not client.is_user_authorized():
#     client.send_code_request(phone)
#     client.sign_in(phone,input('Enter the code: '))
# client.disconnect()




user_id = '+251967731813'
message_content = 'ok'
client = TelegramClient('session', api_id, api_hash)
client.start()
try:
    client.send_message(user_id , message_content)
except Exception as e:
    print(e)
