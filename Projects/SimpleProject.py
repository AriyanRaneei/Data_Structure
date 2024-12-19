class MyClass:
    x = 0
    y = ""

    def __init__(self, anyNumber, anyString):
        self.x = anyNumber
        self.y = anyString

myObject = MyClass(12345, "Hello")

print(myObject.__str__())
print(myObject.__repr__())
print(myObject)


class MyClass2:
    x = 0
    y = 0
    def __init__(self,anynumber, anyString):
        self.x = anynumber
        self.y = anyString
    
    def __str__(self):
        return 'myclass(x = '+str(self.x)+ ',y'+self.y +')'
    
myo2 = MyClass2(12343, "hello")

print(myo2.__str__())        
print(str(myo2))
print(myo2.__repr__())     
