"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import operator_controller
from t08_flask_mysql.app.my_project.auth.domain import Operator

operator_bp = Blueprint('operators', __name__, url_prefix='/operators')

@operator_bp.get('')
def get_all_operators() -> Response:
    """
    Gets all operator objects using the Operator Controller.
    :return: Response object
    """
    return make_response(jsonify(operator_controller.find_all()), HTTPStatus.OK)

@operator_bp.post('')
def create_operator() -> Response:
    """
    Creates a new operator.
    :return: Response object
    """
    content = request.get_json()
    operator = Operator.create_from_dto(content)
    operator_controller.create(operator)
    return make_response(jsonify(operator.put_into_dto()), HTTPStatus.CREATED)

@operator_bp.get('/<int:operator_id>')
def get_operator(operator_id: int) -> Response:
    """
    Gets an operator by ID.
    :return: Response object
    """
    return make_response(jsonify(operator_controller.find_by_id(operator_id)), HTTPStatus.OK)

@operator_bp.put('/<int:operator_id>')
def update_operator(operator_id: int) -> Response:
    """
    Updates an operator by ID.
    :return: Response object
    """
    content = request.get_json()
    operator = Operator.create_from_dto(content)
    operator_controller.update(operator_id, operator)
    return make_response("Operator updated", HTTPStatus.OK)

@operator_bp.patch('/<int:operator_id>')
def patch_operator(operator_id: int) -> Response:
    """
    Patches an operator by ID.
    :return: Response object
    """
    content = request.get_json()
    operator_controller.patch(operator_id, content)
    return make_response("Operator updated", HTTPStatus.OK)

@operator_bp.delete('/<int:operator_id>')
def delete_operator(operator_id: int) -> Response:
    """
    Deletes an operator by ID.
    :return: Response object
    """
    operator_controller.delete(operator_id)
    return make_response("Operator deleted", HTTPStatus.OK)