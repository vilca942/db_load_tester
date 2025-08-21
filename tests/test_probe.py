"""
Tests related to the probe route
"""

from fastapi import status
from fastapi.testclient import TestClient


def test_probe(client: TestClient) -> None:
    """Test that the probe endpoint is working"""

    resp = client.get("/")

    assert resp.status_code == status.HTTP_200_OK
