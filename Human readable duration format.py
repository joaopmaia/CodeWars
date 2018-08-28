def format_duration(seconds):
    iyear = (3600*24*365)
    iday = (3600*24)
    time = []
    if seconds == 0:
        return "now"
    if seconds/iyear == 1:
        time.append("1 year")
    elif seconds/iyear > 1:
        time.append("{} years".format(seconds/iyear))
    if (seconds%iyear)/iday == 1:
        time.append("1 day")
    elif (seconds%iyear)/iday > 1:
        time.append("{} days".format((seconds%iyear)/iday))
    if ((seconds%iyear)%iday)/3600 == 1:
        time.append("1 hour")
    elif ((seconds%iyear)%iday)/3600 > 1:
        time.append("{} hours".format(((seconds%iyear)%iday)/3600))
    if (((seconds%iyear)%iday)%3600)/60 == 1:
        time.append("1 minute")
    elif (((seconds%iyear)%iday)%3600)/60:
        time.append("{} minutes".format((((seconds%iyear)%iday)%3600)/60))
    if (((seconds%iyear)%iday)%3600)%60 == 1:
        time.append("1 second")
    elif (((seconds%iyear)%iday)%3600)%60 > 1:
        time.append("{} seconds".format((((seconds%iyear)%iday)%3600)%60))
    str = ""
    if len(time) == 1:
        return time[0]
    else:
        for i in range(len(time)):
            if i == len(time) - 2:
                str += time[i] + " and " + time[i+1]
                return str
            else:
                str += time[i] + ", "
        