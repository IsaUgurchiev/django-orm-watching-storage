from dotenv import load_dotenv
from environs import Env

load_dotenv()
env = Env()
env.read_env()

import os

DATABASES = {
    'default': {
        'ENGINE': os.getenv("DJANGO_DATABASE_ENGINE"),
        'HOST': os.getenv("DJANGO_DATABASE_HOST"),
        'PORT': os.getenv("DJANGO_DATABASE_PORT"),
        'NAME': os.getenv("DJANGO_DATABASE_NAME"),
        'USER': os.getenv("DJANGO_DATABASE_USER"),
        'PASSWORD': os.getenv("DJANGO_DATABASE_PASSWORD"),
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = os.getenv("SECRET_KEY")

DEBUG = env("DEBUG", True)

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


USE_L10N = os.getenv("USE_L10N")

LANGUAGE_CODE = os.getenv("LANGUAGE_CODE")

TIME_ZONE = os.getenv("TIME_ZONE")

USE_TZ = os.getenv("USE_TZ")

