import json
from typing import Callable, Any

from fastapi import HTTPException
from decimal import Decimal
from apps.core.cache_config import CacheConfig
from apps.core.redis import get_redis


def serialize_dados(dados: Any) -> Any:
    if isinstance(dados, list):
        return [serialize_dados(dado) for dado in dados]

    # Se o dado for um tipo Decimal, converte para float
    if isinstance(dados, Decimal):
        return float(dados)

    # Se o dado for um objeto com atributos, converte para dicionário
    if hasattr(dados, '__dict__'):
        return {key: serialize_dados(value) for key, value in dados.__dict__.items() if not key.startswith('_')}

    return dados

def get_from_cache(
    cache_key: str,
    get_data_func: Callable,
    db_session: Any,
    *args: Any
) -> Any:
    redis_client = get_redis()

    # Tenta obter os dados do cache
    cached_data = redis_client.get(cache_key)

    if cached_data:
        return json.loads(cached_data)

    # Dados não encontrados no cache, então obtém do banco
    try:
        data = get_data_func(db_session, *args)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Erro ao consultar o banco de dados: {str(e)}"
        )

    serializable_data = serialize_dados(data)

    # Armazenando os dados no cache com timeout configurado
    redis_client.setex(cache_key, CacheConfig.REDIS_CACHE_TIMEOUT, json.dumps(serializable_data))

    return data
