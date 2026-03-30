from main import app


def test_random_question():
    from fastapi.testclient import TestClient

    client = TestClient(app)
    response = client.get("/api/question/random")
    assert response.status_code == 200
    data = response.json()
    assert "question" in data
    assert "remaining" in data
    assert "total" in data
    assert data["total"] == 30


def test_no_duplicate_until_exhausted():
    from fastapi.testclient import TestClient

    client = TestClient(app)
    client.get("/api/question/reset")
    seen = set()
    for _ in range(30):
        response = client.get("/api/question/random")
        data = response.json()
        seen.add(data["question"])
    assert len(seen) == 30


def test_reset():
    from fastapi.testclient import TestClient

    client = TestClient(app)
    response = client.get("/api/question/reset")
    assert response.status_code == 200
    assert response.json()["status"] == "reset"


def test_health():
    from fastapi.testclient import TestClient

    client = TestClient(app)
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"
