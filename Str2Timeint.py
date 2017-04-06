def Str2Timeint(Tstring):
    h=int(Tstring[0:1])
    m=int(Tstring[3:5])
    s=int(Tstring[7:9])
    return h*24*60+m*60+s