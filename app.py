from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)


# Função para conectar ao banco de dados
def get_db_connection():
    conn = sqlite3.connect('banco.db')
    conn.row_factory = sqlite3.Row
    return conn


# Rota para a página inicial
@app.route('/')
def inicio():
    return render_template("telainicial.html")


# Rota para listar todos os usuários
@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM usuarios')
    usuarios = cursor.fetchall()
    conn.close()
    return render_template("listar_usuarios.html", usuarios=usuarios)


# Rota para a página de cadastro
@app.route('/cadastrar_usuario', methods=['GET'])
def pagina_cadastro():
    return render_template("cadastrar_usuario.html")  # Renderiza a página de cadastro


# Rota para cadastrar um usuário
@app.route('/usuarios', methods=['POST'])
def cadastrar_usuario():
    novo_usuario = request.form  # Obtenha os dados do formulário
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO usuarios (nome, sobrenome, idade, cpf) VALUES (?, ?, ?, ?)',
                   (novo_usuario['nome'], novo_usuario['sobrenome'], novo_usuario['idade'], novo_usuario['cpf']))
    conn.commit()
    conn.close()
    return "Usuário cadastrado com sucesso", 201


# Rota para a página de atualização
@app.route('/atualizar_usuario/<int:id>', methods=['GET'])
def pagina_atualizar(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM usuarios WHERE id = ?', (id,))
    usuario = cursor.fetchone()
    conn.close()
    return render_template("atualizar_usuario.html",
                           usuario=usuario)  # Renderiza a página de atualização de cadastro com o usuário


# Rota para atualizar um usuário
@app.route('/usuarios/<int:id>', methods=['PUT'])
def atualizar_usuario(id):
    usuario_atualizado = request.form
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE usuarios SET nome=?, sobrenome=?, idade=?, cpf=? WHERE id=?',
                   (usuario_atualizado['nome'], usuario_atualizado['sobrenome'], usuario_atualizado['idade'],
                    usuario_atualizado['cpf'], id))
    conn.commit()
    conn.close()
    return "Usuário atualizado com sucesso"


# Rota para a página de exclusão
@app.route('/excluir_usuario/<int:id>', methods=['GET'])
def pagina_excluir(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM usuarios WHERE id = ?', (id,))
    usuario = cursor.fetchone()
    conn.close()
    return render_template("excluir_usuario.html", usuario=usuario)


# Rota para excluir um usuário
@app.route('/usuarios/<int:id>', methods=['DELETE'])
def excluir_usuario(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM usuarios WHERE id=?', (id,))
    conn.commit()
    conn.close()
    return "Usuário excluído com sucesso"


if __name__ == '__main__':
    app.run(debug=True)
