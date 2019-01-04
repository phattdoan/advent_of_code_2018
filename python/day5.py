import sys
import numpy as numpy

DATA = "../data/day5.txt"

with open(DATA) as file:
    for line in file:
        polymers = line.strip().strip("\n")

print(len(polymers))
polymer_list = list(polymers)

# polymer_list = list("aABcCbdeeDdcD")

processed_polymer = ["_"]

for idx, unit in enumerate(polymer_list):
    previous = str(processed_polymer[-1])
    # print(previous, unit)
    if previous != unit and previous.lower() != unit.lower():
        processed_polymer.append(unit)
    else:
        processed_polymer.pop()

    # print(polymer_list)
    # print(processed_polymer)
    # print("----------------")

print(len(polymer_list))
print(len(processed_polymer)-1)
# print(processed_polymer[:5])
# print(processed_polymer[27100:])





## SANDBOX
line = open("../data/day5.txt").read().splitlines()[0]

oldline = None
while oldline != line:
    oldline = line
    for i in range(0,26):
        line = line.replace(chr(ord("a") + i) + chr(ord("A") + i),"")
        line = line.replace(chr(ord("A") + i) + chr(ord("a") + i),"")

print("Part1:")
print(len(line))

original = line
best = len(line)
for j in range(0,26):
    line = original
    line = line.replace(chr(ord("a") + j),"")
    line = line.replace(chr(ord("A") + j),"")
    oldline = None
    while oldline != line:
        oldline = line
        for i in range(0,26):
            line = line.replace(chr(ord("a") + i) + chr(ord("A") + i),"")
            line = line.replace(chr(ord("A") + i) + chr(ord("a") + i),"")

    best = len(line) if len(line) < best else best
print("Part2:")
print(best)