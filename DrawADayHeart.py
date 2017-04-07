import matplotlib.pyplot as plt
import pandas as pd
import  numpy as np
from scipy.stats import mode
def DrawADayHeart(filename):
    dataFrame=pd.read_csv(filename)
    xarray=np.array(dataFrame.time)         #adjust the 'time'
    yarray=np.array(dataFrame.heartrate)    #adjust the para name

    fig=plt.figure()                    #open a window
    ax=fig.add_subplot(3,1,1)
    ax.plot(xarray,yarray,'k-')              #draw

    ticks = ax.set_xticks([0, 7200, 14400, 21600, 28800, 36000, 43200, 3600*14, 3600*16, 3600*18, 3600*20, 3600*22, 3600*24])
    labels = ax.set_xticklabels(['0h', '2h', '4h', '6h', '8h', '10h', '12h','14h','16h','18h','20h','22h','24h'], fontsize = 'small')
    ax.set_title(filename)
    ax.set_ylabel('value')
    ax.set_xlabel('time')

    axHist=fig.add_subplot(3,1,2)               #histogram
    axHist=dataFrame.heartrate.hist(bins=50)    #need to be changed(heartrate)

    axKDE=fig.add_subplot(3,1,3)                #KDE
    axKDE=dataFrame.heartrate.plot(kind='kde')

    '''sport=dataFrame[dataFrame.heartrate>99]     #sport and extreme sport
    extremeSport=dataFrame[dataFrame.heartrate>138]
    axSport=fig.add_subplot(5,1,4)
    axSport.plot(np.array(sport.time),np.array(sport.heartrate),'.')
    axExtreme=fig.add_subplot(5,1,5)
    axExtreme.plot(np.array(extremeSport.time), np.array(extremeSport.heartrate), '.')'''

    


    Mode=mode(np.array(dataFrame.heartrate),axis=None)
    print("Mode:%d"%(Mode[0]))

    plt.show()

filename='heartrate2017-04-01.csv'
DrawADayHeart(filename)