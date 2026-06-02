import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
BACKEND_PATH = PROJECT_ROOT / "backend"
sys.path.insert(0, str(BACKEND_PATH))

from app import create_app


def make_client(tmp_path):
    database_path = tmp_path / "test_marketplace.db"
    app = create_app(database_path)
    app.config["TESTING"] = True
    return app.test_client()


def register_user(client, name="Mustafa Ismaili", email="mustafa@example.com"):
    return client.post(
        "/register",
        json={"name": name, "email": email, "password": "password123"},
    )


def test_register_user_successfully(tmp_path):
    client = make_client(tmp_path)
    response = register_user(client)

    assert response.status_code == 201
    assert response.get_json()["email"] == "mustafa@example.com"


def test_login_user_successfully(tmp_path):
    client = make_client(tmp_path)
    register_user(client)

    response = client.post(
        "/login",
        json={"email": "mustafa@example.com", "password": "password123"},
    )

    assert response.status_code == 200
    assert response.get_json()["name"] == "Mustafa Ismaili"


def test_login_fails_with_wrong_password(tmp_path):
    client = make_client(tmp_path)
    register_user(client)

    response = client.post(
        "/login",
        json={"email": "mustafa@example.com", "password": "wrongpassword"},
    )

    assert response.status_code == 401


def test_create_service_post(tmp_path):
    client = make_client(tmp_path)
    user_response = register_user(client)
    user_id = user_response.get_json()["id"]

    response = client.post(
        "/services",
        json={
            "user_id": user_id,
            "title": "Math Tutoring",
            "description": "I can help students with math exercises.",
            "category": "Tutoring",
            "price": 10,
        },
    )

    assert response.status_code == 201
    assert response.get_json()["message"] == "Service created successfully"


def test_search_services(tmp_path):
    client = make_client(tmp_path)
    user_response = register_user(client)
    user_id = user_response.get_json()["id"]

    client.post(
        "/services",
        json={
            "user_id": user_id,
            "title": "Programming Notes",
            "description": "Java and Python notes for students.",
            "category": "Notes",
            "price": 5,
        },
    )

    response = client.get("/services?search=python")
    data = response.get_json()

    assert response.status_code == 200
    assert len(data) == 1
    assert data[0]["title"] == "Programming Notes"


def test_send_message(tmp_path):
    client = make_client(tmp_path)
    sender = register_user(client, "Mustafa Ismaili", "mustafa@example.com").get_json()["id"]
    receiver = register_user(client, "Amra Demiri", "amra@example.com").get_json()["id"]

    response = client.post(
        "/messages",
        json={"sender_id": sender, "receiver_id": receiver, "content": "Hello, is this service available?"},
    )

    assert response.status_code == 201
    assert response.get_json()["message"] == "Message sent successfully"


def test_add_review(tmp_path):
    client = make_client(tmp_path)
    user_id = register_user(client).get_json()["id"]

    service_response = client.post(
        "/services",
        json={
            "user_id": user_id,
            "title": "Laptop Rent",
            "description": "Laptop available for rent.",
            "category": "Renting",
            "price": 15,
        },
    )
    service_id = service_response.get_json()["id"]

    response = client.post(
        "/reviews",
        json={"service_id": service_id, "reviewer_id": user_id, "rating": 5, "comment": "Very good service."},
    )

    assert response.status_code == 201
    assert response.get_json()["message"] == "Review added successfully"
