from flask import Flask, request, jsonify
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)

# Conexão Oracle no modo thin
DATABASE_URL = "oracle+oracledb://rm553764:fiap24@oracle.fiap.com.br:1521/orcl"
engine = create_engine(DATABASE_URL)

# Para criar uma nova tarefa
@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    title = data.get('title')
    description = data.get('description')

    if not title or not isinstance(title, str) or len(title.strip()) == 0:
        return jsonify({"error": "O título é obrigatório e deve ser uma string não vazia"}), 400
    if not description or not isinstance(description, str) or len(description.strip()) == 0:
        return jsonify({"error": "A descrição é obrigatória e deve ser uma string não vazia"}), 400

    try:
        with engine.connect() as connection:
            connection.execute(
                text("INSERT INTO tasks (title, description) VALUES (:title, :description)"),
                {"title": title, "description": description}
            )
            connection.commit()
        return jsonify({"message": "Tarefa criada com sucesso"}), 201
    except SQLAlchemyError as e:
        print(f"Erro ao inserir no banco de dados: {e}")
        return jsonify({"error": "Erro ao criar a tarefa"}), 500

# Para listar todas as tarefas
@app.route('/tasks', methods=['GET'])
def get_tasks():
    try:
        with engine.connect() as connection:
            result = connection.execute(text("SELECT * FROM tasks"))
            tasks = [{"id": row[0], "title": row[1], "description": row[2]} for row in result]
        return jsonify(tasks), 200
    except SQLAlchemyError as e:
        print(f"Erro ao consultar o banco de dados: {e}")
        return jsonify({"error": "Erro ao listar tarefas"}), 500

# Para atualizar uma tarefa
@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    data = request.get_json()
    title = data.get('title')
    description = data.get('description')

    if not title or not isinstance(title, str) or len(title.strip()) == 0:
        return jsonify({"error": "O título é obrigatório e deve ser uma string não vazia"}), 400
    if not description or not isinstance(description, str) or len(description.strip()) == 0:
        return jsonify({"error": "A descrição é obrigatória e deve ser uma string não vazia"}), 400

    try:
        with engine.connect() as connection:
            result = connection.execute(
                text("UPDATE tasks SET title=:title, description=:description WHERE id=:id"),
                {"title": title, "description": description, "id": id}
            )
            if result.rowcount == 0:
                return jsonify({"error": "Tarefa não encontrada"}), 404
            connection.commit()
        return jsonify({"message": "Tarefa atualizada com sucesso"}), 200
    except SQLAlchemyError as e:
        print(f"Erro ao atualizar no banco de dados: {e}")
        return jsonify({"error": "Erro ao atualizar a tarefa"}), 500

# Para deletar uma tarefa
@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    try:
        with engine.connect() as connection:
            result = connection.execute(
                text("DELETE FROM tasks WHERE id=:id"),
                {"id": id}
            )
            if result.rowcount == 0:
                return jsonify({"error": "Tarefa não encontrada"}), 404
            connection.commit()
        return jsonify({"message": "Tarefa deletada com sucesso"}), 200
    except SQLAlchemyError as e:
        print(f"Erro ao deletar no banco de dados: {e}")
        return jsonify({"error": "Erro ao deletar a tarefa"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
