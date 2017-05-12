import pandas as pd
from TimeClass import TimeClass
import time as tm
def SleepRoundAtMin(type,start_date = '2016-11-28',end_date = '2017-05-10'):
    datelist = pd.date_range(start=pd.to_datetime(start_date),
                             end=pd.to_datetime(end_date)).tolist()
    for ts in datelist:
        date = ts.strftime('%Y-%m-%d')
        year = int(date[0]) * 1000 + int(date[1]) * 100 + int(date[2]) * 10 + int(date[3])
        month = int(date[5]) * 10 + int(date[6])
        day = int(date[8]) * 10 + int(date[9])
        csvfilename = './csv_file/' + type + '/' + type + date + '.csv'
        file = pd.read_csv(csvfilename)  # file is dataframe

        file.columns = ['time', type]

        index = file.index
        for i in index:
            time = TimeClass(file.time.values[i])  # now time is a TimeClass

            time.sec = 0  # uncomment those lines if you want to round time

            min = time.getmin()
            hour = time.gethour()

            timeStr = str(year) + '-' + str(month).zfill(2) + '-' + str(day).zfill(2) + ' ' + str(hour).zfill(2) + ':' + str(min).zfill(2) + ':' + '00'
            timeArray = tm.strptime(timeStr, "%Y-%m-%d %H:%M:%S")

            file.time.values[i] = int(tm.mktime(timeArray))


        file.to_csv(csvfilename, index=False)



type='sleep'
SleepRoundAtMin(type)