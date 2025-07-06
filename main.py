from aiogram import Bot, Dispatcher, types
import asyncio
from random import randint
import importlib
import os
# from dotenv import load_dotenv
# load_dotenv()
# Token = os.getenv("BOT_TOKEN")
Token = '7993379076:AAHqS0qvQPLdesm3r4BWa1lBoZYiQPH1oT8'

channel = ''
bot = Bot(token=Token)
dp = Dispatcher()

user_data = {}
project_dir = os.path.dirname(os.path.abspath(__file__))
images_dir = os.path.join(project_dir, 'images')

@dp.message()
async def handle_message(message: types.Message):
    user_id = message.from_user.id
    if message.text == '/start':
        await start(message)
    if message.text == '/contact' or message.text == 'Контакты':
        await contact(message)
    if message.text == '/projects' or message.text == 'Проекты':
        await projects(message)
    if message.text == '/about' or message.text == 'Обо мне':
        await about(message)


async def start(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id] = {}
    btn = [
        [
            types.KeyboardButton(text='Контакты'),
            types.KeyboardButton(text='Проекты'),
        ],
        [types.KeyboardButton(text='Обо мне')]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=btn, resize_keyboard=True)
    await message.answer(f'Привет! Я — Назо, и это мой бот-портфолио.\n'
                         f'Здесь ты можешь узнать немного больше обо мне,'
                         f'моих увлечениях, целях и проектах.', reply_markup=keyboard)


async def contact(message: types.Message):
    user_id = message.from_user.id
    await message.answer(f'email: bahromavaa@gmail.com\n'
                         f'tg: @nazoob')


async def projects(message: types.Message):
    user_id = message.from_user.id
    photo_dir = os.path.join(images_dir, 'mitti.jpeg')
    media = types.InputMediaPhoto(
        media=types.FSInputFile(photo_dir),
        caption='В рамках команды проекта Mittivoyim (AI-powered parenting & nutrition PWA),\n'
                'я занималась backend-разработкой с использованием Django.'
    )
    await message.answer_media_group([media])

async def about(message: types.Message):
    user_id = message.from_user.id
    await message.answer(f'Меня зовут Назокат, родилась в 2007 году.\n'
                         f'Я — Data Scientist и ML-инженер, специализируюсь на создании моделей машинного обучения на Python.\n'
                         f'Имею опыт работы с Django для разработки backend.\n'
                         f'Также умею создавать Telegram-ботов и автоматизировать задачи с помощью Python.')


async def main():
    await dp.start_polling(bot)


asyncio.run(main())
