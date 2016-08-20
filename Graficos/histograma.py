import pandas as pd
import numpy as np
import json
import matplotlib.pyplot as plt
import numpy


data = pd.read_json("salida4.json")
#data = data.dropna(subset=["listaAutores"])
data = data.dropna()
data = data.reset_index(drop=True)

#row = ["Titulo","Autores"]
#row = ["Autores"]
y = []
for listaAutor in data["listaAutores"]:
	val = len(listaAutor)
	y.append(val)

bins =  numpy.linspace(0,60,100)
plt.hist(y,bins, alpha = 0.5)
plt.xlabel("Numero de Autores")
plt.ylabel("Frecuencia")
plt.show()