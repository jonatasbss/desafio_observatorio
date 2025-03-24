from sqlalchemy.orm import relationship
from apps.core.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL, Index


class AtividadeEconomica(Base):
    __tablename__ = "atividade_economica"

    id = Column(Integer, primary_key=True, index=True)
    codigo_cnae = Column(String, unique=True, index=True)
    descricao = Column(String, unique=True, index=True)

    dados_transformacao = relationship("DadosTransformacao", back_populates="atividade_economica")


class ComponenteTransformacao(Base):
    __tablename__ = "componente_transformacao"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, unique=True, index=True)

    dados_transformacao = relationship("DadosTransformacao", back_populates="componente_transformacao")


class Periodo(Base):
    __tablename__ = "periodo"

    id = Column(Integer, primary_key=True, index=True)
    ano = Column(Integer, unique=True, index=True)

    dados_transformacao = relationship("DadosTransformacao", back_populates="periodo")


class DadosTransformacao(Base):
    __tablename__ = "dados_transformacao"

    id = Column(Integer, primary_key=True, index=True)
    atividade_economica_id = Column(Integer, ForeignKey("atividade_economica.id"), nullable=False)
    componente_id = Column(Integer, ForeignKey("componente_transformacao.id"), nullable=False)
    periodo_id = Column(Integer, ForeignKey("periodo.id"), nullable=False)
    valor = Column(DECIMAL(18, 2), index=True)  # Não precisa ser unique

    # Relacionamentos corrigidos
    atividade_economica = relationship("AtividadeEconomica", back_populates="dados_transformacao")
    componente_transformacao = relationship("ComponenteTransformacao", back_populates="dados_transformacao")
    periodo = relationship("Periodo", back_populates="dados_transformacao")

    # Criação do índice composto
    __table_args__ = (
        Index('ix_dados_transformacao_atividade_componente_periodo',
              'atividade_economica_id', 'componente_id', 'periodo_id'),
    )