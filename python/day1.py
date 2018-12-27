"""
12/26/2018
https://adventofcode.com/2018/day/1
"""

import os

STARTING_FREQUENCY = 0

DATA_FILE = '../data/day1.txt'

def part_1():
    result = STARTING_FREQUENCY
    with open(DATA_FILE) as infile:
        for line in infile:
            freq_change  = int(line)
            result += freq_change
    return result 

def part_2():
    freq_count = {}
    flag = False

    ## grab the list of frequencies
    freq_change_list = []
    with open(DATA_FILE) as infile:
        for line in infile:
            freq_change_list.append(int(line))

    ## loop through the frequency list until
    ## double frequency was found per problem
    ## indication
    result = STARTING_FREQUENCY            
    while flag == False:
        i = 0

        while i <= len(freq_change_list):
            if i == len(freq_change_list):
                i = 0
            else:
                result += freq_change_list[i]
                if result not in freq_count:
                    freq_count[result] = 1
                else:
                    freq_count[result] += 1
                    flag = True
                    break
                i += 1

    return result

            
# print(part_1())
print(part_2())