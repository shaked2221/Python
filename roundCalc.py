# shaked astemker 311499917
def mul1(x,y):
    "func that mul 2 int num"
    return x*y

def rest_by_10(z):
    "return the rest of dvide by 10"
    return z%10
    

def roundUpMul(x,y):
    "mul 2 number and reutn the circlr up dvide by 10witout rest"
    z=mul1(x,y)
    r=rest_by_10(z)
    if(z>=0):
        if (r != 0):
            x=10-r
            return z+x
        else:
            return z
    else:# if num is nagtive
        if (r!=0):
            x=10-r
            return z+x
        else:
            return z

def roundDownMul (x,y):
    "mul 2 number and reutn the circlr down dvide by 10witout rest"
    z=mul1(x,y)
    r=rest_by_10(z)
    if(z>=0):
        if (r != 0):
            return z-r
        else:
            return z
    else:# if num is nagtive
        if (r!=0):
            x=10-r
            x=10-x
            return z-x
        else:
            return z


def roundMax (x,y):
    "get 2 num return the bigest after circle up to close dvide 10 witoutrest use roundUpMul for help "
    if(x>=y):
        return roundUpMul(x,1)
    return roundUpMul (y,1)
    
        
    
        
      
