import asyncio

from aiogram import Bot, Dispatcher
from aiogram.types import Message

bot = Bot(token='8990916092:AAHAZPr9s4kc-BmUCDVV-DsfLDVYAxX5FTo')
dp = Dispatcher()
@dp.message()
async def message_handler(message: Message):
    if message.chat.id == 777000:
        await message.reply(
            text = "test"
        )

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    print('Бот запущен')
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выкл')