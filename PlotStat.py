import pandas as pd
import matplotlib.pyplot as plt

timeline=pd.read_csv('TimeLine.csv')
heart=pd.read_csv('HeartSample.csv')

me=pd.merge(timeline,heart,how='left')

TIndex=timeline.tolist()
me.reindex(TIndex)

del me['time']