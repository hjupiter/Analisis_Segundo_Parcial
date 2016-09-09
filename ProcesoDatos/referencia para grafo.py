import pandas as pd 
import csv
import sys

def buscar(autor,nombre):
	b = 0
	for f in autor:
		if f==nombre:
			b = 1
			return  1
		else:
			b = 0
	return b

f = open("autores.csv", 'rt')
try:
	rw = []
	rq = []
	reader = csv.reader(f)
	count = 0
	for row in reader:
		for data in row:
			if buscar(rw,data)==0:
				rw.append(data)
				rq.append(count)
				count = count + 1
	f.close()
	f = open("autores.csv", 'rt')
	reader = csv.reader(f)
	file = open("newfiles.txt", "w")
	for row in reader:
		#print row
		val1 = 0
		val2 = 0
		c = 0
		for t in rw:
			if rw[c] == row[0]:
				val1 = rq[c]
			c = c + 1
		p = 0
		for t in range(0,len(rw)):
			if rw[p] == row[1]:
				val2 = rq[p]
			p = p + 1
		#print str(val1) + "\t" + str(val2)
		if val1>0 or val1>1 or val2>0 or val2>1:
			file.write(str(val1) + "\t" + str(val2)+"\n")
	file.close()

	file2 = open("autoresNum.txt", "w")
	count = 0
	for i in rw :
		if count >=2:
			file2.write(str(count) + "\t" + i+"\n")
		count = count + 1
finally:
	f.close()