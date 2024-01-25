from aiogram import Bot, Router
from aiogram.filters import Command
from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    MenuButtonWebApp,
    Message,
    WebAppInfo,
)

router = Router()


@router.message(Command("start"))
async def command_start(message: Message, bot: Bot, base_url: str):
    await bot.set_chat_menu_button(
        chat_id=message.chat.id,
        menu_button=MenuButtonWebApp(text="App", web_app=WebAppInfo(url=f"{base_url}/")),
    )
    await message.answer("""Привет!\nОтправь мне /webview чтобы получить ссылку на приложение.""")


@router.message(Command("webview"))
async def command_webview(message: Message, base_url: str):
    await message.answer(
        "Отлично! Вот твоя кнопка для приложения.",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text="Открыть WebApp", web_app=WebAppInfo(url=f"{base_url}/")
                    )
                ]
            ]
        ),
    )
