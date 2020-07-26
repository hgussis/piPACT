import statistics as stats
from datetime import datetime
from datetime import timedelta

def combo(start_index, stop_index, time_stamp, RSSI, combo_type):
    key_stdev = 0
    key_avg=0
    stdev =stats.stdev(RSSI[start_index:stop_index])
    average = stats.mean(RSSI[start_index:stop_index])

    #find difference between two points in time
    s1 = time_stamp[stop_index]
    s2 = time_stamp[stop_index]
    FMT="%Y-%m-%d %H:%M:%S"
    tdelta = datetime.strptime(s2,FMT) - datetime.strptime(s1,FMT)
    total_seconds = tdelta.total_seconds
    mins_elapsed = total_seconds/60


    if combo_type
        "doorxpocket",
        #"sockxhumanxwall":,
        #"2humans":
        #"humanxwall":,
        #"sockxwall":,
        #"sockxhuman":,
    }



    if stdev == 0 and average < 5:
        return mins_elapsed
    else:
        return 0

    #print(time_stamp)
    #print(rssi)
    #print(tdelta)