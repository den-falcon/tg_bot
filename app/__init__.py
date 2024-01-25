from aiohttp.web_app import Application
import jinja2
import aiohttp_jinja2

from app.routes import setup_routes


def setup_external_libraries(application: Application) -> None:
    aiohttp_jinja2.setup(application, loader=jinja2.FileSystemLoader("templates"))


def setup_app(application: Application) -> None:
    setup_external_libraries(application)
    setup_routes(application)


def create_app() -> Application:
    app = Application()
    setup_app(app)

    return app
