import pytest
from apps.models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from apps.core.config import settings
from apps.crud.crud_user import create_user, get_user
from apps.core.database import Base
from apps.schemas.user import UserCreate


@pytest.fixture(scope='module')
def db():
    # Cria uma instância do banco de dados de teste em memória
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)  # Cria as tabelas
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db_session = SessionLocal()
    yield db_session
    db_session.close()
    Base.metadata.drop_all(engine)


def test_create_user(db):
    # Criar um objeto UserCreate com os dados do usuário
    user_in = UserCreate(
        email="observatorio@sfiec.org.br",
        name="Observatório da Industria",
        phone="85999999999",
        document="07.264.385/0001-43",
        password="observatorio"
    )

    # Passar o objeto UserCreate para a função create_user
    user = create_user(db=db, obj_in=user_in)

    # Verificar os dados do usuário
    assert user.email == "observatorio@sfiec.org.br"
    assert user.name == "Observatório da Industria"
    assert user.phone == "85999999999"
    assert user.document == "07.264.385/0001-43"

    # Verificar se o usuário foi salvo no banco de dados
    db_user = db.query(User).filter(User.email == "observatorio@sfiec.org.br").first()
    assert db_user is not None
    assert db_user.email == "observatorio@sfiec.org.br"

    # Teste de leitura de um usuário existente


def test_read_user(db):
    user_in = UserCreate(
        email="istcis@sfiec.org.br",
        name="Instituto Senai de Tecnologia",
        phone="85999999999",
        document="07.264.385/0001-43",
        password="istcis"
    )

    user = create_user(db=db, obj_in=user_in)

    # Recupera o usuário pelo ID
    db_user = get_user(db, user_id=user.id)
    assert db_user is not None
    assert db_user.email == user.email
    assert db_user.name == user.name
