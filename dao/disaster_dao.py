from models.disaster_model import AnaliseDesastre
from extension import db
from flask import request
from datetime import datetime


class DisasterDao:

    def criarDesastre(self):
        try:
            data = request.form
            
            if("cidade" in data and "estado" in data and "chuva_dia" in data and "acumulado_3d" in data and "acumulado_7d" in data and "risco_nivel" in data and "risco_probabilidade" in data and "data_analise" in data):
                analiseDesastre = AnaliseDesastre(cidade= data["cidade"], estado=data["estado"], chuva_dia=data["chuva_dia"], acumulado_3d= data["acumulado_3d"], acumulado_7d=data["acumulado_7d"],risco_nivel=data["risco_nivel"], risco_probabilidade=data["risco_probabilidade"],data_analise=datetime.strptime(data["data_analise"],"%Y-%m-%d").date())
                db.session.add(analiseDesastre)
                db.session.commit()
                return {"message": "Criado com sucesso"},201
        
            
        except Exception as e:
            db.session.rollback()
            print(e)
            return {"message": "Erro ao criar desastre"},500
        
    def buscarDesastrePorID(self,id):
        try:
            buscar = AnaliseDesastre.query.get(id)
            
            if(buscar):
                return({
                    "cidade": buscar.cidade,
                    "estado": buscar.estado,
                    "acumulado_3d": buscar.acumulado_3d,
                    "acumulado_7d": buscar.acumulado_7d,
                    "risco_nivel": buscar.risco_nivel,
                    "risco_probabilidade": buscar.risco_probabilidade,
                    "data_analise": buscar.data_analise
                }),200
            
        except Exception as e:
            db.session.rollback()
            print(e)
            return {"message": "Erro ao buscar desastre"},500
    
    def listarTodosDesastres(self):
        try:
            listar = AnaliseDesastre.query.all()
            desastres =[]
            
            if(listar):
                for d in listar:
                    desastresDate = {
                    "cidade": d.cidade,
                    "estado": d.estado,
                    "acumulado_3d": d.acumulado_3d,
                    "acumulado_7d": d.acumulado_7d,
                    "risco_nivel": d.risco_nivel,
                    "risco_probabilidade": d.risco_probabilidade,
                    "data_analise": d.data_analise
                    }
                    desastres.append(desastresDate)
                return (desastres),200
            
        except Exception as e:
            db.session.rollback()
            print(e)
            return {"message": "Erro ao listar desastres"},500
    
    def excluirDesastre(self,id):
        try:
            buscar = AnaliseDesastre.query.get(id)

            if(buscar):
                db.session.delete(buscar)
                db.session.commit()
                return {"message": "Desastre apagado com sucesso"},200
        
        except Exception as e:
            db.session.rollback()
            print(e)
            return {"message": "Erro ao excluir desastre"},500
        
    def atualizarDesastre(self,id):
        try:
            data = request.form

            buscar = AnaliseDesastre.query.get(id)
            
            if(buscar):

                if("cidade" in data):
                    buscar.cidade = data["cidade"]
                
                if("estado" in data):
                    buscar.estado = data["estado"]
                
                if("acumulado_3d" in data):
                    buscar.acumulado_3d = data["acumulado_3d"]
                
                if("acumulado_7d" in data):
                    buscar.acumulado_7d = data["acumulado_7d"]
                
                if("risco_nivel" in data):
                    buscar.risco_nivel = data["risco_nivel"]
                
                if("risco_probabilidade" in data):
                    buscar.risco_probabilidade = data["risco_probabilidade"]

                db.session.commit()
                return {"message": "Desastre atualizado com sucesso"},200
        
        except Exception as e:
            db.session.rollback()
            print(e)
            return {"message": "Erro ao atualizar desastre"},500
                    
                   
                    
                    
        
           


             

