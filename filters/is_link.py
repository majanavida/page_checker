from aiogram.filters import Filter
from aiogram.types import Message


class IsLink(Filter):
    async def __call__(self, message: Message) -> bool:
        return (True if message.text.startswith == 'http://' or 'https://'
                else False)