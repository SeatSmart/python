'''for i in dict_cl:
    keys = list(dict_cl.keys())
    clslst = list(dict_cl.values())
    for m in range(len(clslst)):
        values = list(clslst[m].keys())
        print()
        print(values)
        print("Room : ", keys[m])
        print()
        if (len(values) == 2):
            k1 = values[0]
            k2 = values[1]
            for j in range(1, 43):
                if (j%2 != 0):
                    if (k1 in allot):
                        if (allot[k1]+1 <= dict2[k1] and allot[k1]+1 not in dict3[k1]):
                            allot[k1] += 1
                        elif (allot[k1]+1 <= dict2[k1] and allot[k1]+1 in dict3[k1]):
                            allot[k1] += 2
                        elif (allot[k1]+1 > dict2[k1]):
                            continue
                    else:
                        if (1 not in dict3[k1]):
                            allot[k1] = 1
                        else:
                            allot[k1] = 2
                    print(j, " - ", k1, allot[k1])
                else:
                    if (k2 in allot):
                        if (allot[k2]+1 <= dict2[k2] and allot[k2]+1 not in dict3[k2]):
                            allot[k2] += 1
                        elif (allot[k2]+1 <= dict2[k2] and allot[k2]+1 in dict3[k2]):
                            allot[k2] += 2
                        elif (allot[k2]+1 > dict2[k2]):
                            continue
                    else:
                        if (1 not in dict3[k2]):
                            allot[k2] = 1
                        else:
                            allot[k2] = 2
                    print(j, " - ", k2, allot[k2])
        else:
            k1 = values[0]
            for j in range(1, 43):
                if (j%2 != 0):
                    if (k1 in allot):
                        if (allot[k1]+1 <= dict2[k1] and allot[k1]+1 not in dict3[k1]):
                            allot[k1] += 1
                        elif (allot[k1]+1 <= dict2[k1] and allot[k1]+1 in dict3[k1]):
                            allot[k1] += 2
                        elif (allot[k1]+1 > dict2[k1]):
                            continue
                    else:
                        if (1 not in dict3[k1]):
                            allot[k1] = 1
                        else:
                            allot[k1] = 2
                    print(j, " - ", k1, allot[k1])'''
