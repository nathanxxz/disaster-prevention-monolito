from extension import db
from flask_login import UserMixin

class UsuarioAdministrador(db.Model,UserMixin):
    __tablename__ = "administradores"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(45), nullable=False)
    data_nascimento =  db.Column(db.Date,nullable=False)
    email = db.Column(db.String(45), nullable=False, unique=True)
    senha = db.Column(db.String(255), nullable=False)
    data_criacao_conta = db.Column(db.Date, nullable=False)
    desastres = db.relationship("AnaliseDesastre", backref="usuario", lazy=True)


    def __repr__(self):
        return f"Admin('{self.nome}', '{self.email}')"
    
    @property
    def is_admin(self):
        return True
    
    def get_id(self):
        return f"admin_{self.id}"

