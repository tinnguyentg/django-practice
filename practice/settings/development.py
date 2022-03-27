from .base import *  # noqa
from .base import INSTALLED_APPS, MIDDLEWARE

SECRET_KEY = "django-insecure-dv2q*fudqjy@lqn40h)j4bu_ag33i8mtujjxayo-6k#cema+d+"
DEBUG = True
ALLOWED_HOSTS = []

# Config django-debug-toolbar
# assert "django.contrib.staticfiles" in INSTALLED_APPS
# assert TEMPLATES[0]["APP_DIRS"]
INSTALLED_APPS += ["debug_toolbar"]
MIDDLEWARE.insert(0, "debug_toolbar.middleware.DebugToolbarMiddleware")
INTERNAL_IPS = [
    "127.0.0.1",
]
