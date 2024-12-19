def display(n):
    if n ==0:
        return 1
    else:
        print(n-1,end="/")
        return display(n-1)
    
    
    
def Listreturn(ls):
    if len(ls) ==1:
        return ls[0]
    else:
        return ls[0] + Listreturn(ls[1:])
    

def toString(n,base):
    convertstring ="0123456789abcdef"
    if n <base:
        return convertstring[n]
    else:
        return toString(n//base,base)+ convertstring[n%base]
    
    
def tilo(n):
    if n <2:
        return 1
    else:
        return 1/ n+tilo(n-1)
    
def ariyan(n):
    for i in range(1,n+1):
        yield i
        
s = ariyan(1000)
print(next(s))
print(next(s))
def boil_down_array(key,data):
    if type(data) ==dict:
        for key, item in data.items():
            yield from boil_down_array(key, item)
            
    else:
        yield {key:data}
        
        
key= "ariyan" 
data =[1234,12]  
p = boil_down_array(key, data)
for i in p:
    print(i)



sp = {"data":12}




###############
def boyboy(n,b,d):
    if n ==1:
        return 1
    else:
        return boyboy((n-1/b)+d,b,d)
    
    
   
################
def recursive(n):
    if n == 1:
        return 1
    else:
        return recursive(n-1)+ recursive(n-1)
    
    
# this program is running by 2**(n-1) for the numbers upper then 4


def Dc(a,n):
    if n == 1:
        return a
    if n %2 ==0:
        return (Dc(a,n//2)*Dc(a,n//2))
    else:
        return (a*Dc(a, n-1))
    
