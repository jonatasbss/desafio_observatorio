from typing import List
from fastapi import HTTPException
from sqlalchemy.orm import Session, joinedload, class_mapper
from apps.schemas.sidra import FiltroBusca
from apps.models.sidra import AtividadeEconomica, ComponenteTransformacao, Periodo, DadosTransformacao
from apps.schemas.sidra import AtividadeEconomicaCreate, ComponenteTransformacaoCreate, PeriodoCreate, \
    DadosTransformacaoCreate


def create_atividade(db: Session, atividade: AtividadeEconomicaCreate):
    db_atividade = AtividadeEconomica(**atividade.model_dump())
    db.add(db_atividade)
    db.commit()
    db.refresh(db_atividade)
    return db_atividade


def create_componente(db: Session, componente: ComponenteTransformacaoCreate):
    db_componente = ComponenteTransformacao(**componente.model_dump())
    db.add(db_componente)
    db.commit()
    db.refresh(db_componente)
    return db_componente


def create_periodo(db: Session, periodo: PeriodoCreate):
    db_periodo = Periodo(**periodo.model_dump())
    db.add(db_periodo)
    db.commit()
    db.refresh(db_periodo)
    return db_periodo


def create_dados(db: Session, dados: DadosTransformacaoCreate):
    if not db.get(AtividadeEconomica, dados.atividade_economica_id):
        raise HTTPException(status_code=404, detail="Atividade Econômica não encontrada")
    if not db.get(ComponenteTransformacao, dados.componente_id):
        raise HTTPException(status_code=404, detail="Componente não encontrado")
    if not db.get(Periodo, dados.periodo_id):
        raise HTTPException(status_code=404, detail="Período não encontrado")

    db_dados = DadosTransformacao(**dados.model_dump())
    db.add(db_dados)
    db.commit()
    db.refresh(db_dados)
    return db_dados


def get_dados(db: Session, filtros: FiltroBusca) -> List[DadosTransformacao]:
    query = db.query(DadosTransformacao).options(
        joinedload(DadosTransformacao.atividade_economica),
        joinedload(DadosTransformacao.componente_transformacao),
        joinedload(DadosTransformacao.periodo)
    )

    if filtros.atividade_economica_codigo_cnae:
        query = query.join(AtividadeEconomica).filter(
            AtividadeEconomica.codigo_cnae == filtros.atividade_economica_codigo_cnae
        )

    if filtros.atividade_economica_descricao:
        query = query.join(AtividadeEconomica).filter(
            AtividadeEconomica.descricao.ilike(f"%{filtros.atividade_economica_descricao}%")
        )

    if filtros.componente_nome:
        query = query.join(ComponenteTransformacao).filter(
            ComponenteTransformacao.nome.ilike(f"%{filtros.componente_nome}%")
        )

    if filtros.periodo_ano:
        query = query.join(Periodo).filter(
            Periodo.ano == filtros.periodo_ano
        )

    return query.all()
