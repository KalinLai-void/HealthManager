import dj_database_url
from .settings import *
DATABASES = {
    'default': dj_database_url.config(),
}
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
ALLOWED_HOSTS = ['*']
DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'd1g9ql6pr9uf74', # The Server name from 1.5
        'USER': 'floxbkqnccbaxe', # The username from 1.6
        'PASSWORD': '6e3b58cbb2e191f12bfc2c1186f646c7194209b3b18ee3033c540e8a3608e28c', # The password from installation
        'HOST': 'ec2-34-231-177-125.compute-1.amazonaws.com', # Host name/address from 1.6
        'PORT': '5432' # Port from 1.6
    }
}