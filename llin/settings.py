"""
Django settings for llin project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""
from config import *
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
gettext = lambda s: s
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

PROJECT_PATH = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'bkcep0l=(0!5nbafnzbw8=@b98-lre@n1e2dj%%xi2c1p^dl@m'

# SECURITY WARNING: don't run with debug turned on in production!
if PRODUCTION == False:
    DEBUG = True
else:
    DEBUG = False

TEMPLATE_DEBUG = True
if DEBUG == True:
    ALLOWED_HOSTS = []
else:
    ALLOWED_HOSTS = ['.llin.com']

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'grappelli',   
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'south',
    'states',
    'easy_thumbnails','image_cropping',
    'states_documents',
    'accounts',
    'homepagebanners',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'llin.urls'

WSGI_APPLICATION = 'llin.wsgi.application'

LOGIN_URL = '/login'

LOGIN_REDIRECT_URL = '/maps'
# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        
        'NAME': DBNAME,
       
        'USER': DBUSER,                      
        'PASSWORD':DBPASS,                   
        'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
        #'PORT': '5332', 
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

if DEBUG == True:
    STATIC_ROOT = os.path.join(PROJECT_PATH, "static")
    STATIC_URL = '/static/'
else:
    STATIC_ROOT = PRODUCTION_STATIC_ROOT
    STATIC_URL = PRODUCTION_STATIC_URL

#MEDIA_ROOT = os.path.join(PROJECT_PATH, "media")

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media') # Absolute path to the media directory

STATICFILES_DIRS = (os.path.join(os.path.dirname(__file__),"static"),)
#for st in STATICFILES_DIRS:
    #print str(STATICFILES_DIRS)
    
EMAIL_HOST = EMAIL_HOST
EMAIL_PORT = EMAIL_PORT
EMAIL_HOST_USER =  EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = EMAIL_HOST_PASSWORD
EMAIL_USE_TLS = True
#EMAIL_USE_SSL
INTERNAL_IPS =  ('127.0.0.1',)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
)
TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH, "templates"),
)
TEMPLATE_CONTEXT_PROCESSORS = (
    
    "django.core.context_processors.request",
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.debug',
    'django.core.context_processors.media',
    "django.core.context_processors.i18n",
     
)


GRAPPELLI_ADMIN_TITLE = "LLIN Malaria Elimination CMS"


from easy_thumbnails.conf import Settings as thumbnail_settings
THUMBNAIL_PROCESSORS = (
    'image_cropping.thumbnail_processors.crop_corners',
) + thumbnail_settings.THUMBNAIL_PROCESSORS