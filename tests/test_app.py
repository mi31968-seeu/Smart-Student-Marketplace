import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1] / "backend"))

from app import app

def test_home_route():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Smart Student Marketplace API" in response.data

def test_register_user_success():
    client = app.test_client()
    response = client.post("/register", json={
        "name": "Test Student",
        "email": "test1@example.com",
        "password": "12345"
    })
    assert response.status_code == 201
    assert response.get_json()["message"] == "User registered"

def test_register_missing_data():
    client = app.test_client()
    response = client.post("/register", json={
        "name": "",
        "email": "missing@example.com",
        "password": ""
    })
    assert response.status_code == 400

def test_login_invalid_user():
    client = app.test_client()
    response = client.post("/login", json={
        "email": "wrong@example.com",
        "password": "wrong"
    })
    assert response.status_code == 401

def test_add_service_success():
    client = app.test_client()
    response = client.post("/services", json={
        "title": "Math Tutoring",
        "category": "Tutoring",
        "description": "Help with math",
        "price": "10 EUR/hour",
        "owner": "Test Student"
    })
    assert response.status_code == 201
    assert response.get_json()["message"] == "Service added"

def test_search_services():
    client = app.test_client()
    client.post("/services", json={
        "title": "Python Tutoring",
        "category": "Tutoring",
        "description": "Python help",
        "price": "12 EUR/hour",
        "owner": "Test Student"
    })
    response = client.get("/services?search=python")
    assert response.status_code == 200
    assert any(service["title"] == "Python Tutoring" for service in response.get_json())

def test_add_review():
    client = app.test_client()
    response = client.post("/reviews", json={
        "service": "Math Tutoring",
        "rating": 5,
        "comment": "Very useful"
    })
    assert response.status_code == 201
    assert response.get_json()["message"] == "Review added"
