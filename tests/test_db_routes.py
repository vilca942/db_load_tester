"""
Tests related to the db routes
"""

from fastapi import status
from fastapi.testclient import TestClient
from src.db_routes import random_string
from sqlalchemy.engine import Engine
from sqlalchemy import text
import random
from src.settings import settings


def test_write(client: TestClient, db_engine: Engine) -> None:
    """Test the /write route"""

    random = random_string()

    resp = client.post(f"/write?sentence={random}")

    with db_engine.begin() as connection:
        sentences = connection.execute(
            text(f"select * from {settings.db_schema}.sentences;")
        ).all()

    id, sentence = sentences[0]

    assert resp.status_code == status.HTTP_200_OK
    assert id == 1 and sentence == random
    assert len(sentences) == 1


def test_count_all(client: TestClient) -> None:
    """test the /count_all route"""

    count = random.randint(1, 100)

    for _ in range(count):
        client.post("/write")

    resp = client.get("/count_all")

    assert resp.status_code == status.HTTP_200_OK
    assert int(resp.text) == count
