from extension import db
from models.user_admin_model import UsuarioAdministrador
from flask import request
from datetime import datetime, date
from flask_login import login_user, current_user, logout_user

class UsuarioAdministradorDao:

  def criarUsuarioAdmin(self):
     try:
        data = request.form
        if("nome" in data and "data_nascimento" in data and "email" in data and "senha" in data):
            usuario = UsuarioAdministrador(nome=data["nome"], data_nascimento=datetime.strptime(data["data_nascimento"], "%Y-%m-%d").date(), email=data["email"], senha=data["senha"], data_criacao_conta=date.today())
            db.session.add(usuario)
            db.session.commit()
            return True
            
     except Exception as e:
        db.session.rollback()
        print(e)
        return False
     
  def loginUsuarioAdmin(self):
     try:

       data = request.form
       admin = UsuarioAdministrador.query.filter_by(email=data.get("email")).first()
 
       if(admin):
         if(data.get("senha")==admin.senha):
           login_user(admin)
           return True
         
       return False
     except Exception as e:
          db.session.rollback()
          print(e)
          return False


  def logoutAdmin(self):
         logout_user()
         return True
     

  def buscarUsuarioAdminPorID(self,id):
       try:
          buscar = UsuarioAdministrador.query.get(id)
          if(buscar):
             return buscar
          
       except Exception as e:
          db.session.rollback()
          print(e)
          return False
       
  def listarTodosUsuariosAdmin(self):
       try:
          usuario = UsuarioAdministrador.query.filter_by(id=current_user.id).all()
          if(usuario):
             return usuario
       
       except Exception as e:
          db.session.rollback()
          print(e)
          return None
       
  def excluirUsuarioAdmin(self,id):
       try:
          existe = UsuarioAdministrador.query.get(id)
          if(existe):
             db.session.delete(existe)
             db.session.commit()
             return True
          if(not existe):
             return False
          
       except Exception as e:
         db.session.rollback()
         print(e)
         return False
    
  def atualizarUsuarioAdmin(self,id):   
       try:
          data = request.form
          atualizar = UsuarioAdministrador.query.get(id)
          if(atualizar):
             
             if("nome" in data):
                atualizar.nome = data["nome"]

             if("data_nascimento" in data):
                atualizar.data_nascimento = data["data_nascimento"]
            
             if("email" in data):
                atualizar.email = data["email"]
             
             if("senha" in data):
                atualizar.senha = data["senha"]
               
             db.session.commit()

             return True
          
          if(not atualizar):
             return False
          
       except Exception as e:
           db.session.rollback()
           print(e)
           return False
       
      