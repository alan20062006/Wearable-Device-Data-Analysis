import json
from time import sleep

import pandas as pd
import requests

def GetDataOnline(start_date= '2017-03-08',end_date= '2017-03-09'):

    # put the token for your app in between the single quotes
    token = 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI1M1E5RjgiLCJhdWQiOiIyMjhCVk4iLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJyc29jIHJzZXQgcmFjdCBybG9jIHJ3ZWkgcmhyIHJudXQgcnBybyByc2xlIiwiZXhwIjoxNDg5MjAxNjc2LCJpYXQiOjE0ODg1OTY4Nzd9.dFUm4JL7l54oGQy1ABzbSQwhKof_E-XumPv6NdrN4JU'

    # make a list of dates
    # ref: http://stackoverflow.com/questions/993358/creating-a-range-of-dates-in-python
    # You can change the start and end date as you want
    # Just make sure to use the yyyy-mm-dd format

    datelist = pd.date_range(start = pd.to_datetime(start_date),
                             end = pd.to_datetime(end_date)).tolist()

    '''
    The codes below use a for loop to generate one URL for each day in the datelist,
    and then request each day's data and save the data into individual json files.
    Because Fitbit limit 150 request per hour, I let the code sleep for 30 seconds
    between each request, to meet this limitation.
    '''
    for ts in datelist:
        date = ts.strftime('%Y-%m-%d')
        url = 'https://api.fitbit.com/1/user/-/activities/steps/date/' + date + '/1d/1min/time/00:00/23:59.json'
        filename = 'HR'+ date +'.json'
        response = requests.get(url=url, headers={'Authorization':'Bearer ' + token})

        if response.ok:
            with open(filename, 'w') as f:

                BYtes=response.content
                STring=BYtes.decode("utf-8")
                json.dump(STring,f)
            print (date + ' is saved!')
            sleep(30)
        else:
            print ('The file of %s is not saved due to error!' % date)
            sleep(30)
