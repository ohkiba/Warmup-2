def array123(nums):
    count=0
    for x in range(len(nums)):
        if nums[x:x+3]==[1,2,3]:
            count+=1
    return (count>0)