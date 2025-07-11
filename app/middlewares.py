from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, Message
from typing import Callable, Dict, Any, Awaitable

#Here middleware handles every message that user writes to chat and saves it to log file
class TestMiddleware(BaseMiddleware):
    async def __call__(self,
                       handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
                       event: TelegramObject,
                       data: Dict[str, Any]) -> Any:

        if isinstance(event, Message):
            user_id = event.from_user.id
            text = event.text

        else:
            print(f"[Middleware] Unknown event type: {type(event)}")

        result = await handler(event, data)

        print("[Middleware] Middleware triggered")
        return result
