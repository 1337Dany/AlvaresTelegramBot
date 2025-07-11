from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("TOKEN")

class MyBot:
    bot = Bot(token=TOKEN)
    dispatcher = Dispatcher()

bs = MyBot()