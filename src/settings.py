import os
from decouple import config

def _get_config(config_name: str, cast: type, default=None):
    return cast(os.getenv(config_name)) if os.getenv(config_name) else config(config_name, default=default, cast=cast)

PRIVATE_KEY =_get_config(config_name='PRIVATE_KEY', default='', cast=str)
DB_MONGO_URL =_get_config(config_name='DB_MONGO_URL', default='mongodb://admin:secret@localhost:27017/', cast=str)
DB_MONGO_DATABASE =_get_config(config_name='DB_MONGO_DATABASE', default='mydbone', cast=str)
DB_MONGO_COLLECTION =_get_config(config_name='DB_MONGO_COLLECTION', default='contract', cast=str)