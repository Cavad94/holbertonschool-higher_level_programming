#!/usr/bin/python3
"""
A simple Flask API with user management.
"""
from flask import Flask, jsonify, request

app = Flask(__name__)

# Başlanğıc istifadəçi məlumatları
users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}


@app.route("/")
def home():
    """Welcome message."""
    return "Welcome to the Flask API!"


@app.route("/data")
def get_data():
    """Return a list of all usernames."""
    return jsonify(list(users.keys()))


@app.route("/status")
def get_status():
    """Return status OK."""
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    """Return user details."""
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """Add a new user."""
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = data
    return jsonify({"message": "User added", "user": data}), 201


if __name__ == "__main__":
    app.run()
