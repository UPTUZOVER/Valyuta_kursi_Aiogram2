from aiogram import types, Router, F

router_first = Router()
@router_first.message(F.text)
async def first_handler(message: types.Message):
    await message.answer(f"Hello, what is your name!")
















