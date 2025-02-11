import os
from pathlib import Path
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

<<<<<<< HEAD
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
=======
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY', 'your_default_secret_key')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False  # Desactiva el modo debug

ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'your-app-name.onrender.com']  # Agrega el dominio de tu aplicación en producción

# Application definition
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'votaciones',
    }
}
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

<<<<<<< HEAD
=======
# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.config(default=os.getenv('DATABASE_URL'))  # Utiliza dj-database-url para manejar la base de datos
}

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

>>>>>>> 90758a2dfc6e526e05c8008fb64216e84eac2893
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

<<<<<<< HEAD
=======
# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

>>>>>>> 90758a2dfc6e526e05c8008fb64216e84eac2893
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True
<<<<<<< HEAD
=======

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = '/static/'

# En producción, configura STATIC_ROOT
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# También puedes incluir más directorios estáticos si es necesario
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

MEDIA_URL = '/media/'  # URL base para acceder a los archivos de medios
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

>>>>>>> 90758a2dfc6e526e05c8008fb64216e84eac2893
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Logs de errores
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'errors.log'),
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}
