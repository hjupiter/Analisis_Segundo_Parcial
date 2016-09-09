import pandas as pd
import json
import csv
import pandas as pd
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer


#pd.read_csv("r4.csv", encoding="utf-8") 

df = pd.read_csv("nuevoCSV.csv") 

stop = stopwords.words('english')
df_abstract = df['abstract'].apply(lambda x: [item for item in x if item not in stop])

print df_abstract