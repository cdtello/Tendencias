"""
Django settings for maravillapp project.

Generated by 'django-skins startproject' using Django 2.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'eh1m2#l1(2(o7l5&5qdohgt4cn&rrbna*h_6dmtn%k1m#z(+ba'

STRIPE_SECRET_KEY = 'sk_test_LexHyNBv4PeixNhgOAn5Lg7t00bJE2jDgD'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

if DEBUG:
    # test keys
    STRIPE_PUBLISHABLE_KEY = ''
    STRIPE_SECRET_KEY = ''
    BT_ENVIRONMENT='sandbox'
    BT_MERCHANT_ID='YOUR BT_MERCHANT_ID'
    BT_PUBLIC_KEY='YOUR BT_PUBLIC_KEY'
    BT_PRIVATE_KEY='YOUR BT_PRIVATE_KEY'
else:
    # live keys
    STRIPE_PUBLISHABLE_KEY = 'YOUR STRIPE LIVE PUB KEY'
    STRIPE_SECRET_KEY = 'YOUR STRIPE LIVE SECRET KEY'

ALLOWED_HOSTS = ['.localhost', '.127.0.0.1']

AUTH_USER_MODEL = 'usuarios.Usuario'
LOGIN_REDIRECT_URL = 'usuarios:home'
LOGIN_URL = 'usuarios:login'
LOGOUT_REDIRECT_URL = 'usuarios:login'

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY ='236112711519-gluuguht1m2kd0c5oaka8ih196dq2p0n.apps.googleusercontent.com'  #Paste CLient Key
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'bRwho1KFl27VC4HAVC2t3WrA' #Paste Secret Key

CITIES_LIGHT_TRANSLATION_LANGUAGES = ['es', 'en']
CITIES_LIGHT_INCLUDE_COUNTRIES = ['CO']

SITE_ID = 1

# Application definition
SHARED_APPS = (
	'django_tenants',  # Obligatorio
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'bootstrap4',
    'widget_tweaks',
    'django_select2',
    'cities_light',
    'send',
    'social_django',

    'apps.usuarios',
    'apps.tenants',
	'apps.productos',
	'apps.carrito'

)


TENANT_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'bootstrap4',
    'widget_tweaks',
    'django_select2',
    'cities_light',
    'send',
    'social_django',

    'apps.usuarios',
    'apps.productos',
	'apps.carrito',

)

INSTALLED_APPS = list(SHARED_APPS) + [app for app in TENANT_APPS if app not in SHARED_APPS]

TENANT_MODEL = "tenants.Tenant" # Modelo que hereda de TenantMixin
TENANT_DOMAIN_MODEL = "tenants.Dominio"  # Modelo que hereda de DomainMixin

MIDDLEWARE = [
    'django_tenants.middleware.main.TenantMainMiddleware', # Necesario que este en el top de los MIDDLEWARE
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware', #iniciar sesión con redes sociales
]

AUTHENTICATION_BACKENDS = (
    'social_core.backends.open_id.OpenIdAuth',  # for Google authentication
    'social_core.backends.google.GoogleOpenId',  # for Google authentication
    'social_core.backends.google.GoogleOAuth2',  # for Google authentication
    'social_core.backends.github.GithubOAuth2',  # for Github authentication
    'social_core.backends.facebook.FacebookOAuth2',  # for Facebook authentication

    'django.contrib.auth.backends.ModelBackend',
)

ROOT_URLCONF = 'maravillapp.tenant_urls'
# Con esta línea se tiene una separación de las urls del tenant public  y de las urls para los tenants
PUBLIC_SCHEMA_URLCONF = 'maravillapp.public_urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'), 'templates',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'social_django.context_processors.backends',  # iniciar sesión con redes sociales
                'social_django.context_processors.login_redirect',  # iniciar sesión con redes sociales
            ],
        },
    },
]

WSGI_APPLICATION = 'maravillapp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django_tenants.postgresql_backend',
        'NAME': 'maravillapp',
        'USER': 'postgres',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': 5432,
    }
}
# Necesario para multitenant
DATABASE_ROUTERS = (
    'django_tenants.routers.TenantSyncRouter',
)

DOMAIN = '.localhost'

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'America/Bogota'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"), )
MEDIA_ROOT = os.path.join(BASE_DIR, '', 'media')

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'maravilla.franquicias@gmail.com'
EMAIL_HOST_PASSWORD = 'maravilla123'
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False

# Stripe and Braintree Settings
