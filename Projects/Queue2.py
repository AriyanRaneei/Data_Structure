class Queue(object):
    def __init__(self,size):
        self.size = size
        self.__QueueList = [None] *size
        self.__rear = 0
        self.__front = 1
        self.__nItems = 0
        
        
    def insert(self,item):
        if   self.isFull():
            raise Exception("Queue overflow")
        self.__rear += 1
        
        if self.__rear ==self.size:
            self.__rear = 0
        self.__QueueList[self.__rear]= item
        self.__nItems += 1
        
            
    
    
    def remove(self):
        if self.isEmpty():
            raise Exception("queque onderflow")
        front = self.__QueueList[self.__front]
        self.__QueueList[self.__front] = None
        
        if self.__front ==self.__rear:
            self.__front =0
        
        self.__nItems -= 1
        return front
    
    
    def peek(self):
        return None if self.isEmpty() else self.__QueueList[self.__front]
    
    def isEmpty(self):
        return self.__nItems ==0
    
    def isFull(self):
        return self.__nItems == self.size
    
    def __len__(self):
        return self.__nItems
    
    def show(self):
    
    
       return [print(data,end=", ") for data in self.__QueueList if data !=None]
    
