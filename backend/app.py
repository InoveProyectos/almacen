'''
APIS Almacen
--------------------
Descripción:
En este programa van a ir todo los endpoints
'''

#---------------------------------- Importar librerías ----------------------------------#
import traceback
import os
import sys

from flask import Flask, request, jsonify, render_template, Response, redirect , url_for
import joblib
import pandas as pd

from models import db, Recetas

import recetas

#---------------------------- Configuración de la app y la DB ----------------------------#
# Server de flask
app = Flask(__name__)

# Se indica al sistema (app) de donde leer la base de datos
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///recetas.db"

# Se asocia el controlador de la base de datos con la aplicacion
db.init_app(app)

#--------------------------- Cargar modelos de machine learning ---------------------------#
# cargar el mlb que se usó para pasar los ingredientes a columnas
mlb = joblib.load("../analytics/limpieza/mlb_ml.pkl")

# extraer el escalador del modelo 'recomendar_recetas' y cargar el modelo entrenado
scaler_recomendar = joblib.load("../analytics/modelos/scaler_recomendar.pkl")
model_recomendar = joblib.load("../analytics/modelos/recomendar_receta.pkl")


#--------------------------------------- Endpoints ---------------------------------------#
#RUTA DE INICO
@app.route("/")
def home():
    try:
        # En el futuro se podria realizar una página de bienvenida
        return redirect(url_for('api'))
    except:
        return jsonify({'trace': traceback.format_exc()})


#RUTA PARA VER TODOS LOS ENDPOINTS DISPONIBLES
@app.route("/api")
def api():
    try:
        result = "<h1>Endpoints disponibles:</h1>"
        result += "<h2>[GET] /almacen --> mostrar todas las recetas en formato JSON</h2>"
        result += "<h2>[POST] /recomendar --> ingresar ingredientes y recomendar una receta en formato JSON</h2>"
        return result
    except:
        return jsonify({'trace': traceback.format_exc()})
    
    
#RUTA PARA VER TODAS LAS RECETAS DISPONIBLES
@app.route("/almacen")
def almacen():
    try:
        query = recetas.obtener_todo()
        return jsonify(query)
    except:
        return jsonify({'trace': traceback.format_exc()})
        

#RUTA PARA RECOMENDAR UNA RECETA A PARTIR DE LOS INGREDIENTES INGRESADOS
@app.route("/recomendar", methods= ['GET', 'POST'])
def recomendar():
    if request.method == 'GET':
        try:
            return render_template('recomendar.html')
        except:
            return jsonify({'trace': traceback.format_exc()})
        
    if request.method == 'POST':
        try:
            ingredientes_user = request.form.get('ingredientes').split(',')
            ingredientes_mlb = pd.DataFrame(mlb.transform([ingredientes_user]), columns=mlb.classes_)
            ingredientes_scaler = scaler_recomendar.transform(ingredientes_mlb)
            distancias, indices = model_recomendar.kneighbors(ingredientes_scaler)
            indice = int((indices[0][0])+1)
            data = recetas.filtrar_id(indice)
            return jsonify(data)
        except:
            return jsonify({'trace': traceback.format_exc()})
    

#----------------------------------- Lanzar el server -----------------------------------#
if __name__ == '__main__':
    print('Iniciando')
    
    #lanzar server
    app.run(host="127.0.0.1", port=5000)