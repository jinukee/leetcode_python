def duplicateZeros(arr):
    n = len(arr) - 1
    count = 0
    for i in arr : 
        if i == 0 : count += 1
    
    i = n
    p = n + count
    
    while i >= 0 and p >= 0:
        if arr[i] != 0 :
            if p <= n : arr[p] = arr[i]
        else : 
            if p <= n : arr[p] = arr[i]
            p -= 1
            if p <= n : arr[p] = arr[i]
        
        i -= 1
        p -= 1
    
    return arr

print(duplicateZeros([1,0,2,3,0,4,5,0]))
