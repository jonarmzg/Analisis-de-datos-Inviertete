import pandas as pandas
# Importar librerias necesarias
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 

# importar base de datos

bd = pd.read_csv("base_prueba.csv", na_values = np.nan)

# Limpiar base y nombrar funciones para seleccionar desercion 
bd.dropna(how = "all", axis = "columns", inplace =True)
bd.drop(["nombre"], axis = 1, inplace =True)
bd.dropna(inplace = True)
print(bd.dtypes)
