from flask import Blueprint, jsonify, request
from apps.disciplinas.disciplina import inserir_disciplina, select_disciplinas


bp = Blueprint('disciplinas', __name__)
# @bp.route('/professores', methods=["GET"])
# def select():
#     return jsonify(select_professor()), 200


@bp.route('/inserir/disciplina', methods=["POST"])
def insert():
    body = request.get_json()
    inserir_disciplina(body)
    return jsonify("Disciplina Inserida"), 201


@bp.route('/disciplinas', methods=["GET"])
def select():
    return jsonify(select_disciplinas()), 200


