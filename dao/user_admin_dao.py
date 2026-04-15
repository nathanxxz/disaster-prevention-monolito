from extension import db
from models.user_admin_model import UsuarioAdministrador
from flask import request
from datetime import datetime
from flask_login import login_user, login_required, logout_user

class UsuarioAdministradorDao:

  def criarUsuarioAdmin(self):
     try:
        data = request.form
        if("nome" in data and "data_nascimento" in data and "email" in data and "senha" in data and "cod_desastre" in data and "data_criacao_conta" in data):
            usuario = UsuarioAdministrador(nome=data["nome"], data_nascimento=datetime.strptime(data["data_nascimento"], "%Y-%m-%d").date(), email=data["email"], senha=data["senha"], cod_desastre=data["cod_desastre"], data_criacao_conta=datetime.strptime(data["data_criacao_conta"], "%Y-%m-%d").date())
            db.session.add(usuario)
            db.session.commit()
            return {"message": "Usuario criado com sucesso"},201
            
         
     except Exception as e:
        db.session.rollback()
        print(e)
        return {"message": "Erro ao criar usuario"},500
     
  def loginUsuarioCliente(self):
     try:

       data = request.form
       admin = UsuarioAdministrador.query.filter_by(email=data.get("email")).first()
 
       if(admin):
        if(data.get("senha")==admin.senha):
           login_user(admin)
           return {"message": "Login realizado com sucesso"},200
     except Exception as e:
          db.session.rollback()
          print(e)
          return {"message": "Erro ao fazer login"},500


  def logoutCliente(self):
     if(logout_user()):
         return {"message": "Saindo do sistema"},200
     

  def buscarUsuarioAdminPorID(self,id):
       try:
          buscar = UsuarioAdministrador.query.get(id)
          if(buscar):
             return ({
                "id": buscar.id,
                "nome": buscar.nome,
                "email": buscar.email,
             }),200
          
       except Exception as e:
          db.session.rollback()
          print(e)
          return {"message": "Erro ao buscar Usuario"},500
       
  def listarTodosUsuariosAdmin(self):
       try:
          usuario = UsuarioAdministrador.query.all()
          usuariosList = []
          
          for users in usuario:
             usuariosDate = {
                 "id": users.id,
                "nome": users.nome,
                "email": users.email,
             }
             usuariosList.append(usuariosDate)
          return (usuariosList),200
       
       except Exception as e:
          db.session.rollback()
          print(e)
          return {"message": "Erro ao listar Usuarios"},500
       

  def excluirUsuarioAdmin(self,id):
       try:
          existe = UsuarioAdministrador.query.get(id)
          if(existe):
             db.session.delete(existe)
             db.session.commit()
             return {"message": "Usuario excluido com sucesso"},200
          if(not existe):
             return {"message": "Esse usuario nao existe, nao tem como excluir"},404
          
       except Exception as e:
         db.session.rollback()
         print(e)
         return {"message": "Erro ao excluir"},500
    
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

             return{"message": "Usuario atualizado com sucesso"},200
          
          if(not atualizar):
             return{"message": "Nao existe usuario para atualizar"},404
          
       except Exception as e:
           db.session.rollback()
           print(e)
           return {"message": "Erro ao atualizar usuario"}
       
      