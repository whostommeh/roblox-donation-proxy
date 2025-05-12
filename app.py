from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/gamepasses")
def get_gamepasses():
    user_id = request.args.get("userId")
    if not user_id:
        return jsonify({"error": "Missing userId"}), 400

    try:
        r = requests.get(f"https://games.roblox.com/v1/users/{user_id}/game-passes?limit=100")
        r.raise_for_status()
        data = r.json()
        return jsonify(data.get("data", []))
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/")
def index():
    return "Proxy is running"
