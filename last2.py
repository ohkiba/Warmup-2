def last2(str):
    count=0
    last2Str=str[len(str)-2:len(str)]
    if len(str)<=2:
        return 0
    for x in range(len(str)):
        checkStr=str[x-2:x]
        if checkStr==last2Str:
            count+=1
    return count