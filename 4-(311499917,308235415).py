import math
import random
#311499917 shaked astemker and ilan yadgrov 308235415
def integrate(a,b,f):
    "func that give you the integral by monta carlo method"
    max2=f(a)#deful max
    for i in range (a,b+1):#it whill give the max on y arry
        if (f(i)>max2):
            max2=f(i)
    
    n=100000#num of times that arrow throw by mont carlo
    hits = 0  # initialize hits with 0
    for i in range(n):
        x = random.uniform (a,b)
        y = random.uniform (0,max2)
        if ((f(x))>y):#if the arrow is above the func in the point dont it 
            hits=hits+1 
    return ((b-a)*(max2))*(hits/100000)#sum of sqar * % of hits

               
print(integrate(2,4,lambda x: x+2))
print(integrate(2,4,lambda x: x**2+2))

