# Django settings for signbank project.

import os

BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
PROJECT_DIR = os.path.dirname(BASE_DIR)

DEBUG = True

EMAIL_HOST = ""
ADMIN_EMAIL = "webmaster@auslan.org.au"

ADMINS = (
     ('Steve Cassidy', 'steve.cassidy@mq.edu.au'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'signbank.db',
    }
}

TIME_ZONE = 'Australia/Sydney'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True


MEDIA_ROOT = os.path.join(PROJECT_DIR, "test-media")
MEDIA_URL = '/media/'
MEDIA_MOBILE_URL = MEDIA_URL


# Ditto for static files from the Auslan site (css, etc) with trailing slash
AUSLAN_STATIC_PREFIX = "/static/"


# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '^g=q21r_nnmbz49d!vs*2gvpll-y9b@&amp;t3k2r3c$*u&amp;2la5!%s'


MIDDLEWARE = (
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'reversion.middleware.RevisionMiddleware',
    'pages.middleware.PageFallbackMiddleware',
)

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

TEMPLATES = [{
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.static',
                # dictionary context processor adds search forms to every template
                'dictionary.views.dictionary_context_processor',
                'pages.context_processors.menu',
                'pages.context_processors.configuration',
            ],
        }
    },
    ]

# add the Email backend to allow logins using email as username
AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    'allauth.account.auth_backends.AuthenticationBackend',
)

INTERNAL_IPS = ('127.0.0.1',)

# allow embedding pages in iframes if they are from this site
X_FRAME_OPTIONS = 'SAMEORIGIN'

ROOT_URLCONF = 'signbank.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'signbank.wsgi.application'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'bootstrap3',
    'django_summernote',

    # modular signbank apps
    'dictionary',
    'feedback',
    'video',
    'signbank_theme_auslan',
    'pages',

    # this app
    'signbank',

    'reversion',
    'tagging',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',

)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


# turn on lots of logging or not
DO_LOGGING = False
LOG_FILENAME = "debug.log"

## Authentication settings

ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED=True
ACCOUNT_SIGNUP_FORM_CLASS = 'signbank.models.RegistrationForm'

## Application settings for signbank


## Settings controlling page contents

# what do we call this signbank?
LANGUAGE_NAME = "Auslan"
COUNTRY_NAME = "Australia"
SITE_TITLE = "Signbank"

# menu settings
NUMBER_SIGNS = False
COLOUR_SIGNS = False
COUNTRY_SIGNS = False
PLACE_SIGNS = False
FINGER_SIGNS = True

# Show social network links?
SOCIAL_NETWORK_SHARE_LINKS = True
# If you turn this on you should provide either your Twitter, Facebook or both urls or the Share menu will be empty
SOCIAL_NETWORK_FACEBOOK_PAGE = None # e.g. "https://www.facebook.com/pages/whatever"
SOCIAL_NETWORK_FACEBOOK_SHARE = True
SOCIAL_NETWORK_TWITTER_PAGE = None # e.g. "https://www.twitter.com/whatever"
SOCIAL_NETWORK_TWITTER_SHARE = True

# Where does the analytics data go?
# "UA-3928964-1" was the original setting or set to None to disable GA
GOOGLE_ANALYTICS_TRACKING_CODE = None

# do we implement safe search for anonymous users?
# if True, any gloss that is tagged lexis:crude will be removed from
# search results for users who are not logged in
ANON_SAFE_SEARCH = False

# do we show the tag based search for anonymous users?
ANON_TAG_SEARCH = False


# do we display the previous/next links to signs, requires gloss.sn to be used consistently
SIGN_NAVIGATION = True

# show FREQUENCY info on sign distribution
SHOW_FREQUENCY = False

# show traditional info on sign distribution
SHOW_TRADITIONAL = True

# which definition fields do we show and in what order?
DEFINITION_FIELDS = ['auslan', 'general', 'noun', 'verb', 'interact', 'deictic', 'modifier', 'question', 'augment', 'note']

DEFINITION_ROLE_CHOICES = (
    ('auslan', 'Definition in Auslan'),
    ('general', 'General Definition'),
    ('noun', 'As a Noun'),
    ('verb', 'As a Verb or Adjective'),
    ('deictic', 'As a Pointing Sign'),
    ('interact', 'Interactive'),
    ('modifier', 'As Modifier'),
    ('question', 'As Question'),
    ('popexplain', 'Popular Explanation'),
    ('augment', 'Augmented Meaning'),
    ('note', 'Note'),
    ('privatenote', 'Private Note'),
    ('B92 sn', 'Sign Number in Brien 92'),
)

ADMIN_RESULT_FIELDS = ['sn', 'idgloss', 'annotation_idgloss', 'morph']


# location and URL for uploaded files
UPLOAD_ROOT = MEDIA_ROOT + "upload/"
UPLOAD_URL = MEDIA_URL + "upload/"

SUMMERNOTE_CONFIG = {
    'attachment_filesize_limit': 1024 * 1024 * 100,
    'summernote': {
        'toolbar': [
            ['style', ['style']],
            ['font', ['bold', 'underline', 'clear']],
            ['fontname', ['fontname']],
            ['color', ['color']],
            ['para', ['ul', 'ol', 'paragraph']],
            ['table', ['table']],
            ['insert', ['link', 'picture', 'video', 'file']],
            ['view', ['fullscreen', 'codeview', 'help']],
            ],
    },
    'js': (
        '/static/js/summernote-file.js',
    )
}


# Location for comment videos relative to MEDIA_ROOT
COMMENT_VIDEO_LOCATION = "comments"
# Location for videos associated with pages
PAGES_VIDEO_LOCATION = 'pages'
# location for upload of videos relative to MEDIA_ROOT
# videos are stored here prior to copying over to the main
# storage location
VIDEO_UPLOAD_LOCATION = "upload"

# path to store uploaded attachments relative to MEDIA_ROOT
ATTACHMENT_LOCATION = 'attachments'

# within MEDIA_ROOT we store newly uploaded videos in this directory
GLOSS_VIDEO_DIRECTORY = "video"

# which fields from the Gloss model should be included in the quick update form on the sign view
QUICK_UPDATE_GLOSS_FIELDS = ['language', 'dialect']

# should we always require a login for viewing dictionary content
ALWAYS_REQUIRE_LOGIN = False

# name of the primary css file, relative to the media directory
PRIMARY_CSS = "bootstrap_css/test-server.css"

# name of the mobile css extension file, to be loaded after the main mobile css to customise it for a site
# relative to the media directory
MOBILE_CSS = "bootstrap_css/mobile-extra.css"

# do we allow people to register for the site
ALLOW_REGISTRATION = True
ACCOUNT_ACTIVATION_DAYS = 7


# show the number signs page or an under construction page?
SHOW_NUMBERSIGNS = True

LOGIN_REDIRECT_URL = '/feedback/'


# location of ffmpeg, used to convert uploaded videos
# Mac with homebrew
FFMPEG_PROGRAM = "/usr/local/bin/ffmpeg"
# Windows
#FFMPEG_PROGRAM = os.path.expanduser("~/documents/ffmpeg/bin/ffmpeg.exe")
FFMPEG_TIMEOUT = 60
FFMPEG_OPTIONS = ["-vcodec", "h264", "-an"]


# defines the aspect ratio for videos
VIDEO_ASPECT_RATIO = 3.0/4.0

DICTIONARY_FILTER_TAGS = [
        ('semantic:health', 'Health'),
        ('semantic:education', 'Education'),
        ('semantic:animal', 'Animal'),
        ('semantic:arithmetic', 'Arithmetic'),
        ('semantic:arts', 'Arts'),
        ('semantic:bodypart', 'Body Part'),
        ('semantic:car', 'Car'),
        ('semantic:city', 'City'),
        ('semantic:clothing', 'Clothing') ,
        ('semantic:color', 'Color') ,
        ('semantic:cooking', 'Cooking') ,
        ('semantic:day', 'Day') ,
        ('semantic:deaf', 'Deaf') ,
        ('semantic:drink', 'Drink') ,
        ('semantic:family', 'Family') ,
        ('semantic:feel', 'Feel') ,
        ('semantic:food', 'Food') ,
        ('semantic:furniture', 'Furniture') ,
        ('semantic:government', 'Government') ,
        ('semantic:groom', 'Groom') ,
        ('semantic:judge', 'Judge') ,
        ('semantic:language act', 'Language act') ,
        ('semantic:law', 'Law') ,
        ('semantic:material', 'Material') ,
        ('semantic:metalg', 'Metalg') ,
        ('semantic:mind', 'Mind') ,
        ('semantic:money', 'Money') ,
        ('semantic:nature', 'Nature') ,
        ('semantic:number', 'Number') ,
        ('semantic:order', 'Order') ,
        ('semantic:people', 'People') ,
        ('semantic:physical act', 'Physical act') ,
        ('semantic:quality', 'Quality') ,
        ('semantic:quantity', 'Quantity') ,
        ('semantic:question', 'Question') ,
        ('semantic:recreation', 'Recreation') ,
        ('semantic:rooms', 'Rooms') ,
        ('semantic:salutation', 'Salutation') ,
        ('semantic:sensing', 'Sensing') ,
        ('semantic:sexuality', 'Sexuality') ,
        ('semantic:shapes', 'Shapes') ,
        ('semantic:shopping', 'Shopping') ,
        ('semantic:sport', 'Sport') ,
        ('semantic:telecommunications', 'Telecommunications') ,
        ('semantic:time', 'Time') ,
        ('semantic:travel', 'Travel') ,
        ('semantic:utensil', 'Utensil') ,
        ('semantic:weather', 'Weather') ,
        ('semantic:work', 'Work') ,
        ]

# settings for django-tagging

FORCE_LOWERCASE_TAGS = True

# a list of tags we're allowed to use
ALLOWED_TAGS = [ '',
                 'b92:directional',
                 'b92:regional',
                 'corpus:attested',
                 'iconicity:obscure',
                 'iconicity:opaque',
                 'iconicity:translucent',
                 'iconicity:transparent',
                 'lexis:battinson',
                 'lexis:classifier',
                 'lexis:crude',
                 'lexis:doubtlex',
                 'lexis:fingerspell',
                 'lexis:gensign',
                 'lexis:marginal',
                 'lexis:obsolete',
                 'lexis:proper name',
                 'lexis:regional',
                 'lexis:restricted lexeme',
                 'lexis:signed english',
                 'lexis:signed english only',
                 'lexis:technical',
                 'lexis:varlex',
                 'morph:begin directional sign',
                 'morph:body locating',
                 'morph:directional sign',
                 'morph:end directional sign',
                 'morph:locational and directional',
                 'morph:orientating sign',
                 'phonology:alternating',
                 'phonology:dominant hand only',
                 'phonology:double handed',
                 'phonology:forearm rotation',
                 'phonology:handshape change',
                 'phonology:onehand',
                 'phonology:parallel',
                 'phonology:symmetrical',
                 'phonology:two handed',
                 'religion:anglican',
                 'religion:catholic',
                 'religion:catholic school',
                 'religion:jehovas witness',
                 'religion:other',
                 'religion:religion',
                 'semantic:animal',
                 'semantic:arithmetic',
                 'semantic:arts',
                 'semantic:bodypart',
                 'semantic:car',
                 'semantic:city',
                 'semantic:clothing',
                 'semantic:color',
                 'semantic:cooking',
                 'semantic:day',
                 'semantic:deaf',
                 'semantic:drink',
                 'semantic:education',
                 'semantic:family',
                 'semantic:feel',
                 'semantic:food',
                 'semantic:furniture',
                 'semantic:government',
                 'semantic:groom',
                 'semantic:health',
                 'semantic:judge',
                 'semantic:language act',
                 'semantic:law',
                 'semantic:material',
                 'semantic:metalg',
                 'semantic:mind',
                 'semantic:money',
                 'semantic:nature',
                 'semantic:number',
                 'semantic:order',
                 'semantic:people',
                 'semantic:physical act',
                 'semantic:quality',
                 'semantic:quantity',
                 'semantic:question',
                 'semantic:recreation',
                 'semantic:rooms',
                 'semantic:salutation',
                 'semantic:sensing',
                 'semantic:sexuality',
                 'semantic:shapes',
                 'semantic:shopping',
                 'semantic:sport',
                 'semantic:telecommunications',
                 'semantic:time',
                 'semantic:travel',
                 'semantic:utensil',
                 'semantic:weather',
                 'semantic:work',
                 'school:state school',
                 'workflow:needs video',
                 'workflow:redo video',
                 'workflow:problematic',
                 ]
