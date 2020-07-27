import statistics as stats
from datetime import datetime
from datetime import timedelta

def human(start_index, stop_index, time_stamp, RSSI):
    stdev =stats.stdev(RSSI[start_index:stop_index])
    average = stats.mean(RSSI[start_index:stop_index])
    median= stats.median(RSSI[start_index:stop_index])

    #find difference between two points in time
    s1 = time_stamp[start_index]
    s2 = time_stamp[stop_index]
    FMT="%Y-%m-%d %H:%M:%S"
    tdelta = datetime.strptime(s2,FMT) - datetime.strptime(s1,FMT)

    total_seconds = float(tdelta.total_seconds())
    mins_elapsed = float(total_seconds // 60)

    if median >=-58 and average >= -58.41:
        return mins_elapsed
    else:
        return 0