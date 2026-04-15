from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()

login = LoginManager()

@login.user_loader
def load_user(user_id):
    from models.user_admin_model import UsuarioAdministrador
    from models.user_cliente_model import UsuarioCliente

    try:
        role , id_numerico = user_id.split("_")
        id_numerico = int(id_numerico)

        if(role == "admin"):
            return UsuarioAdministrador.query.get(id_numerico)
        
        elif(role == "cliente"):
            return UsuarioCliente.query.get(id_numerico)
    
    except ValueError:
        return None
    
    return None
