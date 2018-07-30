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
    medals_df = pd.DataFrame(main_dict)
    print(medals_df.head())

    #Elegimos donde guardarlo (en la carpeta athletes es donde tiene mas sentido por el contexto del análisis)
    mainpath = "Documents/python-ml-course/datasets"
    #filename = "athletes/downloaded_medals."
    fullpath = os.path.join(mainpath, filename)

    #Lo guardamos en CSV, en JSON o en Excel según queramos
    medals_df.to_csv(fullpath+".csv")
    medals_df.to_json(fullpath+".json")
    medals_df.to_excel(fullpath+".xls")
    
    return