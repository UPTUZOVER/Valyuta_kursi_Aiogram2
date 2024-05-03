from aiogram import Bot, Dispatcher, types
from data.config import BOT_TOKEN

# Create the Bot object with DefaultBotProperties
bot = Bot(token=BOT_TOKEN,parse_mode='HTML')
dp = Dispatcher()
