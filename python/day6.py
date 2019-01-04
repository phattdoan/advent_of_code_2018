import sys
import numpy as np
import pprint as pp

DATA_FILE = "../data/day6.txt"

def calc_manhattan_dist(coord1, coord2):
    """
        calculate manhattan distance
        args: coordinates
        return: manhattan distance
    """
    return abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1])

def create_coord_key(coord1, coord2):
    return str(str(coord1)+"|"+str(coord2))

coord_list = []
coord_dict = {}
with open(DATA_FILE) as file:
    for line in file:
        x, y = line.strip("\n").split(" ")
        coord_list.append([int(x.strip(",")), int(y.strip())])
        coord_dict[create_coord_key(int(x.strip(",")), int(y.strip()))] = {}

for x in range(0,500):
    for y in range(0,150):
        ## for each [x,y] coordinate, get distance 
        ## to the pre-defined coordinate
        # print(x,y)
        dist_list = []
        for coord in coord_list:
            dist = calc_manhattan_dist([x,y], coord)
            dist_list.append(dist)
        
        sorted_dist_list = sorted(dist_list)
        # print(sorted_dist_list)
        # print(coord_list[np.array(dist_list).argsort()[0]])
        flag_closest = False
        for i, dist in enumerate(sorted_dist_list[:-1]):
            if dist != sorted_dist_list[i+1]:
                flag_closest = True
                break
        
        if flag_closest:
            key = create_coord_key(coord_list[np.array(dist_list).argsort()[0]][0],coord_list[np.array(dist_list).argsort()[0]][1])
            coord_dict[key].update({create_coord_key(x,y):sorted_dist_list[0]})
    #     break
    # break


coords = list(coord_dict.keys())
closests = []
for coord in coord_dict:
    closests.append(len(coord_dict[coord].keys()))

for idx in np.array(closests).argsort():
    print(closests[idx], coords[idx])
    print(coord_dict[coords[idx]])
