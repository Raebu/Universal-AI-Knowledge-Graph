from __future__ import annotations

from fastapi.testclient import TestClient

from universal_kg.api.main import app


def test_health_and_ready() -> None:
    client = TestClient(app)
    assert client.get("/health").status_code == 200
    assert client.get("/ready").json() == {"status": "ready"}


def test_end_to_end_ingest_then_search() -> None:
    client = TestClient(app)
    ingest_response = client.post(
        "/v1/ingest",
        json={
            "workspace_id": "e2e",
            "source": "manual",
            "title": "Slack export note",
            "body": "The platform team decided that GitHub pull requests need security review.",
            "metadata": {"system": "slack"},
        },
    )
    assert ingest_response.status_code == 200

    search_response = client.post(
        "/v1/search",
        json={"workspace_id": "e2e", "query": "GitHub security review", "limit": 5},
    )
    assert search_response.status_code == 200
    assert search_response.json()["hits"]


def test_rejects_invalid_workspace() -> None:
    client = TestClient(app)
    response = client.post(
        "/v1/search",
        json={"workspace_id": "bad workspace", "query": "test", "limit": 5},
    )
    assert response.status_code == 422
