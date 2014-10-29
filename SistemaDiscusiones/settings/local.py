from .base import *

DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'Discusiones',
        'USER':'postgres',
        'PASSWORD':'root',
        'HOST':'localhost',
    }
}

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR.child('static')]

SOCIAL_AUTH_FACEBOOK_KEY = '869171993098500'
SOCIAL_AUTH_FACEBOOK_SECRET = 'b4417ca0376ae49967e94bc497ee56c6'

SOCIAL_AUTH_TWITTER_KEY = 'j0LPozsYlizCx1l3AvLHFNHRG'
SOCIAL_AUTH_TWITTER_SECRET = 'ZGNBo0cmiNhPtRYbgc1L31TxeGjmcnuL2hTFcQ3cBns6qxcvdI'

SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']

MANDRILL_API_KEY = 'rXmo4PtP1CNqE4SdQuPJBg'


CACHES = {
		'default':{
			'BACKEND': 'redis_cache.RedisCache',
			#'LOCATION':'grideye.redistogo.com:10097',
			'LOCATION':'localhost:6379',
			'OPTIONS':{
				'DB':1,
				#'PASSWORD':'aaaa',
			}
		}

	}

