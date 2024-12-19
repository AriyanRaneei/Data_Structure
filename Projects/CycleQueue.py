class CycleOueue:
    def __init__(self,initialsize):
        self.initialsize =initialsize
        self.queue = [None] * initialsize
        self.front = -1
        self.rear = -1
    def enqueue(self,data,function=print):
        if ((self.rear+1)% self.initialsize==self.front):
            function("FULL")
        
        elif (self.front ==-1):
            self.front = 0 
            self.rear = 0
            
        else:
            self.rear = (self.rear+1)%self.initialsize
            self.queue[self.rear]= data
            
            
            
    def dequeue(self,function=print):
        if (self.front ==-1):
            function("EMPTY")
        elif (self.front ==self.rear):
            t = self.queue[self.front]
            self.front = -1
            self.rear = -1
            return t
        
        else:
            t = self.queue[self.front]
            self.front = (self.front+1)%self.initialsize
            return t
    
    
    def traverse(self,function=print):  
        for i in range(self.front,self.rear+1):
            function(self.queue[i],end=' ')
        function()
        
        
        
cyque = CycleOueue(4)
cyque.enqueue("ariyan")
