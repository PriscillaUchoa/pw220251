from app import app
from flask import render_template, request, jsonify
from sqlalchemy.orm import sessionmaker
from model.conexao import engine
from model.usuario import Usuario

sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@app.route('/usuarios', methods=['GET'])

def usuarios():
    db = sessionlocal()
    usuarios = db.query(Usuario).all()
    return jsonify([usuario.to_dict() for usuario in usuarios]), 200

@app.route('/usuarios/novo', methods=['GET'])
def novo():
    return render_template("index.html")

#Criando a rota para salvar o usuario no banco de dados
@app.route('/usuarios/salvar', methods=['POST'])
def create():  
    db = sessionlocal()
    usuario = Usuario(nome = request.form['nome'], data = request.form['aniversario'])
    db.add(usuario)
    db.commit()
    return jsonify({'message': 'Salvo com sucesso!'}), 200