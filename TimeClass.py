class TimeClass(object):
    def __init__(self,timestr):
        self.hour = int(timestr[0])*10+int(timestr[1])
        self.min = int(timestr[3])*10+int(timestr[4])
        self.sec = int(timestr[-2])*10+int(timestr[-1])
    def gethour(self):
        return self.hour
    def getmin(self):
        return self.min
    def getsec(self):
        return self.sec
    def gettimestr(self):
        return str(self.hour).zfill(2)+':'+str(self.min).zfill(2)+':'+str(self.sec).zfill(2)