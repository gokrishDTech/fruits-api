from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_add_and_get_fruit():
    # Add a new fruit
    response = client.post("/fruits", json={"fruit": "apple", "color": "red"})
    assert response.status_code == 200
    fruit_id = response.json()["id"]

    # Retrieve the added fruit by ID
    response = client.get(f"/fruits/{fruit_id}")
    assert response.status_code == 200
    assert response.json()["fruit"] == "apple"
    assert response.json()["color"] == "red"
