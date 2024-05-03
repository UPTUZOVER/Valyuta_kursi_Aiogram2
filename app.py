from loader import bot, dp
from utills.notify import *
from utills.set_bot import *
import asyncio
import handlers
from handlers.users.first import router_first
from handlers.users.second import router_second
async def main():
    dp.startup.register(start_up)
    dp.shutdown.register(shut_up)
    dp.include_routers(router_first, router_second)
    await bot.set_my_commands(commands=commands)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session().close()

if __name__ == '__main__':
    asyncio.run(main())






































