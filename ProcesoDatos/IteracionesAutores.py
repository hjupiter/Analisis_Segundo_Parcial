import pandas as pd
import json
import csv

data = pd.read_json("salida4.json")
#data = data.dropna(subset=["titulo"])
#data = data.dropna(subset=["listaAutores"])
#data = data.dropna(subset=["listaAfiliacion"])
data = data.dropna()
data = data.reset_index(drop=True)
count = 1;
row = ["Source","Target"]
with open('autores.csv', 'w') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(row)
    for listaAutor in data["listaAutores"]:
		count = 0
		if len(listaAutor)<200:
			for j in listaAutor:
				if len(j)>1:
					p = 0
					for k in listaAutor:
						if len(k)>1 and p>count and j!=k:
							row[0] = j.encode('ascii','ignore')
							row[1] = k.encode('ascii','ignore')
							#row = [v.decode('utf8') if isinstance(v, str) else v for v in row]
							wr.writerow(row)
						p = p + 1
					count = count + 1