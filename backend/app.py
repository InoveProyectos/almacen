'''
Descripción:
En este programa van a ir todo los endpoints
'''

import traceback
import os

from flask import Flask, request, jsonify, render_template, Response, redirect , url_for

import recetas

# Server de flask
app = Flask(__name__)

# Se indica al sistema (app) de donde leer la base de datos
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///recetas.db"

# Se asocia el controlador de la base de datos con la aplicacion
from models import db
db.init_app(app)

#Endpoints
@app.route("/")
def home():
    try:
        home= 'Inicio'
        return home
    except:
        return jsonify({'trace': traceback.format_exc()})


#Lanzar el server
if __name__ == '__main__':
    print('Iniciando')
    
    #lanzar server
    app.run(host="127.0.0.1", port=5000)