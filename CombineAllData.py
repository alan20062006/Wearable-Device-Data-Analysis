import pandas as pd
import numpy as np

start_date = '2016-11-28'
end_date = '2017-04-03'
Type=['steps','distance','floors','elevation','heartrate','sleep','calories']

datelist = pd.date_range(start = pd.to_datetime(start_date),end = pd.to_datetime(end_date)).tolist()
OuterFrame=[]
#InnerFrame=[]
for ts in datelist:
    date = ts.strftime('%Y-%m-%d')
    year=date[0]*10+date[1]
    month=date[3]*10+date[4]
    day=date[6]*10+date[7]

    for type in Type:
        csvfilename='./csv_file/'+type+'/'+type+ date +'.csv'
        if type=='steps':
            steps=pd.read_csv(csvfilename)
        elif type=='distance':
            dist=pd.read_csv(csvfilename)
        elif type=='floors':
            floors=pd.read_csv(csvfilename)
        elif type=='elevation':
            elev=pd.read_csv(csvfilename)
        elif type=='heartrate':
            heart=pd.read_csv(csvfilename)
        elif type=='sleep':
            sleep=pd.read_csv(csvfilename)
        elif type=='calories':
            cal=pd.read_csv(csvfilename)

    allme=pd.merge(heart,steps,how='outer',on='time')
    allme=pd.merge(allme,dist,how='outer',on='time')
    allme=pd.merge(allme,floors,how='outer',on='time')
    allme=pd.merge(allme,elev,how='outer',on='time')
    allme=pd.merge(allme,sleep,how='outer',on='time')
    allme=pd.merge(allme,cal,how='outer',on='time')

    '''innerme=pd.merge(heart,steps,how='inner',on='time')
    innerme=pd.merge(innerme,dist,how='inner',on='time')
    innerme=pd.merge(innerme,floors,how='inner',on='time')
    innerme=pd.merge(innerme,elev,how='inner',on='time')
    innerme=pd.merge(innerme,sleep,how='inner',on='time')
    innerme=pd.merge(innerme,cal,how='inner',on='time')'''

    OuterFrame.append(allme)
    #InnerFrame.append(innerme)

OuterData=pd.concat(OuterFrame)
#InnerData=pd.concat(InnerFrame)

#InnerData.to_csv('AllData.csv')
OuterData.to_csv('AllOuterData.csv')