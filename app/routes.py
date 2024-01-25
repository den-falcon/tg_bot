from app import views


def setup_routes(application):
    application.router.add_get("/", views.index)
