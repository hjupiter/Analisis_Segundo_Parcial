import pandas as pd
import numpy as np
import json
import matplotlib.pyplot as plt
import numpy
import collections
import csv


data = pd.read_json("salida4.json")
data = data.dropna()
data = data.reset_index(drop=True)
y = []
for listaAutor in data["listaAutores"]:
	val = len(listaAutor)
	y.append(val)
y = np.sort(y)
counter=collections.Counter(y)
row = ["Numero de autores x paper","Frecuencia"]
with open('filename.csv', 'w') as myfile:
	wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
	wr.writerow(row)
	for x,y in zip(counter.keys(),counter.values()):
		row[0] = x
		row[1] = y
		wr.writerow(row)
#print counter
bins =  numpy.linspace(0,60,200)
plt.hist(y,bins, alpha = 0.5)
plt.xlabel("Numero de Autores")
plt.ylabel("Frecuencia")
plt.show()