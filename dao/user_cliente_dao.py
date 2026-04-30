from extension import db
from models.user_cliente_model import UsuarioCliente
from flask import request
from datetime import datetime, date
from flask_login import login_user, login_required, logout_user

class UsuarioClienteDao:
  

  def criarUsuarioCliente(self):
     try:
        data = request.form
        if("nome" in data and "data_nascimento" in data and "email" in data and "senha" in data):
            usuario = UsuarioCliente(nome=data["nome"], data_nascimento=datetime.strptime(data["data_nascimento"], "%Y-%m-%d").date(), email=data["email"], senha=data["senha"], data_criacao_conta=date.today())
            db.session.add(usuario)
            db.session.commit()
            return usuario
            
     except Exception as e:
        db.session.rollback()
        print(e)
        return False
  
  def loginUsuarioCliente(self):
     try:
       data = request.form
       cliente = UsuarioCliente.query.filter_by(email=data.get("email")).first()
       if(cliente):
         if(data.get("senha")==cliente.senha):
           login_user(cliente)
           return True
         
       return False
     except Exception as e:
          db.session.rollback()
          print(e)
          return True

  def logoutCliente(self):
         logout_user()
         return True
     
  def buscarUsuarioClientePorID(self,id):
       try:
          buscar = UsuarioCliente.query.get(id)
          if(buscar):
             return buscar
                   
       except Exception as e:
          db.session.rollback()
          print(e)
          return False
       
  def listarTodosUsuariosClientes(self):
       try:
          usuario = UsuarioCliente.query.all()
          if(usuario):
             return usuario
             
       except Exception as e:
          db.session.rollback()
          print(e)
          return False
       
  def excluirUsuarioCliente(self,id):
       try:
          existe = UsuarioCliente.query.get(id)
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
    
  def atualizarUsuarioCliente(self,id):
       try:
          data = request.form
          atualizar = UsuarioCliente.query.get(id)
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
       
      