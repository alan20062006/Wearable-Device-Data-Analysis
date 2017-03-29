from GetDataOnline import GetDataOnline
from URL_Dict import *

start_date = '2017-03-11'
end_date = '2017-03-28'

#type='sleep'
#GetDataOnline(type,start_date,end_date)

Type=['steps','distance','floors','elevation','calories','heartrate','sleep']
#Type=['floors','elevation','calories','heartrate']
for type in Type:
    GetDataOnline(type,start_date,end_date)
