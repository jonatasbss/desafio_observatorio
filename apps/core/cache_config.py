from decouple import config


class CacheConfig:
    REDIS_HOST = config("REDIS_HOST", default="localhost")
    REDIS_PORT = config("REDIS_PORT", default=6379, cast=int)
    REDIS_DB = config("REDIS_DB", default=0, cast=int)
    REDIS_PASSWORD = config("REDIS_PASSWORD", default=None)
    REDIS_CACHE_TIMEOUT = config("REDIS_CACHE_TIMEOUT", default=300, cast=int)
