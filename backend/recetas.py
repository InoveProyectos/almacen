'''
Recetas DB Manager
-----------------------
Descripción:
Programa para administrar la base de datos de recetas.db.
'''

from models import db, Recetas
from flask_sqlalchemy import SQLAlchemy

#CREAR ESQUEMA DE LA TABLA
def create_squema():
    db.create_all()

#TRAER TODAS LAS RECETAS DISPONIBLES
def obtener_todo():
    query = db.session.query(Recetas)
    data = []
    for i in query:
        json_result = {}
        json_result['Id']= i.id
        json_result['Nombre']= i.nombre
        json_result['Ingredientes']= i.ingredientes
        json_result['Categoria']= i.categoria
        data.append(json_result)
    return data

#FILTRAR REGISTRO DE LA DB POR EL ID
def filtrar_id(id):
    json_result_list=[]
    query = db.session.query(Recetas).filter(Recetas.id==id).all()
    for i in query:
        json_result= {}
        json_result['Id']= i.id
        json_result['Nombre']= i.nombre
        json_result['Ingredientes']= i.ingredientes
        json_result['Categoria']= i.categoria
        json_result_list.append(json_result)
    return json_result_list

#BUSCAR REGISTRO DE LA DB POR UNA PALABRA
def buscar(palabra):
    json_result_list=[]
    query = db.session.query(Recetas).filter(Recetas.nombre.ilike(f'%{palabra}%')).all()
    for i in query:
        json_result= {}
        json_result['Nombre']= i.nombre
        json_result['Ingredientes']= i.ingredientes
        json_result['Categoria']= i.categoria
        json_result_list.append(json_result)
    return json_result_list

#INSERTAR NUEVA RECETA
def insert(nombre, ingredientes, categoria):
    #crear nueva receta
    receta = Recetas(nombre=nombre, ingredientes=ingredientes, categoria=categoria)
    db.session.add(receta)
    db.session.commit()