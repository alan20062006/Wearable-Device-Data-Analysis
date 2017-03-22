import csv
import json
import pandas as pd


def Json2CSV(type,start_date = '2016-11-28',end_date = '2017-03-10'):
    datelist = pd.date_range(start = pd.to_datetime(start_date),
                             end = pd.to_datetime(end_date)).tolist()
    #f=open("DataSample.json", encoding='utf-8')        #Open DataSample
    for ts in datelist:
        date = ts.strftime('%Y-%m-%d')
        jsonfilename='./json_file/'+type+'/'+type+ date +'.json'
        csvfilename='./csv_file/'+type+'/'+type+ date +'.csv'
        #process the files
        with open(jsonfilename,'r') as f:
            DICT=json.load(f)
            DICT=json.loads(DICT)                           #DICT is dict
            Intraday=DICT.get('activities-'+type+'-intraday')  #Intraday is dict    #distance,elevation,floors,steps
            Dataset=Intraday.get('dataset')                 #Dataset is list

        n=len(Dataset)

        fieldnames=['time', 'value']
        with open(csvfilename, 'a') as file:#Totally rewrite:'w', continue input:'a'
            dict_writer=csv.DictWriter(file, fieldnames=fieldnames,lineterminator='\n')
            dict_writer.writeheader()#remember to comment the line when you continue the input
            dict_writer.writerows(Dataset)

'''Type=['steps','distance','floors','elevation','calories']
for type in Type:
    Json2CSV(type)'''
Json2CSV('calories')