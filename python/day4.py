"""
https://adventofcode.com/2018/day/4
"""

import sys
import numpy as np

FILE = '../data/day4.txt'

def calc_asleep(str1, str2):
    """
        arg:
        return: total minutes asleep
    """
    sleep = int(str1.split(" ")[1].strip("]").split(":")[1])
    wake = int(str2.split(" ")[1].strip("]").split(":")[1])
    return wake - sleep

def get_minutes(str1, str2):
    """
        arg:
        return: list of minutes asleep
    """
    sleep = int(str1.split(" ")[1].strip("]").split(":")[1])
    wake = int(str2.split(" ")[1].strip("]").split(":")[1])
    return list(range(sleep, wake))

def part_1():
    # count = 0
    records = []
    with open(FILE) as file:
        for line in file:
            records.append(line.strip("\n"))

    # records = np.array(records).sort()
    records = sorted(records)
    i = 0
    records_dict = {}
    while i < len(records):
        if len(records[i].split(" ")) == 6:
            j = i + 1
            guard = records[i].split(" ")[3].strip("#")
            if guard not in records_dict:
                records_dict[guard] = {"minutes":[]
                                      ,"time":[]}
            while j < len(records)-1 and len(records[j].split(" ")) != 6:
                records_dict[guard]["minutes"].append(calc_asleep(records[j], records[j+1]))
                for m in get_minutes(records[j], records[j+1]):
                    records_dict[guard]["time"].append(m)
                j += 2
            i += 1
        else: 
            i += 1

    guard_most = 0
    total_minutes_most = 0
    minute_most = 0
    for guard in records_dict:
        # print(guard)
        records_dict[guard].update({"total_minutes":np.array(records_dict[guard]["minutes"]).sum()})
        try:
            (values,counts) = np.unique(np.array(records_dict[guard]["time"]),return_counts=True)
            ind=np.argmax(counts)
            records_dict[guard].update({"most_minute":values[ind]})
        except:
            # print("error!!!!")
            records_dict[guard].update({"most_minute":0})

        if records_dict[guard]['total_minutes'] > total_minutes_most:
            guard_most = guard
            total_minutes_most = records_dict[guard]['total_minutes']
            minute_most = records_dict[guard]['most_minute']

        # print(records_dict[guard])
        # print("----------------------------")


    # for guard in records_dict:
    #     print(guard)
    #     print(records_dict[guard]['total_minutes'])
    #     print(records_dict[guard]['most_minute'])
    #     print("----------------------------")

    print("Guard: ", guard_most, " Minute: ", total_minutes_most
         , " Results: ", int(guard_most) * int(minute_most))
    """Answer: Guard: 3491 * 42 most minute = 146622
    """

def part_2():
    # count = 0
    records = []
    with open(FILE) as file:
        for line in file:
            records.append(line.strip("\n"))

    # records = np.array(records).sort()
    records = sorted(records)
    i = 0
    records_dict = {}
    while i < len(records):
        if len(records[i].split(" ")) == 6:
            j = i + 1
            guard = records[i].split(" ")[3].strip("#")
            if guard not in records_dict:
                records_dict[guard] = {"minutes":[]
                                      ,"time":[]}
            while j < len(records)-1 and len(records[j].split(" ")) != 6:
                records_dict[guard]["minutes"].append(calc_asleep(records[j], records[j+1]))
                for m in get_minutes(records[j], records[j+1]):
                    records_dict[guard]["time"].append(m)
                j += 2
            i += 1
        else: 
            i += 1

    guard_most = 0
    count_most = 0
    minute_most = 0
    for guard in records_dict:
        if records_dict[guard]["time"] == []:
            pass
        else:
            # print(guard)
            (values,counts) = np.unique(np.array(records_dict[guard]["time"]),return_counts=True)
            ind=np.argmax(counts)
            records_dict[guard].update({"most_minute":values[ind]
                                        ,"count":np.max(counts)})
            # print(records_dict[guard]['most_minute'])
            # print(records_dict[guard]['count'])
            # print("----------------------------")
            if records_dict[guard]['count'] > count_most:
                guard_most = guard
                count_most = records_dict[guard]['count']
                minute_most = records_dict[guard]['most_minute']
    """
        Answer: Guard 1327 * Minute 24 = 31848
    """

    print("Guard: ", guard_most, " Minute: ", minute_most
        , "Results: ", int(guard_most) * int(minute_most))


if __name__ == "__main__":
    if sys.argv[1] == "part_1":
        part_1()
    elif sys.argv[1] == "part_2":
        part_2()
    else:
        print("Syntax: python day4.py ($part_1/part_2)")

