# Day 3 of the 2024 Advent of Code
def mulRes(eq):
    if eq==[]: return 0
    A,B = '',''
    closeA = False
    i=0
    while i<len(eq):
        if eq[i].isdigit():
            if not closeA:
                A = A+eq[i]
                if len(A)>3: return 0
                if eq[i+1]==",":
                    closeA = True
                    i += 1
            else:
                B = B+eq[i]
                if len(B)>3: return 0
                if eq[i+1]==")": return int(A)*int(B)
        else: return 0
        i += 1

# Read input file
with open("../include/input3.inc","r") as mul_file:
    mul_list = mul_file.readlines()

########################### Part 1 ###########################
mul_sum = 0
for line in mul_list:
    eq_list = (line.strip()).split("mul(")
    for each in eq_list:
        mul_sum += mulRes([i for i in each][0:8])
        
print("Part 1: %s"%mul_sum)

########################### Part 2 ###########################
# remove muls that show after a don't()"" from mul_list
#print("Part 2: %s"%safe_count)