# (c) @AbirHasan2005

import os


class Config(object):
	API_ID = int(os.environ.get(1386682))
	API_HASH = os.environ.get("b71138018a6d8f4485c81f3159dcec87")
	BOT_TOKEN = os.environ.get("5005531765:AAGLP3xzRBwDGL5Cs_U1OwLf8QfjunIaL8M")
	BOT_USERNAME = os.environ.get("CC_Files_DataBase_bot")
	DB_CHANNEL = int(os.environ.get(-1001360549004))
	BOT_OWNER = int(os.environ.get(773321791))
	DATABASE_URL = os.environ.get("mongodb+srv://closeCoder:2006yillar@closecoder.lsbis.mongodb.net/CloseCoder?retryWrites=true&w=majority")
	UPDATES_CHANNEL = os.environ.get("-1001360549004", "0")
	LOG_CHANNEL = os.environ.get("LOG_CHANNEL", None)
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	ABOUT_BOT_TEXT = f"""
This is Permanent Files Store Bot!
Send me any file I will save it in my Database. Also works for channel. Add me to channel as Admin with Edit Permission, I will add Save Uploaded File in Channel & add Sharable Button Link.

🤖 **My Name:** [Files Store Bot](https://t.me/{BOT_USERNAME})

📝 **Language:** [Python3](https://www.python.org)

📚 **Library:** [Pyrogram](https://docs.pyrogram.org)

📡 **Hosted on:** [Heroku](https://heroku.com)

🧑🏻‍💻 **Developer:** @Close_Coder

👥 **Support Group:** [Linux Repositories](https://t.me/CC_Drive)

📢 **Updates Channel:** [Discovery Projects](https://t.me/projects_mine)
"""
	ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 **Developer:** @Close_Coder

Developer is Super Noob. Just Learning from Official Docs. Please Donate the developer for Keeping the Service Alive.

Also remember that developer will Delete Adult Contents from Database. So better don't Store Those Kind of Things.

[Donate Now](https://www.paypal.me/Close_Coder) (PayPal)
"""
	HOME_TEXT = """
Hi, [{}](tg://user?id={})\n\nThis is Permanent **File Store Bot**.

Send me any file I will give you a permanent Sharable Link. I Support Channel Also! Check **About Bot** Button.
"""
