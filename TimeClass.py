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

    def get5stime(self):                #get the 5s latter time string
        self.sec += 5
        if self.sec > 59:
            self.sec = self.sec%60
            self.min += 1
            if self.min > 59:
                self.min = self.min%60
                self.hour += 1
        return self.gettimestr()


    def istrue(self):                   #whether the time is in the range of 24 hrs
        if self.hour > 23:
            return False
        elif self.hour==23 and self.min==59 and self.sec==55:
            return False
        else:
            return True