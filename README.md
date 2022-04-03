# telegramMessage
Send telegram msg to anyone using bot - developed using python

Step1 - setup bot
1) set up telegram account if you dont have any
replace phone = 'YOUR_PHONE_INCLUDING_COUNTRY_CODE' with the phone number you used to create a telegram account
2) next open telegram app and search for @BotFather then click on the start button or send "/start".
3) send “/newbot” message or click on /newbot link to set up a name and a username. Username must end in "bot"
4) After setting name and username BotFather will give you an API token which is your bot token.
replace token = '<BOOT_TOKEN' with this token from BotFather


Step2 create an app on telegram
1) go to https://my.telegram.org/ - if first time it will ask you to enter phone number to which OTC will be sent.
   Note that this should be the same phone number from which you created the bot.
2) Click on Go to ‘API development tools’ and fill out the form. Telegram will give you the api_id and api_hash parameters required for starting session.
replace api_id = '<API_ID' and api_hash = '<API_HASH' with the corresponding strings you get.

Step3 run the python script
This is a very simple script with no parametrized inputs. 
- You need python3.
- You will need to install the following python libs telethon - read about it here https://pypi.org/project/Telethon/.
to Install: pip install telethon

replace user_id = '<@TELEGRAM_NAME|PHONE' with the phone or username to which message will be sent.
