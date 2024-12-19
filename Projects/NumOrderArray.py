class NumOrderArray(object):
    def __init__(self,initialsize):
        self.__a = [None] *initialsize
        self.__nItems = 0
        
   
    
    def find(self,item):
        lo = 0
        hi = self.__nItems -1
        while lo<=hi:
            mid = (lo + hi) //2
            if self.__a[mid] ==item:
                return mid
            elif self.__a[mid]<item:
                lo =  mid +1
                
            else:
                hi = mid -1
                return lo
            
    def search(self,item):
        index = self.find(item)
        if index <self.__nItems and self.__a[index] == item:
            return self.__a[index]
   
    
   
    def insert(self,item):
        if self.__nItems>=len(self.__a):
            raise Exception("Array overflow")
            
        index = self.find(item)
        
        for j in range(self.__nItems,index,-1):
            self.__a[j] = self.a[j-1] 
            self.__a[index] = item
            self.__nItems +=1
            
            
