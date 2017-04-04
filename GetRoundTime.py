import pandas as pd
from TimeClass import TimeClass
def GetRoundTime(type,start_date = '2016-11-28',end_date = '2017-04-03'):
    datelist = pd.date_range(start=pd.to_datetime(start_date),
                             end=pd.to_datetime(end_date)).tolist()
    for ts in datelist:
        date = ts.strftime('%Y-%m-%d')
        csvfilename = './csv_file/' + type + '/' + type + date + '.csv'
        file=pd.read_csv(csvfilename)                       #file is dataframe

        if type=='calories':
            file.columns=('calorieslevel','caloriesmets','time',type)
        else:
            file.columns=['time',type]

        index=file.index
        for i in index:
            time=TimeClass(file.time.values[i])        #now time is a TimeClass
            sec=time.getsec()
            if sec % 5:
                sec=(sec//5+1)*5
            time.sec=sec
            file.time.values[i]=time.gettimestr()

        file.to_csv(csvfilename,index=False)

Type=['steps','distance','floors','elevation','heartrate','sleep','calories']
for type in Type:
    GetRoundTime(type)
#type='heartrate'
#GetRoundTime(type)