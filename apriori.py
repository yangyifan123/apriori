import sys

def apriori:
    C1 = {}
    for line in Datas:
        for item in line:
            if item in C1:
                C1[item] += 1
            else:
                C1[item] = 1
    keys1 = C1.keys()
    keys = []
    for key in keys1:
        keys.append([key])
