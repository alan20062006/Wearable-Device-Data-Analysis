import csv
import json
import pandas as pd


def Json2CSV(type,start_date = '2017-03-29',end_date = '2017-03-29'):
    datelist = pd.date_range(start = pd.to_datetime(start_date),
                             end = pd.to_datetime(end_date)).tolist()
    #f=open("HeartSample.json", encoding='utf-8')        #Open DataSample
    for ts in datelist:
        date = ts.strftime('%Y-%m-%d')
        jsonfilename='./json_file/'+type+'/'+type+ date +'.json'
        csvfilename='./csv_file/'+type+'/'+type+ date +'.csv'
        #process the files
        sleeplistlabel=1
        with open(jsonfilename,'r') as f:
            DICT=json.load(f)
            DICT=json.loads(DICT)                           #DICT is dict
            if type=='heartrate':
                Intraday=DICT.get('activities-heart-intraday')
                Dataset=Intraday.get('dataset')
            elif type=='sleep':
                Intraday=DICT.get('sleep')
                if Intraday:
                    Dataset=Intraday[0].get('minuteData')
                else:
                    sleeplistlabel=0        #the list is empty, no sleep data in this day
            else:
                Intraday=DICT.get('activities-'+type+'-intraday')  #Intraday is dict    #distance,elevation,floors,steps
                Dataset=Intraday.get('dataset')                 #Dataset is list

        if not (type == 'sleep' and sleeplistlabel == 0):
            n=len(Dataset)
            fieldnames=['time', 'value']

        if type=='sleep':
            fieldnames=['dateTime','value']

        if type=='calories':
            fieldnames=['level','mets','time','value']

        with open(csvfilename, 'w') as file:#Totally rewrite:'w', continue input:'a'
            dict_writer=csv.DictWriter(file, fieldnames=fieldnames,lineterminator='\n')
            dict_writer.writeheader()#remember to comment the line when you continue the input
            if not (type == 'sleep' and sleeplistlabel == 0):
                dict_writer.writerows(Dataset)

#Type=['steps','distance','floors','elevation','heartrate','sleep']
#for type in Type:
#    Json2CSV(type)
Json2CSV('heartrate')