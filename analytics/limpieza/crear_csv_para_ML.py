#importar las librerias necesarias
import numpy as np
import pandas as pd
import os
#importar función MultiLabelBinarizer para hacer un one hot encoder a los valores de la columna 'Ingredientes'
from sklearn.preprocessing import MultiLabelBinarizer

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
#agreagar las columnas faltantes
ingredientes_df["Nombre"] = df["Nombre"]
ingredientes_df["Categoria"] = df["Categoria"]

#mostrar las primeras 5 filas de dataframe ya transformado 
print('\nDataframe ya transformado:\n', ingredientes_df.head())
#mostrar el tamaño del dataframe
print('Tamaño:\n', ingredientes_df.shape)

#guardar dataframe ya transformado como un archivo csv
ingredientes_df.to_csv('recetas_ML.csv', index=False)