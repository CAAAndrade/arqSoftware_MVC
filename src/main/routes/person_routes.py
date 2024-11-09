from flask import Blueprint, jsonify, request
from src.errors.error_handle import handle_error
from src.views.http_types.http_request import HttpRequest
from src.main.composer.person_creator_composer import person_creator_composer
from src.main.composer.person_finder_composer import person_finder_composer

person_routes_bp = Blueprint("person_routes", __name__)


@person_routes_bp.route("/people", methods=["POST"])
def create_person():
    try:
        http_request = HttpRequest(body=request.json)
        view = person_creator_composer()

        http_response = view.handle(http_request)

        return jsonify(http_response.body), http_response.status_code
    except Exception as exeption:
        http_response= handle_error(exeption)

        return jsonify(http_response.body), http_response.status_code


@person_routes_bp.route("/people/<person_id>", methods=["GET"])
def find_person(person_id):
    try:
        http_request = HttpRequest(params={"person_id": person_id})
        view = person_finder_composer()

        http_response = view.handle(http_request)

        return jsonify(http_response.body), http_response.status_code
    except Exception as exeption:
        http_response = handle_error(exeption)

        return jsonify(http_response.body), http_response.status_code