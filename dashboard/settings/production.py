import dj_database_url
from .common import *

DEBUG = False
ALLOWED_HOSTS = ['your_production_domain.com']

# Use PostgreSQL for production
DATABASES = {
    'default': dj_database_url.config(default=os.getenv('DJANGO_DATABASE_URL'))
}
