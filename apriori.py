def apriori(Data,min_support):
    C1 = {}
    for line in Data:                 #把第一项集存放到C1中                                                      
        for item in line:
            if item in C1:
                C1[item] += 1
            else:
                C1[item] = 1
    keys_1 = C1.keys()                 
    keys1 = []
    for key in keys_1:                #把keys_1列表存放到keys1中（keys_1=[['a'],['b'],['c']]    keys1=['a','b','c',]）
        keys1.append([key])
    length = len(Data)

    remain_keys = []
    for k in keys1:                     #删除支持度小于置信度的第一项集
        if C1[k[0]] * 1.0 / length >= min_support:
            remain_keys.append(k)
    remain_keys.sort()
    keys = remain_keys
    all_keys = []
    while remain_keys != []:            #递归的把所有频繁项集存放到all_keys中
        C = getCount(Data, remain_keys)
        remain_keys = deleteKeys(remain_keys,C,min_support, length)
        for key in remain_keys:
            all_keys.append(key)
        remain_keys = aprioriGen(remain_keys)
    return all_keys



def getCount(Data, keys):               #计算支持度
    C = []
    for key in keys:
        count = 0
        for line in Data:
            have = True
            for k in key:
                if k not in line:
                    hava = False
            if have:
                count += 1
        C.append(count)
    return C


def deleteKeys(keys, C, min_support, length):   #删除支持度小于置信度的结点
    for i, key in enumerate(keys):
        if float(C[i]) / length < min_support:
            keys.remove(key)
        return keys


def aprioriGen(keys):                           #把集合中所有频繁子项集输出合并
    result_key = []
    for keys1 in keys:
        for keys2 in keys:
            if keys1 != keys2:
                key = []
                for k in keys1:
                    if k not in key:
                        key.append(k)
                for k in keys2:
                    if k not in key:
                        key.append(k)
                key.sort()
                if key not in result_key:
                    result_key.append(key)
    return result_key

Data = [['A','B','C','D'],['B','C','E'],['A','B','C','E'],['B','D','E'],['A','B','C','D']]
F = apriori(Data, 0.7)
print '\nfrequent itemset:\n', F
