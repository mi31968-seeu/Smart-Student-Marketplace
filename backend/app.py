from flask import Flask, jsonify, request
from flask_cors import CORS
from database import get_connection, initialize_database, DATABASE_PATH
from models import row_to_dict


def create_app(database_path=DATABASE_PATH):
    app = Flask(__name__)
    CORS(app)
    initialize_database(database_path)

    @app.route("/", methods=["GET"])
    def home():
        return jsonify({"message": "Smart Student Marketplace API is running"})

    @app.route("/register", methods=["POST"])
    def register():
        data = request.get_json() or {}
        name = data.get("name", "").strip()
        email = data.get("email", "").strip().lower()
        password = data.get("password", "").strip()

        if not name or not email or not password:
            return jsonify({"error": "Name, email, and password are required"}), 400

        try:
            connection = get_connection(database_path)
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO users (name, email, password) VALUES (?, ?, ?)",
                (name, email, password),
            )
            connection.commit()
            user_id = cursor.lastrowid
            connection.close()
            return jsonify({"id": user_id, "name": name, "email": email}), 201
        except Exception:
            return jsonify({"error": "Email already exists"}), 409

    @app.route("/login", methods=["POST"])
    def login():
        data = request.get_json() or {}
        email = data.get("email", "").strip().lower()
        password = data.get("password", "").strip()

        connection = get_connection(database_path)
        user = connection.execute(
            "SELECT id, name, email FROM users WHERE email = ? AND password = ?",
            (email, password),
        ).fetchone()
        connection.close()

        if user is None:
            return jsonify({"error": "Invalid email or password"}), 401

        return jsonify(row_to_dict(user)), 200

    @app.route("/services", methods=["POST"])
    def create_service():
        data = request.get_json() or {}
        required_fields = ["user_id", "title", "description", "category", "price"]

        if any(field not in data or data[field] in ["", None] for field in required_fields):
            return jsonify({"error": "All service fields are required"}), 400

        connection = get_connection(database_path)
        cursor = connection.cursor()
        cursor.execute(
            """
            INSERT INTO services (user_id, title, description, category, price)
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                data["user_id"],
                data["title"],
                data["description"],
                data["category"],
                float(data["price"]),
            ),
        )
        connection.commit()
        service_id = cursor.lastrowid
        connection.close()

        return jsonify({"id": service_id, "message": "Service created successfully"}), 201

    @app.route("/services", methods=["GET"])
    def list_services():
        search = request.args.get("search", "").strip().lower()
        category = request.args.get("category", "").strip().lower()

        query = "SELECT * FROM services WHERE 1=1"
        params = []

        if search:
            query += " AND (LOWER(title) LIKE ? OR LOWER(description) LIKE ?)"
            params.extend([f"%{search}%", f"%{search}%"])

        if category:
            query += " AND LOWER(category) = ?"
            params.append(category)

        connection = get_connection(database_path)
        services = connection.execute(query, params).fetchall()
        connection.close()

        return jsonify([row_to_dict(service) for service in services]), 200

    @app.route("/messages", methods=["POST"])
    def send_message():
        data = request.get_json() or {}
        required_fields = ["sender_id", "receiver_id", "content"]

        if any(field not in data or data[field] in ["", None] for field in required_fields):
            return jsonify({"error": "Sender, receiver, and content are required"}), 400

        connection = get_connection(database_path)
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO messages (sender_id, receiver_id, content) VALUES (?, ?, ?)",
            (data["sender_id"], data["receiver_id"], data["content"]),
        )
        connection.commit()
        message_id = cursor.lastrowid
        connection.close()

        return jsonify({"id": message_id, "message": "Message sent successfully"}), 201

    @app.route("/reviews", methods=["POST"])
    def add_review():
        data = request.get_json() or {}
        required_fields = ["service_id", "reviewer_id", "rating", "comment"]

        if any(field not in data or data[field] in ["", None] for field in required_fields):
            return jsonify({"error": "All review fields are required"}), 400

        rating = int(data["rating"])
        if rating < 1 or rating > 5:
            return jsonify({"error": "Rating must be between 1 and 5"}), 400

        connection = get_connection(database_path)
        cursor = connection.cursor()
        cursor.execute(
            """
            INSERT INTO reviews (service_id, reviewer_id, rating, comment)
            VALUES (?, ?, ?, ?)
            """,
            (data["service_id"], data["reviewer_id"], rating, data["comment"]),
        )
        connection.commit()
        review_id = cursor.lastrowid
        connection.close()

        return jsonify({"id": review_id, "message": "Review added successfully"}), 201

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
