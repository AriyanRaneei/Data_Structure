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
            queue[self.rear]= data
