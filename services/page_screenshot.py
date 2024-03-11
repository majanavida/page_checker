import shutil
import os
from environs import Env
from screenshotone import Client, TakeOptions
from aiogram.types import Message, FSInputFile


async def take_screenshot(message: Message, path: str | None = None):
    # try:
    env = Env()
    env.read_env(path)
    name = f'{message.text.split('.')[1]}.{message.text.split('.')[2]}.png'
    client = Client(access_key=env('SCREENSHOT_ACCESS'), 
                    secret_key=env('SCREENSHOT_SECRET'))
    options = (TakeOptions.url(f'{message.text}')
            .format('png')
            .viewport_width(1024)
            .viewport_height(768)
            .block_cookie_banners(True)
            .block_chats(True))
    image = client.take(options)
    with open(f'{name}', 'wb') as file:
        shutil.copyfileobj(image, file)
        await message.answer_photo(FSInputFile(
            path='{filename}', caption=f'Скриншот страницы {message.text}'
        ))
    # except FileNotFoundError:
    #     await message.answer('Что-то пошло не так... Попробуйте снова')
    # os.remove(f'{name}')