import pandas as pd
from TimeClass import TimeClass
import time as tm
def GetRoundTime(type,start_date = '2017-04-04',end_date = '2017-05-10'):
    datelist = pd.date_range(start=pd.to_datetime(start_date),
                             end=pd.to_datetime(end_date)).tolist()
    for ts in datelist:
        date = ts.strftime('%Y-%m-%d')
        year = int(date[0]) * 1000 + int(date[1])*100+int(date[2])*10+int(date[3])
        month = int(date[5]) * 10 + int(date[6])
        day = int(date[8]) * 10 + int(date[9])
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
            time.sec=sec                             #uncomment those lines if you want to round time

            min=time.getmin()
            hour=time.gethour()

            timeStr=str(year)+'-'+str(month)+'-'+str(day)+' '+str(hour)+':'+str(min)+':'+str(sec)
            timeArray=tm.strptime(timeStr,"%Y-%m-%d %H:%M:%S")
            file.time.values[i]=int(tm.mktime(timeArray))

        file.to_csv(csvfilename,index=False)

Type=['steps','distance','floors','elevation','heartrate','sleep','calories']
for type in Type:
    GetRoundTime(type)
#type='heartrate'
#GetRoundTime(type)