import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Configuración de archivos estáticos para desarrollo y producción
STATIC_URL = '/static/'

# Directorio donde se guardarán los archivos estáticos en producción
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

# Directorios adicionales para archivos estáticos en desarrollo
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    'C:/aplicaciones-web/Apli/Mesa/ProVotacion/static',  # Ajusta si es necesario
]

# Configuración de medios (archivos subidos por los usuarios)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Configuración para la base de datos
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'votaciones',
    }
}

# Seguridad: Permitir solo ciertos hosts en producción
ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'tu_dominio.com']

# Otras configuraciones (por ejemplo, contraseñas y validaciones de seguridad)
SECRET_KEY = 'django-insecure-d-m-l4tj+)!z)0#eysno$ck^-%bl7%yld$hwgn^49rh!u+n(!9'
DEBUG = True
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Aplicaciones.Electoral',
]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
ROOT_URLCONF = 'Mesa.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Mesa.wsgi.application'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
