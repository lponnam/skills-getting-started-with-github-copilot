import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_get_activities():
    response = client.get("/activities")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

def signup_for_activity(activity_name: str, email: str):
    payload = {"email": email}
    response = client.post(f"/activities/{activity_name}/signup", json=payload)
    assert response.status_code in (200, 400)  # 400 if already signed up
    # Try duplicate signup
    response_dup = client.post(f"/activities/{activity_name}/signup", json=payload)
    assert response_dup.status_code == 400
    assert "already signed up" in response_dup.json()["detail"].lower()

def signup_for_activity_with_email(activity_name: str, email: str):
    response = client.post(f"/activities/{activity_name}/signup?email={email}")
    assert response.status_code in (200, 400)  # 400 if already signed up
    # Try duplicate signup
    response_dup = client.post(f"/activities/{activity_name}/signup?email={email}")
    assert response_dup.status_code == 400
    assert "already signed up" in response_dup.json()["detail"].lower()

# Add more tests as needed for delete, edge cases, etc.
