import os
from environs import Env
from dotenv import load_dotenv

load_dotenv()
env = Env()
env.read_env() # reading .env file

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")

DATABASES = {
    'default': {
        'ENGINE': os.getenv("DB_ENGINE"),
        'HOST': os.getenv("DB_HOST"),
        'PORT': os.getenv("DB_PORT"),
        'NAME': os.getenv("DB_NAME"),
        'USER': os.getenv("DB_DATABASES_USER"),
        'PASSWORD': os.getenv("DB_PASSWORD"),
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
