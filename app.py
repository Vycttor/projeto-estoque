from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
from datetime import datetime


app = Flask(__name__)
app.secret_key = "segredo"

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    produtos = conn.execute('SELECT * FROM produto').fetchall()
    conn.close()
    return render_template('index.html', produtos=produtos)

@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':
        nome = request.form['nome']
        codigo = request.form['codigo']
        fornecedor = request.form['fornecedor']
        quantidade = int(request.form['quantidade'])
        estoque_minimo = int(request.form['estoque_minimo'])
        preco = float(request.form['preco'])
        data_cadastro = datetime.now().strftime('%d-%m-%Y')
        conn = get_db_connection()
        conn.execute('INSERT INTO produto (nome, codigo, fornecedor, quantidade, estoque_minimo, preco, data_cadastro) VALUES (?, ?, ?, ?, ?, ?, ?)',
                     (nome, codigo, fornecedor, quantidade, estoque_minimo, preco, data_cadastro))
        conn.commit()
        conn.close()
        flash('Produto cadastrado com sucesso!')
        return redirect(url_for('index'))
    return render_template('cadastrar.html')

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    conn = get_db_connection()
    produto = conn.execute('SELECT * FROM produto WHERE id = ?', (id,)).fetchone()
    if request.method == 'POST':
        nome = request.form['nome']
        codigo = request.form['codigo']
        fornecedor = request.form['fornecedor']
        quantidade = int(request.form['quantidade'])
        estoque_minimo = int(request.form['estoque_minimo'])
        preco = float(request.form['preco'])
        conn.execute('UPDATE produto SET nome = ?, codigo = ?, fornecedor = ?, quantidade = ?, estoque_minimo = ?, preco = ? WHERE id = ?',
                     (nome, codigo, fornecedor, quantidade, estoque_minimo, preco, id))
        conn.commit()
        conn.close()
        flash('Produto atualizado com sucesso!')
        return redirect(url_for('index'))
    conn.close()
    return render_template('editar.html', produto=produto)

@app.route('/excluir/<int:id>')
def excluir(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM produto WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('Produto excluído com sucesso!')
    return redirect(url_for('index'))

@app.route('/entrada/<int:id>', methods=['POST'])
def entrada(id):
    quantidade = int(request.form['quantidade'])
    conn = get_db_connection()
    produto = conn.execute('SELECT quantidade FROM produto WHERE id = ?', (id,)).fetchone()
    nova_quantidade = produto['quantidade'] + quantidade
    conn.execute('UPDATE  produto SET quantidade = ? WHERE id = ?', (nova_quantidade, id))
    conn.commit()
    conn.close()
    flash('Entrada de estoque registrada')
    return redirect(url_for('index'))

@app.route('/saida/<int:id>', methods=['POST'])
def saida(id):
    quantidade = int(request.form['quantidade'])
    conn = get_db_connection()
    produto = conn.execute('SELECT quantidade FROM  produto WHERE id = ?', (id,)).fetchone()
    if quantidade > produto['quantidade']:
        flash('Saída maior que a quantidade disponível')
    else:
        nova_quantidade = produto['quantidade'] - quantidade
        conn.execute('UPDATE produto SET quantidade = ? WHERE id = ?', (nova_quantidade, id))
        conn.commit()
        flash('Saída de estoque registrada!')
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)