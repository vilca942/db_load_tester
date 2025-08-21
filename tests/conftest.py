import pytest
from fastapi import FastAPI
from src.main import create_app
from fastapi.testclient import TestClient
from sqlalchemy.engine import Engine, create_engine
from src.settings import settings
from sqlalchemy import text
from src.models import Base


@pytest.fixture(scope="session")
def db_engine() -> Engine:
    """returns a SQLAlchemy engine which is deleted after the test session"""

    return create_engine(
        settings.db_url,
        pool_size=5,
    )


@pytest.fixture(autouse=True, scope="session")
def set_database(db_engine: Engine) -> None:
    """setting the database at test session start"""

    with db_engine.begin() as connection:
        for table in Base.metadata.sorted_tables:
            connection.execute(text(f"DROP TABLE IF EXISTS {table} CASCADE"))
        connection.execute(text(f"CREATE SCHEMA IF NOT EXISTS {settings.db_schema}"))


@pytest.fixture(autouse=True)
def clean_database(db_engine: Engine) -> None:
    """cleaning database before each test"""

    with db_engine.begin() as connection:
        tables = Base.metadata.sorted_tables
        for table in tables:
            connection.execute(text(f"DELETE FROM {table}"))


@pytest.fixture(scope="session")
def testing_app() -> FastAPI:
    """creating the testing app at test session start"""

    return create_app()


@pytest.fixture(scope="session")
def client(testing_app: FastAPI) -> TestClient:
    """creating a TestClient of the fastapi app at test session start"""

    return TestClient(testing_app)
