from . import *

if DEBUG:
    import sys
    print(" ".join(['='.join([key, os.environ[key]]) for key in ["SECRET_KEY","DEBUG","DB_DEFAULT_HOST","DB_DEFAULT_NAME","DB_DEFAULT_USER","DB_DEFAULT_PASSWORD","DJANGO_SETTINGS_MODULE"]]))
