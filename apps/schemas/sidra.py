from pydantic import BaseModel
from typing import Optional


# Schema para Atividade Econômica (CNAE)
class AtividadeEconomicaCreate(BaseModel):
    codigo_cnae: str
    descricao: str


class AtividadeEconomicaResponse(BaseModel):
    id: int
    codigo_cnae: str
    descricao: str

    class Config:
        from_attributes = True


# Schema para Componentes da Transformação Industrial
class ComponenteTransformacaoCreate(BaseModel):
    nome: str


class ComponenteTransformacaoResponse(BaseModel):
    id: int
    nome: str

    class Config:
        from_attributes = True


# Schema para Período (Ano)
class PeriodoCreate(BaseModel):
    ano: int


class PeriodoResponse(BaseModel):
    id: int
    ano: int

    class Config:
        from_attributes = True


# Schema para Dados da Transformação Industrial
class DadosTransformacaoCreate(BaseModel):
    atividade_economica_id: int
    componente_id: int
    periodo_id: int
    valor: float


class DadosTransformacaoResponse(BaseModel):
    id: int
    valor: float
    atividade_economica: AtividadeEconomicaResponse
    componente_transformacao: ComponenteTransformacaoResponse
    periodo: PeriodoResponse

    class Config:
        from_attributes = True

    # Vamos adicionar métodos para "converter" os relacionamentos manualmente.
    @classmethod
    def from_orm(cls, obj):
        """Método para mapear os dados de relacionamento manualmente."""
        # Pega os atributos do objeto ORM
        data = super().from_orm(obj)

        # Mapeia as relações manualmente
        data.atividade_economica = AtividadeEconomicaResponse.from_orm(obj.atividade_economica)
        data.componente_transformacao = ComponenteTransformacaoResponse.from_orm(obj.componente_transformacao)
        data.periodo = PeriodoResponse.from_orm(obj.periodo)

        return data


class FiltroBusca(BaseModel):
    atividade_economica_codigo_cnae: Optional[str] = None
    atividade_economica_descricao: Optional[str] = None
    componente_nome: Optional[str] = None
    periodo_ano: Optional[int] = None
