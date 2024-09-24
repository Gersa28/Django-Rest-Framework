"""
Django settings for _projectdoctor project.

Generated by 'django-admin startproject' using Django 5.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-fxqj1u=(v4#gnj&--#&imp*(na3%)s=174!!i6kg-262)r24vh'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    'localhost',  # Permitir localhost
    '127.0.0.1',  # Dirección de loopback
    '*',  
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    
    'rest_framework',
    "coreapi",
    'drf_spectacular',
    'django_extensions',# Va con guión Bajo
    
    
    'app_bookings',
    'app_doctors',
    'app_patients',
    'app_documentation',
    'app_users', # la cree para manejar la consola de Administración y visualizar la Columna "Grupos"
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

ROOT_URLCONF = '_projectdoctor.urls'

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

WSGI_APPLICATION = '_projectdoctor.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


REST_FRAMEWORK = {    
    'DEFAULT_AUTHENTICATION_CLASSES': (          
        # 'rest_framework.authentication.BasicAuthentication',    # Para clientes como Postman
        'rest_framework.authentication.SessionAuthentication',  # Para el navegador, mantener sesion activa.
    ),
    
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',  # Permitir acceso a todos sin autenticación
        # 'rest_framework.permissions.IsAuthenticated',  # Requiere autenticación por defecto
    ),
    
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',  # Renderiza como JSON
        'rest_framework.renderers.BrowsableAPIRenderer',  # Renderiza como HTML (interfaz de DRF), habilitar formulario HTML
    ],
    
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',  # Para datos JSON
        'rest_framework.parsers.FormParser',  # Para datos de formularios HTML
        'rest_framework.parsers.MultiPartParser',  # Para manejo de archivos
    ),
    
    # "DEFAULT_SCHEMA_CLASS": ("rest_framework.schemas.coreapi.AutoSchema"
    # ), # Doducmentación autogenerada con COREAPI
    
    'DEFAULT_SCHEMA_CLASS': ('drf_spectacular.openapi.AutoSchema'
    ), # Doducmentación autogenerada con drf_spectacular
    
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '5/minute',
        'user': '1000/minute'
    }
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'SANTATORIO GRS',
    'DESCRIPTION': 'Descripción de tu API',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
}

