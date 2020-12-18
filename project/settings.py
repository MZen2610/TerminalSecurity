import os
from environs import Env

env = Env()
env.read_env()  # reading .env file

SECRET_KEY = env("DJANGO_SECRET_KEY")

DATABASES = {
    'default': {
        'ENGINE': env("DB_ENGINE"),
        'HOST': env("DB_HOST"),
        'PORT': env("DB_PORT"),
        'NAME': env("DB_NAME"),
        'USER': env("DB_DATABASES_USER"),
        'PASSWORD': env("DB_PASSWORD"),
    }
}

INSTALLED_APPS = ['datacenter']

DEBUG = env.bool("DJANGO_DEBUG", default=False)

ROOT_URLCONF = "project.urls"

ALLOWED_HOSTS = ['*']

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]

USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True
