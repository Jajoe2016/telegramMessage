from telethon import TelegramClient, sync

api_id = '<API_ID'
api_hash = '<API_HASH'
token = '<BOOT_TOKEN'
phone = 'YOUR_PHONE_INCLUDING_COUNTRY_CODE' #this is needed for first time authorization - commneted below


# run the below commented section for first time if telegram-send is not authorized
# client = TelegramClient('session', api_id, api_hash)
# client.connect()
# if not client.is_user_authorized():
#     client.send_code_request(phone)
#     client.sign_in(phone,input('Enter the code: '))
# client.disconnect()



# Send Message
user_id = '<@TELEGRAM_NAME|PHONE'  #this is the user to which message is sent
message_content = 'Hi this is test message from my telegram bot'
client = TelegramClient('session', api_id, api_hash)
client.start()
try:
    client.send_message(user_id , message_content)
except Exception as e:
    print(e)
