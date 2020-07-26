from pathlib import Path
from datetime import datetime
from datetime import timedelta
import Pockets
import No_Obstruction
import WallDoor
import Combo

#barrier list contains the time stamps and type of interaction the
#devices had (ex. ([0,3,"no obs]) means that from minutes 0-3,
#there was no obstruction
"""Valid obstruction types:
"""
def pact(barrier_list, file_scan, file_location="Data"):

    #results
    possible_results=("The devices WERE likely within 6 feet for more than fifteen minutes",
                      "The devices WERE NOT likely within 6 feet for more than fifteen minutes")
    mins_within_range=0

    #opens up a file and makes a list of time stamps and corresponding RSSI values
    root= Path(".")
    path_to_data = root / file_location / file_scan
    rssi= []
    time_stamp= []
    #obstruction_dict= {"none":}
    with open(path_to_data, mode = "r") as var:
        content_list= var.readlines()
    for entry in content_list[1:]:
        list_data = entry.split(",")
        time_stamp.append(list_data[2][0:-7])
        rssi.append(list_data[-1][0:-1])

    #looks at each entry to see the obstructions
    for entry in barrier_list:
        start=entry[0]
        stop= entry[1]
        index=0
        #assigns the start and stop times to the corresponding index in time_stamp
        for times in time_stamp:
            if start == times:
                start = index
            if stop == times:
                stop = index
                break
            index += 1

        #puts the start and stop times into each method
        entry[2] = obs
        if obs== "hi":
            mins_within_range += 0 #redirects to method
        elif obs == "hey":
            mins_within_range +=0 #redirects


    if mins_within_range >= 15:
        return possible_results[0]
    else:
        return possible_results[1]



    #find difference between two points in time
    s1 = time_stamp[0]
    s2 = time_stamp[1]
    FMT="%Y-%m-%d %H:%M:%S"
    tdelta = datetime.strptime(s2,FMT) - datetime.strptime(s1,FMT)

    #print(time_stamp)
    #print(rssi)
    #print(tdelta)



string = pact((), "2Y_human_wall_pi_pact_scan_20200723T010012.csv")
print(string)