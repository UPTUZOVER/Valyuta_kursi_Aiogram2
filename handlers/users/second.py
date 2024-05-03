from aiogram import types, Router, F

router_second = Router()
@router_second.message(F.text)
async def first_handler(message: types.Message):
    await message.answer(f"Hello, aaaaaaaaaaaaaaaa   a!")
















