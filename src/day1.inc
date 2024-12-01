# Day 1 of the 2024 Advent of Code

# Read input file
with open("../include/input1.inc","r") as ID_file:
    ID_list = ID_file.readlines()

########################### Part 1 ###########################
listA = []
listB = []
for line in ID_list:
    idA,idB = line.split()
    listA.append(int(idA))
    listB.append(int(idB))
listA.sort()
listB.sort()

print("Part 1: %s"%sum(list(map(lambda x,y: abs(x-y),listA,listB))))

########################### Part 2 ###########################
similarity_dict = {}
for x in listA:
    if x not in similarity_dict.keys(): similarity_dict[x] = (listB.c ount(x))*x
print("Part 2: %s"%sum(similarity_dict.values()))