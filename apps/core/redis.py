import redis
from apps.core.cache_config import CacheConfig

def get_redis():
    # Criar um pool de conexões
    pool = redis.ConnectionPool(
        host=CacheConfig.REDIS_HOST,
        port=CacheConfig.REDIS_PORT,
        db=CacheConfig.REDIS_DB,
        password=CacheConfig.REDIS_PASSWORD,
        decode_responses=True
    )
    return redis.Redis(connection_pool=pool)