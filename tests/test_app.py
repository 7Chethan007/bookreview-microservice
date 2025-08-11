import pytest
import json
from app import app

@pytest.fixture
def client():
    """Create a test client for the Flask application"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_root(client):
    """Test the root endpoint"""
    response = client.get('/')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert "BookReview API" in data["service"]
    assert data["version"] == "1.0"
    assert "Welcome to the BookReview service!" in data["message"]

def test_reviews(client):
    """Test the reviews endpoint"""
    response = client.get('/reviews')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert "reviews" in data
    assert "count" in data
    assert data["count"] == 2
    assert len(data["reviews"]) == 2

def test_status(client):
    """Test the status/health endpoint"""
    response = client.get('/status')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["status"] == "healthy"
    assert "uptime" in data
    assert "timestamp" in data