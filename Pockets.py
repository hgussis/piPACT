def pockets(start_index, stop_index, time_stamp, RSSI):
    #find difference between two points in time
    s1 = time_stamp[start_index]
    s2 = time_stamp[stop_index]
    FMT="%Y-%m-%d %H:%M:%S"
    tdelta = datetime.strptime(s2,FMT) - datetime.strptime(s1,FMT)

    #print(time_stamp)
    #print(rssi)
    #print(tdelta)