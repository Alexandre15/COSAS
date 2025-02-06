from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)



# Função para conectar ao banco de dados
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Rota para a página inicial
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nome = request.form['nome']
        sobrenome = request.form['sobrenome']
        
        # Adiciona o usuário ao banco de dados
        conn = get_db_connection()
        conn.execute('INSERT INTO usuarios (nome, sobrenome) VALUES (?, ?)', (nome, sobrenome))
        conn.commit()
        conn.close()
        
        return redirect(url_for('index'))

    # Lista os usuários cadastrados
    conn = get_db_connection()
    usuarios = conn.execute('SELECT * FROM usuarios').fetchall()
    conn.close()
    return render_template('test3.html', usuarios=usuarios)

# Inicializa o banco de dados
def init_db():
    conn = get_db_connection()
    conn.execute('CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, sobrenome TEXT)')
    conn.close()

if __name__ == '__main__':
    init_db()  # Cria a tabela se não existir
    app.run(host='0.0.0.0', port=5000)