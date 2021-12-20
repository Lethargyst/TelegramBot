#!venv/bin/python
import logging
from os import getenv
from tokens import *
from textRecognition import get_analysed
from aiogram import Bot, Dispatcher, executor, types

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands='start')
async def start_process(message: types.Message):
    await message.answer(
        'Зравствуй! Я бот, проводящий морфологический анализ текста на русском языке. '
        'Напиши мне что-нибудь, а я постараюсь провести анализ.')


@dp.message_handler()
async def analyse(message: types.Message):
    await message.reply('Вот, что у меня получилось:\n' + get_analysed(message.text))


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
