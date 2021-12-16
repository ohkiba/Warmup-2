def front_times(str, n):
    front=str[:3]
    newStr=""
    for x in range(n):
        newStr=newStr+front
    return newStr  