def string_match(a, b):
    count=0
    shorter=min(len(a),len(b))
    for x in range(shorter-1):
            if a[x:x+2]==b[x:x+2]:
                count+=1
    return count