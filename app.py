from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/gamepasses")
def get_gamepasses():
    user_id = request.args.get("userId")
    if not user_id:
        return jsonify({"error": "Missing userId"}), 400

    try:
        url = f"https://catalog.roblox.com/v1/search/items?category=3&creatorTargetId={user_id}&limit=30&sortOrder=Asc"
        r = requests.get(url)
        r.raise_for_status()
        data = r.json()
        return jsonify(data.get("data", []))
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/")
def index():
    return "Proxy is running"
