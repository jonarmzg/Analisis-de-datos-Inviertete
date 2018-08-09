# Importar librerias necesarias
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 
import os    

#---------------------------------------------------------------------------------------------------


#---------------------------------------------------------------------------------------------------

#funcion para descargar archivo csv desde url
def downloadFromURL(url, filename, sep = ",", delim = "\n"):
    #primero importamos la libreria y hacemos la conexion con la web de los datos
    import urllib3 
    http = urllib3.PoolManager()
    r = http.request('GET', url)
    print("El estado de la respuesta es %d" %(r.status))
    response = r.data

    #El objeto response contiene un string binario, asi que lo convertimos a un string decodificandolo en UTF-8
    str_data = response.decode('utf-8')

    #Dividimos el string en un array de filas, separandolo por intros
    lines = str_data.split(delim)

    #la primera linea contiene la cabecera, asi que la extraemos
    col_names = lines[0].split(sep)
    n_cols = len(col_names)

    #Generamos un diccionario vacio donde irá la informacion procesada desde la URL externa
    counter = 0
    main_dict = {}
    for col in col_names:
        main_dict[col] = []

    #Procesamos fila a fila la informacion para ir rellenando el diccionario con los datos como hicimos antes
    for line in lines:
        #Nos saltamos la primera línea que es la que contiene la cabecera y ya tenemos procesada 
        if(counter > 0):
            #Dividimos cada string por las comas como elemento separador
            values = line.strip().split(sep)
            #añadimos cada valor a su respectiva columna del diccionario
            for i in range(len(col_names)):
                main_dict[col_names[i]].append(values[i])
        counter += 1

    print("El data set tiene %d filas y %d columnas" %(counter, n_cols))

    #convertimos el diccionario procesado a Data Frame y comprobamos que los datos son correctos
    name_df = pd.DataFrame(main_dict)
    print(name_df.head())

    #Elegimos la ruta donde guardarlo
    mainpath = "C:/Users/Example"
    fullpath = os.path.join(mainpath, filename)

    #Lo guardamos en CSV, en JSON o en Excel según queramos
    name_df.to_csv(fullpath+".csv") 
    name_df.to_json(fullpath+".json")
    name_df.to_excel(fullpath+".xls")
    
    return

#---------------------------------------------------------------------------------------------------
#direccion url donde se encuentra el archivo csv
URL = "https://raw.githubusercontent.com/jonarmzg/Analisis-de-datos-Inviertete/master/base_prueba.csv"
#Carpeta/Nompre_de_archivo
filename="inviertete/downloaded_inviertete"
downloadFromURL(URL,filename)

#---------------------------------------------------------------------------------------------------

#Definir ruta del archivo 
mainpath="C:/Users/Example"
filename="inviertete/downloaded_inviertete.csv"
fullpath=mainpath + "/" + filename

#---------------------------------------------------------------------------------------------------

# importar base de datos
baseDatos = pd.read_csv(fullpath, na_values = np.nan)

#---------------------------------------------------------------------------------------------------

# Limpiar base y nombrar funciones para seleccionar desercion 
baseDatos.dropna(how = "all", axis = "columns", inplace =True)
baseDatos.drop(["nombre"], axis = 1, inplace =True)
baseDatos.dropna(inplace = True)
print(baseDatos.dtypes)


baseDatos.plot(kind = "scatter", x = "edad", y = "raven_score")

#----------------------------------------------------------------------------------------------------
plt.figure()
plt.boxplot(baseDatos["edad"])
plt.ylabel("Edad")
plt.title("Boxplot de la edad de las personas inscritas al curso")
plt.grid()
#
IQR = baseDatos["edad"].quantile(0.75) - baseDatos["edad"].quantile(0.25) #Rango Inter Cuartil
print("El IQR es: ", IQR)
print("Los valores atipicos estan debajo de: ", baseDatos["edad"].quantile(0.25) - 1.5*IQR," y sobre", baseDatos["edad"].quantile(0.75) + 1.5*IQR)
print(baseDatos["edad"].describe())


### Histogramas de frecuencia 
plt.figure()
rs=1 + np.log2(40)# Regla de sturges
k = np.ceil(rs)#bins->num de divisiones: np.ceil->Redondea hacia el valor superior
plt.hist(baseDatos["edad"], bins = int(k))
plt.xlabel("Edad de las personas")
plt.ylabel("Frecuencia")
plt.title("Histograma de edades")
#data["Day Calls"].plot(kind="hist", bins=int(k))
plt.grid(color='r', linestyle='-', linewidth=.3)




plt.show()