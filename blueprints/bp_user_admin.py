from flask import Blueprint,request,render_template,redirect,url_for
from flask_login import login_user, logout_user, login_required, current_user
from extension import db

from dao.user_admin_dao import UsuarioAdministradorDao

adminDAO = UsuarioAdministradorDao()

bp_admin = Blueprint("admin",__name__,url_prefix="/admin")

@bp_admin.route("/login/admin", methods=["POST","GET"])
def loginUsuarioAdmin():
  try:
    if(request.method == "POST" or request.method == "GET"):
       sucesso = adminDAO.loginUsuarioAdmin()
       if(sucesso):
          return redirect(url_for("admin.dashboardAdmin"))
       return render_template("login_admin.html")
    
    return render_template("login_admin.html")
    
  except Exception as e:
    print(e)

@bp_admin.route("/dashboard")
@login_required
def dashboardAdmin():
    return render_template("dashboard_admin.html")

@bp_admin.route("/logout",methods=["POST"])
@login_required
def logoutUsuarioAdmin():
  try:
     adminDAO.logoutAdmin()
     return redirect(url_for("admin.loginUsuarioAdmin"))
    
  except Exception as e:
    print(e)



@bp_admin.route("/cadastrar", methods=["POST", "GET"])
def criarUsuarioAdmin():
    try:
     if(request.method == "POST"):
        adminDAO.criarUsuarioAdmin()
        return redirect(url_for("admin.loginUsuarioAdmin"))

     return render_template("cadastro_admin.html")
    
    except Exception as e:
      print(e)

@bp_admin.route("/buscar/<int:id>", methods=["GET"])
@login_required
def buscarUsuarioAdminPorID(id):
  try:
    if(request.method == "GET"):
      admin = adminDAO.buscarUsuarioAdminPorID(id)
      return render_template("buscar_admin.html", admin= admin)
    
  except Exception as e:
    print(e)

@bp_admin.route("/listar", methods=["GET"])
@login_required
def listarAdmins():
  try:
    if(request.method == "GET"):
      admins = adminDAO.listarTodosUsuariosAdmin()
      return render_template("listar_admins.html", admins = admins)
    
  except Exception as e:
    print(e)

@bp_admin.route("/excluir/<int:id>",methods=["POST"])
@login_required
def excluirUsuarioAdmin(id):
  try:
    if(request.method == "POST"):
      adminDAO.excluirUsuarioAdmin(id)
      return redirect(url_for("admin.listarAdmins"))
    
  except Exception as e:
    print(e)
   
@bp_admin.route("/atualizar/<int:id>", methods=["POST", "GET"])
@login_required
def atualizarAdmin(id):
  try:
    if(request.method == "POST"):
      adminDAO.atualizarUsuarioAdmin(id)
      return redirect(url_for('admin.listarAdmins'))
    
    admin = adminDAO.buscarUsuarioAdminPorID(id)
    return render_template("atualizar_admin.html", admin=admin)
    
  except Exception as e:
    print(e)