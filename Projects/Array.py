class Array(object):
    def __init__(self,initialsize):
        self.__a = [None] * initialsize
        self.nItems = 0
        
    def __len__(self):
        return self.nItems
    
    def get(self,n):
        if 0 <= n and n <self.nItems:
            return self.__a[n]
        
    def set1(self,n, value):
        if 0 <= n and n <self.nItems: 
            self.__a[n] = value
            
    
    def insert(self,item):
        self.__a[self.nItems] = item
        self.nItems +=1
        
        
    def find(self,item):
        for i in range(self.nItems):
            if self.__a[i ] == item:
                return i 
        return False
    
    def search(self,item):
        return self.get(self.find(item))
    
    
    def delete(self,item):
        for i in range(self.nItems):
            if self.__a[i] ==item:
                for k in range(i ,  self.nItems):
                    self.__a[k] = self.__a[k+1]
        return True
    def traverse(self, function=print):
        for j in range(self.nItems):
            function(self.__a[j])
            
            
            
            
            
            
            

arr = Array(10)
arr.insert(99)
arr.insert("bar")
arr.insert(44)
arr.insert(55)
arr.insert(12.34)
arr.insert(0)
arr.insert("baz")

print("Array containing", len(arr), "items")
arr.traverse()
print("Search for 12 returns", arr.search(12))
print("Search for 12.34 returns", arr.search(12.34))
print("Deleting 0 returns", arr.delete(0))
print("Deleting 17 returns", arr.delete(17))
print("Setting item at index 3 to 33")
arr.set1(3, 33)

#########


w = "ariyan"
print(isinstance(w,(int,float)))   


