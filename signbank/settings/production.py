from signbank.settings.base import *
import os

DEBUG = os.environ.get("DEBUG")
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    "default": {
        "ENGINE": os.environ.get("SQL_ENGINE", "django.db.backends.sqlite3"),
        "NAME": os.environ.get("SQL_DATABASE", os.path.join(BASE_DIR, "db.sqlite3")),
        "USER": os.environ.get("SQL_USER", "user"),
        "PASSWORD": os.environ.get("SQL_PASSWORD", "password"),
        "HOST": os.environ.get("SQL_HOST", "localhost"),
        "PORT": os.environ.get("SQL_PORT", "5432"),
    }
}

SECRET_KEY = os.environ.get("SECRET_KEY")

# 'DJANGO_ALLOWED_HOSTS' should be a single string of hosts with a space between each.
# For example: 'DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]'
ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")

PRIMARY_CSS = os.environ.get("PRIMARY_CSS")
EMAIL_HOST =  os.environ.get("EMAIL_HOST")
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL = os.environ.get("DEFAULT_FROM_EMAIL")
SERVER_EMAIL = os.environ.get("SERVER_EMAIL")

# Absolute path to the directory that holds media.
MEDIA_ROOT = os.environ.get("MEDIA_ROOT")
# URL that handles the media served from MEDIA_ROOT.
MEDIA_URL = os.environ.get("MEDIA_URL")

# within MEDIA_ROOT we store newly uploaded videos in this directory
GLOSS_VIDEO_DIRECTORY = os.environ.get("GLOSS_VIDEO_DIRECTORY")
FILE_UPLOAD_PERMISSIONS = 0o644

# do we implement safe search for anonymous users?
# if True, any gloss that is tagged lexis:crude will be removed from
# search results for users who are not logged in
ANON_SAFE_SEARCH = os.environ.get("ANON_SAFE_SEARCH") == "True"

# do we show the tag based search for anonymous users?
ANON_TAG_SEARCH =  os.environ.get("ANON_TAG_SEARCH") == "True"

# show the number signs page link
NUMBER_SIGNS =  os.environ.get("NUMBER_SIGNS") == "True"

# location of ffmpeg, used to convert uploaded videos
FFMPEG_PROGRAM = os.environ.get("FFMPEG_PROGRAM")
FFMPEG_TIMEOUT = os.environ.get("FFMPEG_TIMEOUT")
FFMPEG_OPTIONS = os.environ.get("FFMPEG_OPTIONS").split(" ")
# Analytics
GOOGLE_ANALYTICS_TRACKING_CODE = os.environ.get("GOOGLE_ANALYTICS_TRACKING_CODE")
