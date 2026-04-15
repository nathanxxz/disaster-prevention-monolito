from flask import Blueprint,request,render_template,redirect,url_for
from flask_login import login_user, logout_user, login_required, current_user
from extension import db
from decorators import admin_required

from dao.disaster_dao import DisasterDao

desastreDAO = DisasterDao()


bp_disaster = Blueprint("desastres",__name__, url_prefix="/desastres")

@bp_disaster.route("/criar", methods=["POST", "GET"])
@login_required
def criarDesastre():
    try:

        if(request.method == "POST" or request.method == "GET"):
            criar = desastreDAO.criarDesastre()
            return render_template("criar_desastre.html", desastres=criar)
        
    except Exception as e:
        print(e)

@bp_disaster.route("/buscar/<int:id>", methods=["GET"])
@login_required
def buscarDesastrePorID(id):
    try:

        if(request.method == "GET"):
            buscar = desastreDAO.buscarDesastrePorID(id)
            return render_template("buscar_desastre.html",desastres=buscar)
        
    except Exception as e:
        print(e)

@bp_disaster.route("/listar", methods=["GET"])
@login_required
@admin_required
def listarDesastres():
    try:
        if(request.method == "GET"):
           listar = desastreDAO.listarTodosDesastres()
           return render_template("listar_desastres.html", desastres= listar)
        
    except Exception as e:
        print(e)

@bp_disaster.route("/excluir/<int:id>", methods=["POST"])
@login_required
@admin_required
def excluirDesastre(id):
    try:

        if(request.method == "POST"):
            excluir = desastreDAO.excluirDesastre(id)
            return render_template("excluir_desastre.html", desastres=excluir)
        
    except Exception as e:
        print(e)

@bp_disaster.route("/atualizar/<int:id>", methods=["POST"])
@login_required
@admin_required
def atualizarDesastre(id):
    try:
        if(request.method == "POST"):
            atualizar = desastreDAO.atualizarDesastre(id)
            return render_template("atualizar_desastre.html", desastres=atualizar)
        
    except Exception as e:
        print(e)