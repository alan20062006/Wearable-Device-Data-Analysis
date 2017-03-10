import csv
import json

f=open("DataSample.json", encoding='utf-8')
DICT=json.load(f)
DICT=json.loads(DICT)                           #DICT is dict
Intraday=DICT.get('activities-heart-intraday')  #Intraday is dict
Dataset=Intraday.get('dataset')                 #Dataset is list

n=len(Dataset)

fieldnames=['time', 'value']
with open('mycsvfile.csv', 'a') as file:#Totally rewrite:'w', continue input:'a'
    dict_writer=csv.DictWriter(file, fieldnames=fieldnames,lineterminator='\n')
    dict_writer.writeheader()#remember to comment the line when you continue the input
    dict_writer.writerows(Dataset)