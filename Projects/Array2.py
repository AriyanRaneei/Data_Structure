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
    
    def getMaxnum(self):
        
        for i in range(self.nItems):
           
            if isinstance(self.__a[i],(int,float)) ==True: 
                if self.__a[i]> self.__a[0]: 
                    self.__a[0] = self.__a[i]
                    self.__a[i] += 1
        return self.__a[0]
                  
             
    
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
arr.insert(9)
arr.insert("bar")
arr.insert(440)
arr.insert(550)
arr.insert(12.34)
arr.insert(9000)
arr.insert("baz")
print(arr.getMaxnum())



