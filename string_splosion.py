def string_splosion(str):
    n=len(str)+1
    newStr=""
    for x in range(n):
        newStr=newStr+str[:x]
    return newStr