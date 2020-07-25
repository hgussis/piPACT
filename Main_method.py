from pathlib import Path
from datetime import datetime
from datetime import timedelta
#
#
def pact(barrier_list, file_scan):
    root= Path(".")
    path_to_data = root / "Data" / file_scan
    rssi= []
    time_stamp= []
    with open(path_to_data, mode = "r") as var:
        content_list= var.readlines()
    for entry in content_list[1:]:
        list_data = entry.split(",")
        time_stamp.append(list_data[2][0:-7])
        rssi.append(list_data[-1][0:-1])

    #find difference between two points in time
    s1 = time_stamp[0]
    s2 = time_stamp[1]
    FMT="%Y-%m-%d %H:%M:%S"
    tdelta = datetime.strptime(s2,FMT) - datetime.strptime(s1,FMT)
    print(tdelta)



pact(0, "2Y_human_wall_pi_pact_scan_20200723T010012.csv")