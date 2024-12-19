def selectionsort(arr,size):
    for i in range(size):
        min_index = i
        for j in range(i+1,size):
            if arr[j]< arr[min_index]:
                min_index = j 
                
        (arr[i], arr[min_index]) = (arr[min_index], arr[i])
    return arr

arr = [1,53,123,53,2,1,3,453,65,323,49,31,]
print(selectionsort(arr, len(arr)))    
