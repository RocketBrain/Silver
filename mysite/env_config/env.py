from .config import env

if env == 'dev':
    from .env import *
elif env == 'prod':
    from .prod import *