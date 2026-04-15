from flask import Blueprint,request,render_template,redirect,url_for
from flask_login import login_user, logout_user, login_required, current_user
from extension import db

from dao.user_admin_dao import UsuarioAdministradorDao

adminDAO = UsuarioAdministradorDao()

bp_admin = Blueprint("admin",__name__,url_prefix="/admin")

bp_admin.route("/login/admin", methods=["POST"])
def loginUsuarioAdmin():
  try:

    if(request.method == "POST"):
      adminDAO.loginUsuarioAdmin()
      return render_template("loginAdmin.html")
    
  except Exception as e:
    print(e)

@bp_admin.route("/logout",methods=["POST"])
@login_required
def logoutUsuarioAdmin():
  try:

    if(request.method == "POST"):
      adminDAO.logoutAdmin()
      return render_template("loginAdmin.html")
    
  except Exception as e:
    print(e)



@bp_admin.route("/cadastrar", methods=["POST"])
def criarUsuarioAdmin():
    try:
       
     if(request.method == "POST"):
      adminDAO.criarUsuarioAdmin()
      return render_template("cadastroAdmin.html")
    
    except Exception as e:
      print(e)

@bp_admin.route("/buscar/<int:id>", methods=["GET"])
@login_required
def buscarUsuarioAdminPorID(id):
  try:

    if(request.method == "GET"):
      adminDAO.buscarUsuarioAdminPorID(id)
      return render_template("buscarAdmin.html")
    
  except Exception as e:
    print(e)

@bp_admin.route("/listar", methods=["GET"])
@login_required
def listarAdmins():
  try:

    if(request.method == "GET"):
      adminDAO.listarTodosUsuariosAdmin()
      return render_template("listarAdmin.html")
    
  except Exception as e:
    print(e)

@bp_admin.route("/excluir/<int:id>",methods=["POST"])
@login_required
def excluirUsuarioAdmin(id):
  try:

    if(request.method == "POST"):
      adminDAO.excluirUsuarioAdmin(id)
      return render_template("excluirAdmin.html")
    
  except Exception as e:
    print(e)
   
@bp_admin.route("/atualizar/<int:id>", methods=["POST"])
@login_required
def atualizarAdmin(id):
  try:

    if(request.method == "POST"):
      adminDAO.atualizarUsuarioAdmin(id)
      return render_template("atualizarAdmin.html")
    
  except Exception as e:
    print(e)