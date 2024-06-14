from fastapi.testclient import TestClient

from api.app import app


def test_app():
    client = TestClient(app) # Arrange (organização)

    response = client.get('/') # Act (ação)

    SUCCESS = 200
    assert response.status_code == SUCCESS # Assert (garantir que)
    assert response.json() == {'message': 'Hello world!'} # Assert (garantir que)
