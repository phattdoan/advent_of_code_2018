"""
12/27/2018
https://adventofcode.com/2018/day/3
"""

import numpy as np

DATA_FILE = '../data/day3.txt'
DIMENSION_X = 1000
DIMENSION_Y = 1000

def create_array(left_edge, right_edge, width, height, claims_id = 1):
    """
        Create a numpy array by taking in the measurement provided
        by the problem
    """
    array = np.zeros((DIMENSION_X, DIMENSION_Y))    
    for i in range(right_edge, right_edge + height):
        for j in range(left_edge, left_edge + width):
            array[i,j] = claims_id
    return array

def part_1():
    """
        Use numpy array to check overlay for each claim fabric
        For the matrix of 1000x1000, no fabric is represented as 0s
        and with fabric as 1s
        Adding matrix to find those area with total sum > 1 would mean
        there is an overlap between the fabric
    """
    start_array = np.zeros((DIMENSION_X, DIMENSION_Y))
    with open(DATA_FILE) as main:
        for line in main:
            claims_id, misc, edges, width_height = line.split(" ")
            left,right = edges.strip(":").split(",")
            width, height = width_height.strip().split("x")
            start_array = np.add(start_array, create_array(int(left), int(right), int(width), int(height)))
    
    return start_array


def part_2():
    """
        Use numpy array to check overlay for each claim fabric
        For the matrix of 1000x1000, no fabric is represented as 0s
        and with fabric as the claim_id for that fabric (i.e. 123)
        Adding matrix to find those area with total sum > 1 would mean
        there is an overlap between the fabric
        Fabric without overlap will maintain their claim_id fabric code
    """
    claims_dict = {}
    start_array = np.zeros((DIMENSION_X, DIMENSION_Y))
    with open(DATA_FILE) as main:
        for line in main:
            claims_id, misc, edges, width_height = line.split(" ")
            left,right = edges.strip(":").split(",")
            width, height = width_height.strip().split("x")
            claims_id = int(claims_id.strip("#"))
            claims_dict[claims_id] = {'array':create_array(int(left), int(right), int(width), int(height), claims_id)
                                     ,'area': int(width)*int(height)}
            start_array = np.add(start_array,claims_dict[claims_id]['array'])

    
    result = 0
    for claim in claims_dict:
        # print("claim id: ", claim)
        # print("count: ", np.count_nonzero(start_array == claim))
        # print("area: ", claims_dict[claim]['area'])
        # print("-----------------------")
        if np.count_nonzero(start_array == claim) == claims_dict[claim]['area']:
            result = claim
            break
    return result

# print(np.count_nonzero(part_1() > 1))
print(part_2())



######################################
## SANDBOX
######################################
# array1 = np.array([[2,2,2],[2,2,2]])
# array2 = np.array([[1,1,1],[1,1,1]])

# print(np.add(array1,array2))


