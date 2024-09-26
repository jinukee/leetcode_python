def findMaxConsecutiveOnes(nums) :
    currunt_Max = 0
    count = 0
    for i in nums:
        if i == 1 : count += 1
        else : 
            currunt_Max = max(count, currunt_Max)
            count = 0
    
    return max(count, currunt_Max)

print(findMaxConsecutiveOnes([1,1,0,1,1,1]))
print(findMaxConsecutiveOnes([1,0,1,1,0,1,1,1,1,1,1,0,0,0]))