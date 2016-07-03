from .config import env

if env == 'dev':
    from .dev import *
elif env == 'prod':
    from .prod import *