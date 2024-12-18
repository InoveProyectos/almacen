#controlador de la base de datos que se va a usar
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

#modelo de la base de datos
class Recetas(db.Model):
    __tablename__= "recetas"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String)
    ingredientes = db.Column(db.String)
    categoria = db.Column(db.String)

    def __repr__(self):
        return f"Receta: {self.nombre}, ingredientes: {self.ingredientes}, categoría: {self.categoria}"
