'''
Descripción:
Programa para administrar la base de datos de recetas.db.
'''

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Recetas(db.Model):
    __tablename__= "recetas"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String)
    ingredientes = db.Column(db.String)
    categoria = db.Column(db.String)

    def __repr__(self):
        return f"Receta: {self.nombre}, ingredientes: {self.ingredientes}, categoría: {self.categoria}"

def create_squema():
    #crear la tabla
    db.create_all()
