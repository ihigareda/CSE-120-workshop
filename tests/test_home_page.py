from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_home_page_renders():
    resp = client.get("/")
    assert resp.status_code == 200
    body = resp.text
    assert "CSE120 GitHub Workshop" in body
    assert "Average Calculator" in body