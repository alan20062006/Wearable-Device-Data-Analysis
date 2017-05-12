import pandas as pd
from TimeClass import TimeClass
import time as tm
def HeartRoundAtMin(type,start_date = '2017-04-09',end_date = '2017-05-10'):
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

        droplist=[]
        length=len(file)
        index = file.index
        for i in index:
            time = TimeClass(file.time.values[i])  # now time is a TimeClass
            sec = time.getsec()

            secflag=-1          #if secflag=0, sec is rounded to last min. if 1, to next min
            if sec <= 30:
                sec = 0
                secflag = 0
            else:
                sec = 0
                if time.min==59:
                    time.min=0
                    time.hour += 1
                else:
                    time.min += 1
                secflag = 1
            time.sec = 0  # uncomment those lines if you want to round time

            min = time.getmin()
            hour = time.gethour()

            timeStr = str(year) + '-' + str(month).zfill(2) + '-' + str(day).zfill(2) + ' ' + str(hour).zfill(2) + ':' + str(min).zfill(2) + ':' + str(sec).zfill(2)
            timeArray = tm.strptime(timeStr, "%Y-%m-%d %H:%M:%S")

            if file.time.values[i-1]==int(tm.mktime(timeArray)) and secflag == 0 and i>0:
                droplist.append(i)
                file.time.values[i] = int(tm.mktime(timeArray))
            elif file.time.values[i-1] == int(tm.mktime(timeArray)) and secflag ==1 and i>0:
                droplist.append(i-1)
                file.time.values[i] = int(tm.mktime(timeArray))
            else:
                file.time.values[i] = int(tm.mktime(timeArray))


        file=file.drop(droplist)
        file.reindex(range(length-len(droplist)))
        file.to_csv(csvfilename, index=False)



type='heartrate'
HeartRoundAtMin(type)