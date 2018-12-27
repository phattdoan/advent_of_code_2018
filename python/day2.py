"""
12/26/2018
https://adventofcode.com/2018/day/2
"""

import os

FILE_NAME = "../data/day2.txt"

def part_1(file):
    """
        Part 1 of day 2
        For example, if you see the following box IDs:
            abcdef contains no letters that appear exactly two or three times.
            bababc contains two a and three b, so it counts for both.
            abbcde contains two b, but no letter appears exactly three times.
            abcccd contains three c, but no letter appears exactly two times.
            aabcdd contains two a and two d, but it only counts once.
            abcdee contains two e.
            ababab contains three a and three b, but it only counts once.
            Of these box IDs, four of them contain a letter which appears exactly twice,
            and three of them contain a letter which appears exactly three times.
            Multiplying these together produces a checksum of 4 * 3 = 12.
        arg: file name
        return: checksum

    """
    with open(file) as infile:
        ## set dict to keep track of unique 2 and 3 count for each box ID
        count_2_3 = {2:0
                    ,3:0}

        ## take in a line and process count
        for line in infile:
            letters = list(line.strip("\n"))
            letter_count = {}

            ## count letter frequency
            for l in letters:
                if l not in letter_count:
                    letter_count[l] = 1
                else:
                    letter_count[l] += 1

            ## inverse frequency count for checksum
            freq = []
            for l in letter_count:
                freq.append(letter_count[l])

            if 2 in freq:
                count_2_3[2] += 1

            if 3 in freq:
                count_2_3[3] += 1

    return count_2_3[2]*count_2_3[3]


def compare_id(id1, id2):
    """
        count common characters between 2 strings
        arg: str1, str2
        return: count
    """
    count = 0
    for i1, i2 in zip(id1,id2):
        if i1 != i2:
            count += 1
        if count > 1:
            break
    return count

def get_common(id1, id2):
    """
        find common characters between 2 strings
        arg: str1, str2
        return: common characters as a string
    """
    common = ''
    for i1, i2 in zip(id1,id2):
        if i1 == i2:
            common += i1
    return common

def part_2(file):
    line1_count = 0
    flag = False

    ## main loop to compare ids
    with open(file) as main:
        for line1 in main:
            box_id1 = line1.strip("\n")

            ## inner loop to compare box_id to those it has not been
            ## compared yet
            line2_count = 0
            with open(file) as inner:
                for line2 in inner:
                    if line1_count >= line2_count:
                        pass
                    else:
                        box_id2 = line2.strip("\n")
                        if compare_id(box_id1, box_id2) == 1:
                            flag = True
                            break
                    line2_count += 1
            
            if flag == True:
                break

            line1_count += 1
    
    if flag == True:
        return get_common(box_id1, box_id2)
    else:
        return "No match found"

# print(part_1(FILE_NAME))            
print(part_2(FILE_NAME))            