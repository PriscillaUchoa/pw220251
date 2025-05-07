from sqlalchemy import Integer, String, Column
from model.conexao import Base, engine

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    data = Column(String, nullable=False)
   
    def __init__(self, nome, data):
        self.nome = nome
        self.data = data
    
    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'data': self.data
        }