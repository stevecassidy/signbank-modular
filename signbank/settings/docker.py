from signbank.settings.base import *

DEBUG = False
TEMPLATE_DEBUG = False

DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.postgresql',
         'NAME': 'postgres',
         'USER': 'postgres',
         'HOST': 'db',
         'PORT': 5432,
     }
 }


# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = "/code/signbank_static/"

# should be customised on the production server and not kept in VC
SECRET_KEY = '^g=q21r_nnmbz49d!vs*2gvplfsd((02l-y9b@&amp;t3k2r3c$*u&amp;2la5!%s'

ALLOWED_HOSTS = ['web']
