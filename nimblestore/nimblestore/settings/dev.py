from .base import *

SECRET_KEY = "django-insecure-=li(=f0m230@nagulg7&=+10xpno51!!r#i7&tj4amhn#4%(e1"
DEBUG = True
ALLOWED_HOSTS = ['*']

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}
