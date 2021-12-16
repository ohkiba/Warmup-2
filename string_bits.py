def string_bits(str):
    n=len(str)
    newStr=""
    for x in range(n):
        if x%2==0:
            newStr=newStr+str[x]
    return newStr