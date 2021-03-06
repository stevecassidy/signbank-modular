from signbank.settings.base import *


# show emails on the console
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

#PRIMARY_CSS = "bootstrap_css/bsl.css"
PRIMARY_CSS = "bootstrap_css/auslan.css"


# defines the aspect ratio for videos
#VIDEO_ASPECT_RATIO = 360.0/640.0

#Enable searching certain tags e.g. medical in a public (anonymous) search
ANON_TAG_SEARCH = True

#Enable safe search in a public (anonymous) search to filter rude words
ANON_SAFE_SEARCH = True

# show/don't show sign navigation
SIGN_NAVIGATION = True

# show the number signs page or an under construction page?
#SHOW_NUMBERSIGNS = False

# do we show the 'advanced search' form and implement 'safe' search?
#ADVANCED_SEARCH = False

# which definition fields do we show and in what order?
#DEFINITION_FIELDS = []


#ADMIN_RESULT_FIELDS = ['idgloss', 'annotation_idgloss']


GLOSS_VIDEO_DIRECTORY = 'glossvideo'


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'debug.log',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}


import mimetypes
mimetypes.add_type("video/mp4", ".mov", True)



# a list of tags we're allowed to use
XALLOWED_TAGS = [ '',
                 'workflow:needs video',
                 'workflow:redo video',
                 'workflow:problematic',
                 'b92:directional',
                 'b92:regional',
                 'b92:variant',
                 'corpus:attested',
                 'lexis:doubtlex',
                 'phonology:alternating',
                 'phonology:dominant hand only',
                 'phonology:double handed',
                 'phonology:forearm rotation',
                 'phonology:handshape change',
                 'phonology:onehand',
                 'phonology:parallel',
                 'phonology:symmetrical',
                 'phonology:two handed',
                ]

FFMPEG_PROGRAM = "/usr/local/bin/ffmpeg"
