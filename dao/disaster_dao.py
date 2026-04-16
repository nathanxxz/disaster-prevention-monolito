from models.disaster_model import AnaliseDesastre
from extension import db
from flask import request
from datetime import datetime
from flask_login import current_user


class DisasterDao:

    def criarDesastre(self):
        try:
            data = request.form
            
            if("cidade" in data and "estado" in data and "chuva_dia" in data and "acumulado_3d" in data and "acumulado_7d" in data and "risco_nivel" in data and "risco_probabilidade" in data and "data_analise" in data):
                analiseDesastre = AnaliseDesastre(cidade= data["cidade"], estado=data["estado"], chuva_dia=data["chuva_dia"], acumulado_3d= data["acumulado_3d"], acumulado_7d=data["acumulado_7d"],risco_nivel=data["risco_nivel"], risco_probabilidade=data["risco_probabilidade"],data_analise=datetime.strptime(data["data_analise"],"%Y-%m-%d").date(), cod_user=current_user.id)
                db.session.add(analiseDesastre)
                db.session.commit()
                return True
        
            
        except Exception as e:
            db.session.rollback()
            print(e)
            return False
        
    def buscarDesastrePorID(self,id):
        try:
            buscar = AnaliseDesastre.query.get(id)
            
            if(buscar):
              return buscar
            
        except Exception as e:
            db.session.rollback()
            print(e)
            return False
    
    def listarTodosDesastres(self):
        try:
            listar = AnaliseDesastre.query.all()
            if(listar):
                return listar
            
        except Exception as e:
            db.session.rollback()
            print(e)
            return False
    
    def excluirDesastre(self,id):
        try:
            buscar = AnaliseDesastre.query.get(id)

            if(buscar):
                db.session.delete(buscar)
                db.session.commit()
                return True
        
        except Exception as e:
            db.session.rollback()
            print(e)
            return False
        
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
                return True
        
        except Exception as e:
            db.session.rollback()
            print(e)
            return False
                    
                   
                    
                    
        
           


             

