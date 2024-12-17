'''
Crear scv para los moodelos de machine learning
------------------------------------------------
Aquí se se pasan los ingredientes a columnas y luego se escalan los datos
'''

#importar las librerias necesarias
import numpy as np
import pandas as pd
import os
#importar función MultiLabelBinarizer para hacer un one hot encoder a los valores de la columna 'Ingredientes'
from sklearn.preprocessing import MultiLabelBinarizer
#Escalar los datos con StandarScaler
from sklearn.preprocessing import StandardScaler

#------------------------ Convertir ingredientes en columnas -------------------#
#extraer los datos
archivo_csv = os.path.join(os.path.dirname(__file__), 'recetas_limpio.csv')
df = pd.read_csv(archivo_csv)

#convertir los valores de la columna Ingredientes a una lista para luego poder transformarlos 
df['Ingredientes']=df['Ingredientes'].str.split("-")
print(df.head())

mlb = MultiLabelBinarizer()
ingredientes_matrix = mlb.fit_transform(df["Ingredientes"])

#crear un dataFrame para mostrar los valores ya transformados en sus respectivas columnas 
ingredientes_df = pd.DataFrame(ingredientes_matrix, columns=mlb.classes_)
print('\n\nINGREDIENTES A COLUMNAS:\n\n', ingredientes_df.head())

#------------------------ csv para el modelo 'recomendar_recetas' -------------------#
#Escalar datos del nuevo dataframe
x_recomendar = ingredientes_df.copy()

scaler_recomendar = StandardScaler()
x_scaler_1 = scaler_recomendar.fit_transform(x_recomendar)

df_recomendar_recetas = pd.DataFrame(x_scaler_1, columns=x_recomendar.columns)
print('\n\nINGREDIENTES ESCALADO:\n\n',df_recomendar_recetas.head())

#agreagar las columnas faltantes
df_recomendar_recetas["Nombre"] = df["Nombre"]
df_recomendar_recetas["Categoria"] = df["Categoria"]

#mostrar las primeras 5 filas de dataframe ya transformado 
print('\n\nDF PARA MODELO RECOMENDAR_RECETAS:\n\n', df_recomendar_recetas.head())
#mostrar el tamaño del dataframe
print('\n\nTAMAÑO:\n\n', df_recomendar_recetas.shape)

#guardar dataframe ya transformado como un archivo csv
df_recomendar_recetas.to_csv('recomendar_recetas.csv', index=False)

#---------------------- csv para el modelo 'clasificar_recetas' ---------------------#
#En este caso, para poder hacer el modelo para clasificar las recetas se necesita primero balancear 
# los datos y recien ahí escalarlos, por lo que aquí se hara ese proceso y se guardará en un csv llamado "clasificar_recetas.csv"