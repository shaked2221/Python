def make_sequence(x):
    def all_filter(func=None):
        """ filter all the list by func who give by the user"""
        if(func==None):
            return tuple(x)
        new_list=[]
        for i in range(len(x)):
            if func(x[i]):
                new_list+=[x[i]]
        return tuple (new_list)
    
    def return_filter(func=None):
        """func who get taple and [rint her from begining to end and revrse0"""
        if(func==None):
            return tuple(x)
        temp_t=all_filter(func)
        j=0
        def next2():
            """ print start from the begin to lest """
            nonlocal j
            print( temp_t[j])
            j=(j+1)%len(temp_t)
        def reverse():
            """ print start from the end to fires """
            nonlocal j
            j=((j-1)%(len(temp_t)))
            print( temp_t[j])
            
        return{'next':next2, 'reverse': reverse}

    def reverse():
        """return revrese tuple"""
        new_t=()
        for i in range(len(x)-1,-1,-1):
            new_t+=(x[i],)
        return new_t

    def extend(s):
        """ extend the seq by seq who goven"""
        nonlocal x
        x+=s
    def clear( ):
        """ clear all the sequnce"""
        nonlocal x
        x=[]

    return{'all_filter': all_filter, 'return_filter': return_filter, 'reverse': reverse, 'extend': extend, 'clear': clear }


        
        
