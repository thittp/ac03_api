from flask import Blueprint, jsonify, request
from apps.professor.professor import insert_professor, select_professor


bp = Blueprint('professores', __name__)
@bp.route('/professores', methods=["GET"])
def select():
    return jsonify(select_professor()), 200


@bp.route('/inserir/professor', methods=["POST"])
def insert():
    body = request.get_json()
    insert_professor(body)
    return jsonify("Professor Inserido"), 201
