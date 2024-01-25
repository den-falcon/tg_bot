from aiohttp.web_app import Application
from aiogram import Bot, Dispatcher
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from aiogram.types import MenuButtonWebApp, WebAppInfo

from app import create_app
from app.handlers import router

TOKEN = "5718260789:AAGK8wFPs8t5GSdocmsuqoD7nRAA9PMGreI"
APP_BASE_URL = "https://4a9e-185-53-230-255.ngrok-free.app"
DB_PASS = "03uXao55IUtaX2Iv"


async def on_startup(bot: Bot, base_url: str):
    await bot.set_webhook(f"{base_url}/webhook")
    await bot.set_chat_menu_button(
        menu_button=MenuButtonWebApp(
            text="App", web_app=WebAppInfo(url=f"{base_url}/")
        )
    )


def main() -> Application:
    bot = Bot(token=TOKEN, parse_mode="HTML")
    dispatcher = Dispatcher()
    dispatcher["base_url"] = APP_BASE_URL
    dispatcher.startup.register(on_startup)

    dispatcher.include_router(router)

    app = create_app()
    app["bot"] = bot

    SimpleRequestHandler(
        dispatcher=dispatcher,
        bot=bot,
    ).register(app, path="/webhook")
    setup_application(app, dispatcher, bot=bot)

    return app


app = main()
