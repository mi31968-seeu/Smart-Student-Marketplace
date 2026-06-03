from flask import Flask, jsonify, request

app = Flask(__name__)

users = []
services = []
reviews = []

@app.route("/")
def home():
    return jsonify({"message": "Smart Student Marketplace API"})

@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    if not data.get("name") or not data.get("email") or not data.get("password"):
        return jsonify({"error": "Missing registration data"}), 400

    if any(user["email"] == data["email"] for user in users):
        return jsonify({"error": "Email already exists"}), 409

    users.append(data)
    return jsonify({"message": "User registered", "user": data}), 201

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    user = next(
        (user for user in users if user["email"] == data.get("email") and user["password"] == data.get("password")),
        None
    )

    if not user:
        return jsonify({"error": "Invalid email or password"}), 401

    return jsonify({"message": "Login successful", "user": user}), 200

@app.route("/services", methods=["GET", "POST"])
def service_collection():
    if request.method == "POST":
        data = request.get_json()
        required_fields = ["title", "category", "description", "price", "owner"]

        if not all(field in data and data[field] for field in required_fields):
            return jsonify({"error": "Missing service data"}), 400

        services.append(data)
        return jsonify({"message": "Service added", "service": data}), 201

    search = request.args.get("search", "").lower()

    if search:
        filtered = [
            service for service in services
            if search in service["title"].lower()
            or search in service["category"].lower()
            or search in service["description"].lower()
        ]
        return jsonify(filtered)

    return jsonify(services)

@app.route("/reviews", methods=["GET", "POST"])
def review_collection():
    if request.method == "POST":
        data = request.get_json()
        reviews.append(data)
        return jsonify({"message": "Review added", "review": data}), 201

    return jsonify(reviews)

if __name__ == "__main__":
    app.run(debug=True)
