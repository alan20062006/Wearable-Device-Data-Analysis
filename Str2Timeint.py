def Str2Timeint(Tstring):
    h=int(Tstring[0])*10+int(Tstring[1])
    m=int(Tstring[3])*10+int(Tstring[4])
    s=int(Tstring[6])*10+int(Tstring[7])
    return h*60*60+m*60+s
    return h*24*60+m*60+s
    return h*24*60+m*60+s