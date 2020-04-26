from flask import Blueprint, jsonify, request
from apps.aluno.aluno import insert_aluno, select_aluno


bp = Blueprint('alunos', __name__)
@bp.route('/alunos', methods=["GET"])
def select():
    return jsonify(select_aluno()), 200


@bp.route('/inserir/aluno', methods=["POST"])
def insert():
    body = request.get_json()
    insert_aluno(body)
    return jsonify("Aluno Inserido"), 201
