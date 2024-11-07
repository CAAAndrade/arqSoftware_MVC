from flask import Blueprint, jsonify

pet_routes_bp = Blueprint("pet_routes", __name__)

@pet_routes_bp.route("/pets", methods=["GET"])
def list_pets():
    return jsonify({"Ola": "Mundo!"}), 200