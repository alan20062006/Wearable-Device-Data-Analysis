from GetDataOnline import GetDataOnline
from URL_Dict import *

start_date = '2017-04-04'
end_date = '2017-05-03'

type='calories'
GetDataOnline(type,start_date,end_date)

#Type=['steps','distance','floors','elevation','calories','heartrate','sleep']
#Type=['sleep','elevation','calories']
#for type in Type:
#    GetDataOnline(type,start_date,end_date)
