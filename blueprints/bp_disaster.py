from flask import Blueprint,request,render_template,redirect,url_for
from flask_login import login_user, logout_user, login_required, current_user
from extension import db
from decorators import admin_required

from dao.disaster_dao import DisasterDao

desastreDAO = DisasterDao()


bp_disaster = Blueprint("desastres",__name__, url_prefix="/desastres")

@bp_disaster.route("/criar", methods=["POST"])
@login_required
def criarDesastre():
    try:

        if(request.method == "POST"):
            desastreDAO.criarDesastre()
            return render_template("criar_desastre.html")
        
    except Exception as e:
        print(e)

@bp_disaster.route("/buscar/<int:id>", methods=["GET"])
@login_required
def buscarDesastrePorID(id):
    try:

        if(request.method == "GET"):
            desastreDAO.buscarDesastrePorID(id)
            return render_template("buscar_desastre.html")
        
    except Exception as e:
        print(e)

@bp_disaster.route("/listar", methods=["GET"])
@login_required
@admin_required
def listarDesastres():
    try:
        if(request.method == "GET"):
            desastreDAO.listarTodosDesastres()
            return render_template("listar_desastres.html")
        
    except Exception as e:
        print(e)

@bp_disaster.route("/excluir/<int:id>", methods=["POST"])
@login_required
@admin_required
def excluirDesastre(id):
    try:

        if(request.method == "POST"):
            desastreDAO.excluirDesastre(id)
            return render_template("excluir_desastre.html")
        
    except Exception as e:
        print(e)

@bp_disaster.route("/atualizar/<int:id>", methods=["POST"])
@login_required
@admin_required
def atualizarDesastre(id):
    try:
        if(request.method == "POST"):
            desastreDAO.atualizarDesastre(id)
            return render_template("atualizar_desastre.html")
        
    except Exception as e:
        print(e)