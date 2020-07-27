from pathlib import Path
from datetime import datetime
from datetime import timedelta
import Pockets
import No_Obstruction
import WallDoor
import Combo
import statistics
import Humans
""""#barrier list contains the time stamps and type of interaction the
devices had (ex. ([1,3,"no obs],[3,9,"wall"]) means that from minutes 1-3 during the current hour
there was no obstructions and from minutes 3 to 9 there was a wall between the devices

Valid obstruction types: "no obs","wall","door","pockets","doorxpocket",
"pocketxhumanxwall","2humans","humanxwall","sockxwall","sockxhuman","human"

There must be atleast two tuples in the barrier_list or an error will be raised
"""
def pact(barrier_list, file_scan, file_location="Tests"):

    #opens up a file and makes a list of time stamps and corresponding RSSI values
    root= Path(".")
    path_to_data = root / file_location / file_scan
    RSSI= []
    time_stamp= []
    with open(path_to_data, mode = "r") as var: #opens file up
        content_list= var.readlines()
    for entry in content_list[1:]:
        list_data = entry.split(",")
        time_stamp.append(list_data[2][0:-7]) #puts every time stamp into a list
        RSSI.append(int(list_data[-1][0:-1])) #puts every RSSI value into a list

    mins_within_range=0 #represents how long the devices were within 6 feet

    #looks at each tuple in the barrier list to see the obstructions
    for entry in barrier_list:
        start=int(entry[0])
        stop= int(entry[1])
        index=0

        #assigns the start and stop times from the barrier list to the corresponding index in time_stamp
        for times in time_stamp:

            if start == int(times[-5:-3]):
                start = index
            if stop == int(times[-5:-3]):
                stop = index
                break
            index += 1

        obstruction_types = {  # creates a dictionary that holds all the possible barrier functions
            "no obs": No_Obstruction.no_obs(start, stop, time_stamp, RSSI), #puts the start and stop times into each method
            "wall": WallDoor.wall_door(start,stop,time_stamp,RSSI, "wall"),
            "door": WallDoor.wall_door(start,stop,time_stamp,RSSI, "door"),
            "pockets": Pockets.pockets(start, stop, time_stamp, RSSI),
            "doorxpocket": Combo.combo(start, stop, time_stamp, RSSI, "doorxpocket"),
            "pocketxhumanxwall": Combo.combo(start, stop, time_stamp, RSSI, "pocketxhumanxwall"),
            "2humans":  Combo.combo(start, stop, time_stamp, RSSI, "2humans"),
            "humanxwall": Combo.combo(start, stop, time_stamp, RSSI,"humanxwall" ),
            "sockxwall": Combo.combo(start, stop, time_stamp, RSSI, "sockxwall"),
            "sockxhuman": Combo.combo(start, stop, time_stamp, RSSI,"sockxhuman" ),
            "human": Humans.human(start, stop, time_stamp, RSSI),
        }


        obs = entry[2].lower() #ensure that capital letters arent used
        if obs in obstruction_types: #makes sure the obstruction is a part of the dictionary
            mins_within_range = mins_within_range + obstruction_types[obs] #puts the inputs into a barrier method to see if they were <6 ft
        else:
            raise NameError(
                "{x} does not have a specific function. Please review your inputs in the barrier_list".format(x=obs))
                # ensures that a user knows if there is an invalid input


    possible_results = ("The devices WERE likely within 6 feet for more than fifteen minutes. It is estimated that they were in contact for {} minutes".format(mins_within_range),
                        "The devices WERE NOT likely within 6 feet for more than fifteen minutes. It is estimated that they were in contact for {} minutes".format(mins_within_range),)


    if mins_within_range >= 15:
        return possible_results[0]
    else:
        return possible_results[1]




string = pact(((12,15,"door"), (0,5,"door")), "pos_door.csv")
print(string)