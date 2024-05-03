from loader import *
from data.config import *

async def start_up():
    for i in ADMINS:
        await bot.send_message(chat_id=i, text="bot ishlayapdi!")

async def shut_up():
    for i in ADMINS:
        await bot.send_message(chat_id=i, text="bot tuxtadi!")
