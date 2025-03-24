import pytest
from fastapi.testclient import TestClient
from apps.main import app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from apps.core.database import Base, get_db
from apps.schemas.user import UserCreate
from apps.crud.crud_user import create_user


@pytest.fixture(scope='module')
def db():
    engine = create_engine("sqlite:///:memory:", connect_args={"check_same_thread": False})
    Base.metadata.create_all(engine)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db_session = SessionLocal()

    app.dependency_overrides[get_db] = lambda: db_session

    yield db_session

    db_session.close()
    Base.metadata.drop_all(engine)


@pytest.fixture(scope='module')
def client(db):
    client = TestClient(app)
    return client


@pytest.fixture(scope='module')
def create_test_user(db):
    user_in = UserCreate(
        email="testuser@example.com",
        name="Test User",
        phone="1234567890",
        document="123.456.789-00",
        password="testpassword"
    )

    user = create_user(db=db, obj_in=user_in)
    return user


def test_login(db, create_test_user, client):
    login_data = {
        "email": "testuser@example.com",
        "password": "testpassword"
    }

    response = client.post('/api/v1/auth/login', json=login_data)

    assert response.status_code == 200

    response_json = response.json()

    assert "access_token" in response_json
    assert "token_type" in response_json

    assert response.json()["token_type"] == "bearer"


def test_logout(client, create_test_user):
    login_data = {
        "email": "testuser@example.com",
        "password": "testpassword"
    }

    response = client.post("/api/v1/auth/login", json=login_data)
    token = response.json().get("access_token")

    response_logout = client.post("/api/v1/auth/logout", headers={"Authorization": f"Bearer {token}"})

    assert response_logout.status_code == 200
    assert response_logout.json() == {"message": "Successfully logged out"}


def test_logout_without_token(client):
    response_logout = client.post("/api/v1/auth/logout")
    assert response_logout.status_code == 400
    assert response_logout.json() == {"detail": "Token is required"}
