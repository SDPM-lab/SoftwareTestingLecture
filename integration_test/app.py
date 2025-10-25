from flask import Flask, request, jsonify
from integration_test.db import insert_user

flask_app = Flask(__name__)

@flask_app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    username = data.get("username")
    if not username:
        return jsonify({"error": "Username required"}), 400
    insert_user(username)
    return jsonify({"message": f"User {username} registered"}), 201
