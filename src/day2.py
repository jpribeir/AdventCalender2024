# Day 2 of the 2024 Advent of Code
def diffSign(a,b):
    if a==b: return 0,0
    return (a-b)/abs(a-b),abs(a-b)

def checkSafety(report):
    prev_sign,diff = diffSign(report[1],report[0])
    if diff>3 or diff==0: return 0,1
    for i in range(2,len(report)):
        new_sign,diff = diffSign(report[i],report[i-1])
        if new_sign*prev_sign<0: return 0,i
        if diff>3 or diff==0: return 0,i
    return 1,0

def problemDampener(report):
    first_try,stop = checkSafety(report)
    if first_try: return 1
    else:
        second_try,_ = checkSafety(report[0:stop-1]+report[stop:])
        if second_try: return 1
        else:
            third_try,_ = checkSafety(report[0:stop]+report[stop+1:])
            if third_try: return 1
            elif stop>1:
                forth_try,_ = checkSafety(report[0:stop-2]+report[stop-1:])
                return forth_try
            else: return 0

# Read input file
with open("../include/input2.inc","r") as report_file:
    report_list = report_file.readlines()

########################### Part 1 ###########################
safe_count = 0
for line in report_list:
    inc,_ = checkSafety(list(map(int,line.split())))
    safe_count += inc
print("Part 1: %s"%safe_count)

########################### Part 2 ###########################
safe_count = 0
for line in report_list:
    safe_count += problemDampener(list(map(int,line.split())))
print("Part 2: %s"%safe_count)