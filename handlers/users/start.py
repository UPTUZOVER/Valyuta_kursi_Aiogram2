from aiogram.filters import *
from loader import *
from aiogram import types
from handlers.users import *
@dp.message(CommandStart())
async def start(message: types.Message):
    #await message.answer(message.json())
    await message.answer(f"Hello, {message.from_user.first_name}!")


@dp.message(Command('help'))
async def help_command(message: types.Message):
    await message.answer("This is the help message. Here's what you can do:\n"
                         "/start - Restart the bot\n"
                         "/help - Get help")