from .common import *

DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# Use SQLite for local development
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
