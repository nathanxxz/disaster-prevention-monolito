from extension import db

class AnaliseDesastre(db.Model):
    __tablename__ = "analise_desastres"
    id = db.Column(db.Integer, primary_key=True,  autoincrement=True)
    cidade = db.Column(db.String(45), nullable=False)
    estado = db.Column(db.String(2), nullable = False)
    chuva_dia = db.Column(db.Float, nullable=False)
    acumulado_3d = db.Column(db.Float,nullable=False)
    acumulado_7d = db.Column(db.Float,nullable=False)
    risco_nivel = db.Column(db.String(45),nullable=False)
    risco_probabilidade = db.Column(db.Float, nullable=False)
    cod_user = db.Column(db.Integer, db.ForeignKey("administradores.id"), nullable=False)
    data_analise = db.Column(db.Date, nullable=False)
    