from TimeClass import TimeClass
import pandas as pd
import time
timeline=pd.read_csv('TimeLine.csv')
timepoint=TimeClass('00:00:00')
Date='1975-01-01'
DateType='%Y-%m-%d %H:%M:%S'

zerotime=time.mktime(time.strptime(Date+' '+timepoint.gettimestr(), DateType))
tl={'time':[zerotime]}
while(timepoint.istrue()):
    tl['time'].append(time.mktime(time.strptime(Date+' '+timepoint.get5stime(), DateType)))
timeline=pd.DataFrame(tl)
#timeline.columns=['time']
timeline.to_csv('TimeLine.csv',index=False)