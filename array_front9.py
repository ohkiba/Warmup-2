def array_front9(nums):
    count=0
    if len(nums)>4:
        for x in range(4):
            if nums[x]==9:
                count+=1
    else:
        for x in range(len(nums)):
            if nums[x]==9:
                count+=1
    return (count>0)