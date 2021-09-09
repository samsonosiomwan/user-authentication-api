from .base import *
import dj_database_url


DATABASES = {
    'default': {
        **dj_database_url.parse(config('DATABASE_URL')),
        'ENGINE': 'django.db.backends.postgresql',
    }
}
