class Queue(object):
    def __init__(self,size):
        self.__maxSize = size
        self.__que = [None] *size
        self.__front = -1
        self.__rear = -1
        self.__nItems = 0
        
    def insert(self,item):
        if self.isFull():
            raise Exception("Queue overflow")
        self.__rear +=1
        if self.__rear == self.__maxSize:
            self.__rear = 0
        self.__que[self.__rear] = item
        
        self.__nItems +=1
        return True
    def remove(self):
        if self.isEmpty():
            raise Exception("Queue underflow")
        front = self.__que[self.__front]
        self.__que[self.__front] = None
        self.__front +=1
        if self.__front == self.__maxSize:
            self.__front = 0
        self.__nItems -= 1
        return front
    
    
    def peek(self):
        return None if self.isEmpty() else self.__que[self.__front]
    
    
    def isEmpty(self):
        return self.__nItems ==0
    
    
    
    def isFull(self):
        return self.__nItems == self.__maxSize
    
    
    def __len__(self):
        return self.__nItems
    
    
    
    
    def show(self):
        for data in self.__que:
            if data is not None: 
                print(data,'\n')
            
            
my_que = Queue(10)
for i in ["ariyan","ayda","akbar","dara","sara","sima"]:
    my_que.insert(i)          
            
    
    
print("ΩΩΩΩΩΩΩ.Ω⌡ΩΩΩΩΩΩ")
my_que.remove()

my_que.remove()

my_que.remove()
my_que.remove()
my_que.remove()
my_que.show()
