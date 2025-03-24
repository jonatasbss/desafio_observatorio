import json

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, joinedload
from typing import List

from apps.core.cache import get_from_cache
from apps.core.database import get_db
from apps.core.security import get_current_user
from apps.crud import crud_sidra
from apps.models.sidra import AtividadeEconomica, ComponenteTransformacao, Periodo, DadosTransformacao
from apps.models.user import User
from apps.schemas.sidra import (AtividadeEconomicaCreate, AtividadeEconomicaResponse, ComponenteTransformacaoCreate,
                                ComponenteTransformacaoResponse, PeriodoCreate, PeriodoResponse,
                                DadosTransformacaoCreate, DadosTransformacaoResponse, FiltroBusca)

router = APIRouter()


@router.post("/atividade", response_model=AtividadeEconomicaResponse)
def create_atividade(atividade: AtividadeEconomicaCreate, db: Session = Depends(get_db),
                     current_user: User = Depends(get_current_user)):
    return crud_sidra.create_atividade(db, atividade)


@router.post("/componente", response_model=ComponenteTransformacaoResponse)
def create_componente(componente: ComponenteTransformacaoCreate, db: Session = Depends(get_db),
                      current_user: User = Depends(get_current_user)):
    return crud_sidra.create_componente(db, componente)


@router.post("/periodo", response_model=PeriodoResponse)
def create_periodo(periodo: PeriodoCreate, db: Session = Depends(get_db),
                   current_user: User = Depends(get_current_user)):
    return crud_sidra.create_periodo(db, periodo)


@router.post("/dados", response_model=DadosTransformacaoResponse)
def create_dados(dados: DadosTransformacaoCreate, db: Session = Depends(get_db),
                 current_user: User = Depends(get_current_user)):
    return crud_sidra.create_dados(db, dados)


@router.get("/dados", response_model=List[DadosTransformacaoResponse])
def read_dados(filtros: FiltroBusca = Depends(), db: Session = Depends(get_db),
               current_user: User = Depends(get_current_user)):
    filtro_key = f"filtros:{json.dumps(filtros.dict())}"

    dados = get_from_cache(filtro_key, crud_sidra.get_dados, db, filtros)

    return dados
