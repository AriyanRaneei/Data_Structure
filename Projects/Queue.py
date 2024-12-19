#queue
class Oueue:
    def __init__(self,initialsize):
        self.initialsize =initialsize
        self.queue = [None] * initialsize
        self.front = -1
        self.rear = -1
        
    def display(self):
        if (self.front ==-1):
            print("EMPTHY")
        for i in range(self.front,self.rear+1):
            print(self.queue[i],end=' ')
        print()
        
    def enqueue(self,data):
        if ((self.rear+1)== self.initialsize):
            print("full")
        elif (self.front ==-1):
            self.front = 0
            self.rear = 0
            self.queue[self.rear]= data
        else:
            self.rear +=1
            self.queue[self.rear]= data
            
    def dequeque(self):
        if (self.front ==-1):
            print("EMPTHY")
        #  if we have one element
        elif (self.front == self.rear):
            t = self.queue[self.front]
            self.front = -1
            self.rear = -1
            return t
        else:
            t = self.queue[self.front]
            self.front +=1
            return t
            
        
        
        
queue =Oueue(5)
queue.enqueue("ariyan")
queue.enqueue("sara")   
