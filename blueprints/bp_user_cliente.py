from flask import Blueprint,request,render_template,redirect,url_for
from flask_login import login_user, logout_user, login_required, current_user
from extension import db
from decorators import admin_required

from dao.user_cliente_dao import UsuarioClienteDao


clienteDAO = UsuarioClienteDao()

bp_cliente = Blueprint("cliente",__name__,url_prefix="/cliente")


@bp_cliente.route("/login/cliente", methods=["POST","GET"])
def loginUsuarioCliente():
  try:

    if(request.method == "POST" or request.method == "GET"):
       sucesso = clienteDAO.loginUsuarioCliente()
       if(sucesso):
          return redirect(url_for("cliente.dashboardCliente"))
       return render_template("login_cliente.html")
    return render_template("login_cliente.html")
    
  except Exception as e:
    print(e)

@bp_cliente.route("/dashboard")
@login_required
def dashboardCliente():
    return render_template("dashboard_cliente.html")


@bp_cliente.route("/logout",methods=["POST", "GET"])
@login_required
def logoutUsuarioCliente():
  try:
     
     clienteDAO.logoutCliente()
     return redirect(url_for("cliente.loginUsuarioCliente"))
  
  except Exception as e:
    print(e)


@bp_cliente.route("/cadastrar", methods=["POST", "GET"])
def criarUsuarioCliente():
    try:
  
     if(request.method == "POST"):
        sucesso = clienteDAO.criarUsuarioCliente()
        if(sucesso):
          return redirect(url_for("cliente.dashboardCliente"))
        return render_template("login_cliente.html")
     return render_template("cadastro_cliente.html")
    
    except Exception as e:
      print(e)

@bp_cliente.route("/buscar/<int:id>", methods=["GET"])
@login_required
@admin_required
def buscarUsuarioClientePorID(id):
  try:

    if(request.method == "GET"):
      cliente =  clienteDAO.buscarUsuarioClientePorID(id)
      return render_template("buscar_cliente.html", cliente = cliente)
    
  except Exception as e:
    print(e)

@bp_cliente.route("/listar", methods=["GET"])
@login_required
@admin_required
def listarClientes():
  try:

    if(request.method == "GET"):
      clientes = clienteDAO.listarTodosUsuariosClientes()
      return render_template("listar_clientes.html", clientes = clientes)
    
  except Exception as e:
    print(e)

@bp_cliente.route("/excluir/<int:id>",methods=["POST"])
@login_required
@admin_required
def excluirUsuarioCliente(id):
  try:

    if(request.method == "POST"):
      clienteDAO.excluirUsuarioCliente(id)
      return redirect(url_for("cliente.listarClientes"))
    
  except Exception as e:
    print(e)
   
@bp_cliente.route("/atualizar/<int:id>", methods=["POST", "GET"])
@login_required
def atualizarCliente(id):
  try:

    if(request.method == "POST"):
      clienteDAO.atualizarUsuarioCliente(id)
      return render_template("cliente.listarClientes")
    
    cliente = clienteDAO.buscarUsuarioClientePorID(id)
    return render_template("atualizar_cliente.html", cliente=cliente)
    
  except Exception as e:
    print(e)