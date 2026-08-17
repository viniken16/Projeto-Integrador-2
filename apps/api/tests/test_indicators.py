from fastapi.testclient import TestClient


def test_indicators_summary(client: TestClient) -> None:
    response = client.get("/indicators/summary")
    assert response.status_code == 200
    payload = response.json()
    assert "informalidade_geral" in payload
    assert "informalidade_domestica" in payload
    assert "rendimento_domestico" in payload
    assert payload["informalidade_geral"]["informal"] >= 0
    assert payload["informalidade_domestica"]["informal"] >= 0
    assert payload["rendimento_domestico"]["formal"] > 0
