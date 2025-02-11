import os
from pathlib import Path
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

# Configuración de archivos estáticos para desarrollo y producción
STATIC_URL = '/static/'

# En producción, configura STATIC_ROOT
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Directorios adicionales para archivos estáticos en desarrollo
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    # 'C:/aplicaciones-web/Apli/Mesa/ProVotacion/static',  # Ajusta si es necesario
]

# Configuración de medios (archivos subidos por los usuarios)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Seguridad: Permitir solo ciertos hosts en producción
ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'your-app-name.onrender.com']  # Cambia 'your-app-name' por tu dominio

# Configuración para la base de datos
DATABASES = {
    'default': dj_database_url.config(default=os.getenv('DATABASE_URL'))  # Utiliza dj-database-url para manejar la base de datos
}

# Otras configuraciones (por ejemplo, contraseñas y validaciones de seguridad)
SECRET_KEY = os.getenv('SECRET_KEY', 'your_default_secret_key')  # Asegúrate de configurar la variable de entorno SECRET_KEY
DEBUG = False  # Desactiva el modo debug en producción

# Password validation
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

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

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
