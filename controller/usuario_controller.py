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

@app.route('/usuarios', methods=['GET'])
def get_usuarios():
    db = sessionlocal()
    usuarios = db.query(Usuario).all()
    return jsonify([usuario.to_dict() for usuario in usuarios]), 200

@app.route('/usuarios/<int:id>', methods=['GET'])
def get_usuario(id):
    db = sessionlocal()
    usuario = db.query(Usuario).get(id)
    if usuario:
        return jsonify(usuario.to_dict()), 200
    else:
        return jsonify({'message': 'Usuário não encontrado!'}), 404
    
@app.route('/usuarios/<int:id>', methods=['DELETE'])
def delete_usuario(id):
    db = sessionlocal()
    usuario = db.query(Usuario).get(id)
    if usuario:
        db.delete(usuario)
        db.commit()
        return jsonify({'message': 'Usuário deletado!'}), 204
    else:
        return jsonify({'message': 'Usuário não encontrado!'}), 404

@app.route('/usuarios', methods=['POST'])
def create_usuario():
    db = sessionlocal()
    data = request.get_json()
    usuario = Usuario(nome=data['nome'], data=data['aniversário'])
    db.add(usuario)
    db.commit()
    return jsonify({'message': 'Usuário criado com sucesso!', 
                   'usuário': usuario.to_dict()}), 201

@app.route('/usuarios/<int:id>', methods=['PUT'])    
def update_usuario(id):
    db = sessionlocal()
    data = request.get_json()
    usuario = db.query(Usuario).get(id)
    if usuario:
        usuario.nome = data['nome']
        usuario.data = data['aniversário']
        db.commit()
        return jsonify({'message': 'Usuário atualizado com sucesso!', 
                       'usuário': usuario.to_dict()}), 200
    else:
        return jsonify({'message': 'Usuário não encontrado!'}), 404