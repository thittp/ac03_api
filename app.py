from flask import Flask, jsonify
from apps.aluno.aluno_route import bp as bp_alunos
from apps.professor.professor_route import bp as bp_professores
from apps.disciplinas.disciplinas_route import bp as bp_disciplinas

app = Flask('app')
app.register_blueprint(bp_alunos)
app.register_blueprint(bp_professores)
app.register_blueprint(bp_disciplinas)

@app.route('/')
def index():
  return jsonify("Bem Vindos!!!")


app.run(host='localhost', port='5000', debug=True)
