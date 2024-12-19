def BubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]> arr[j+1]:
                arr[j], arr[j+1] = arr[j+1],arr[j]
                swapped =True
                
        if (swapped == False):
            break
        
        
        
if __name__ == "__main__":
    arr = [2,3,43,32,43,1,1,98,100,4,]  
    BubbleSort(arr)
    
for i in range(len(arr)):
    print(arr[i])
