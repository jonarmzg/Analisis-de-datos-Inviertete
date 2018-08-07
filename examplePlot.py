import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("Customer Churn Model.txt")

data.head()

data.shape

#savefig("path_donde_guardar_im.jpeg")

### Scater Plot
data.plot(kind = "scatter", x = "Day Mins", y = "Day Charge")
plt.grid(color='r', linestyle='-', linewidth=2)

data.plot(kind = "scatter", x = "Night Mins", y = "Night Charge")
plt.grid(color='g', linestyle='-', linewidth=2)

fig3, axs = plt.subplots(2,2, sharey=True, sharex=True)
data.plot(kind = "scatter", x = "Day Mins", y = "Day Charge", ax = axs[0][0], grid=True, linestyle='-', color='g')
data.plot(kind = "scatter", x = "Night Mins", y = "Night Charge", ax = axs[0][1], grid=True, linestyle='-', color='g')
data.plot(kind = "scatter", x = "Day Calls", y = "Day Charge", ax = axs[1][0], grid=True, linestyle='-', color='g')
data.plot(kind = "scatter", x = "Night Calls", y = "Night Charge", ax = axs[1][1], grid=True, linestyle='-', color='g')



### Histogramas de frecuencia 
plt.figure()
k = np.ceil(1 + np.log2(3333))#bins->num de divisiones: np.ceil->Redondea hacia el valor superior
plt.hist(data["Day Calls"], bins = int(k))
plt.xlabel("Número de llmadas al día")
plt.ylabel("Frecuencia")
plt.title("Histograma de número de llamadas al día")
#data["Day Calls"].plot(kind="hist", bins=int(k))
plt.grid(color='r', linestyle='-', linewidth=2)


### Boxplot: Diagrama de caja y bigotes 
plt.figure()
plt.boxplot(data["Day Calls"])
plt.ylabel("Numero de llamadas diarias")
plt.title("Boxplot de las llamadas diarias")
#data["Day Calls"].plot(kind="box", title ="Boxplot de las llamadas diarias" , x = "Numero de llamadas diarias")
plt.grid(color='black', linestyle='-', linewidth=2)

data["Day Calls"].describe()

IQR = data["Day Calls"].quantile(0.75) - data["Day Calls"].quantile(0.25) #Rango Inter Cuartil
data["Day Calls"].quantile(0.25) - 1.5*IQR
data["Day Calls"].quantile(0.75) + 1.5*IQR



plt.show()

