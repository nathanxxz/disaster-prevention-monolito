from extension import db
from flask_login import UserMixin

class UsuarioCliente(db.Model,UserMixin):
    __tablename__ = "clientes"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(45), nullable=False)
    data_nascimento =  db.Column(db.Date,nullable=False)
    email = db.Column(db.String(45), nullable=False, unique=True)
    senha = db.Column(db.String(255), nullable=False)
    data_criacao_conta = db.Column(db.Date, nullable=False)


    def __repr__(self):
        return f"Admin('{self.nome}', '{self.email}', '{self.id}')"
    
    @property
    def is_admin(self):
        return False
    
    def get_id(self):
        return f"cliente_{self.id}"
