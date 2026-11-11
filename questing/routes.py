from flask import Blueprint, jsonify

quests_bp = Blueprint("quests", __name__)


@quests_bp.get("/health")
def health():
    return jsonify({"status": "users ok"})