import os

from aiogram import Router, F
from aiogram.types import Message, FSInputFile
from aiogram.filters import Command, CommandStart
from lexicon.lexicon import LEXICON_RU
from services.page_screenshot import take_screenshot
from filters.is_link import IsLink

import pyppeteer


router = Router()


@router.message(CommandStart())
async def proccess_command_start(message: Message):
    await message.answer(text=LEXICON_RU['/start'])
    
    
@router.message(Command(commands=['help']))
async def process_command_help(message: Message):
    await message.answer(text=LEXICON_RU['/help'])
    
    
@router.message(IsLink())
async def process_screenshot(message: Message):
    filename = 'temp.png'
    await message.answer(text=LEXICON_RU['start_download'])
    browser = await pyppeteer.launch()
    page = await browser.newPage()
    await page.goto(url=message.text)
    await page.setViewport(dict(width=1024, height=768))
    await page.screenshot({'path': filename})
    await browser.close()
    photo = FSInputFile(path=filename)
    await message.answer_photo(photo=photo, 
                               caption=f'Скриншот страницы {message.text}')
    os.remove(filename)
    
    