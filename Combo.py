import statistics as stats
from datetime import datetime
from datetime import timedelta

def combo(start_index, stop_index, time_stamp, RSSI, combo_type):
    stdev =stats.stdev(RSSI[start_index:stop_index])
    average = stats.mean(RSSI[start_index:stop_index])
    median = stats.median(RSSI[start_index:stop_index])

    #find difference between two points in time
    s1 = time_stamp[stop_index]
    s2 = time_stamp[stop_index]
    FMT="%Y-%m-%d %H:%M:%S"
    tdelta = datetime.strptime(s2,FMT) - datetime.strptime(s1,FMT)
    total_seconds = float(tdelta.total_seconds())
    mins_elapsed = float(total_seconds // 60)


    if combo_type == "doorxpocket":
        if median >= -58 and average >= -59.4:
            return mins_elapsed
        else:
            return 0
    elif combo_type == "pocketxhumanxwall":
        if median >= -69 and average >= -69.5:
            return mins_elapsed
        else:
            return 0
    elif combo_type == "2humans":
        if median >= -65 and average >= -64.6:
            return mins_elapsed
        else:
            return 0
    elif combo_type== "humanxwall":
        if median >= -55 and average >= -57.1:
            return mins_elapsed
        else:
            return 0
    elif combo_type == "sockxwall":
        if median >= -70 and average >= -70.2:
            return mins_elapsed
        else:
            return 0
    elif combo_type == "sockxhuman":
        if median >= -57 and average >= -59.6:
            return mins_elapsed
        else:
            return 0

