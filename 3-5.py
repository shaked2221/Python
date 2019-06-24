empty_rlist = None
def make_mutable_rlist(list12=None):
    "func that make mutavle rlist"
    contents = empty_rlist
    def length():
        "return lenget list"
        return len_rlist(contents)
    def get_item(ind):
        "fun help bring item in insex"
        return getitem_rlist(contents, ind)
    def push_first(value):
        "add value"
        nonlocal contents
        contents = make_rlist(value, contents)
    def pop_first():
        "out the firest vale"
        nonlocal contents
        f = first(contents)
        contents = rest(contents)
        return f
    def strz():
        "return string of the list"
        temp_first=contents
        strig='['
        while(temp_first!=empty_rlist):
            strig+=str(first(temp_first))+','
            temp_first=rest(temp_first)
        strig=strig[0:-1]
        strig+=']'
        return strig

    def get_iterator():
        def haxNext():
            return True if contents else False
        def next():
            nonlocal contents
            f=first(contents)
            contents=rest(contents)
            return f
        return {'hasNext':haxNext , 'next':next,}
    
    def slice_(index_1, index_2):
        "return vale frome 2 index"
        new_list=make_mutable_rlist()
        index=index_2-1
        for _ in range(index_2-index_1):
            new_list['push_first'](get_item(index))
            index-=1
        return new_list

    
    def insert(index, num):
        "func thet insert value in some index"
        nonlocal contents
        #temp_first=contents
        h=[]
        for _ in range(index):
            h.append(first(contents))
            contents=rest(contents)
        #print(h)
        push_first(num)
        for i in range(index-1,-1,-1):
            push_first(h[i])
             
    return {'length':length, 'get_item':get_item, 'push_first':push_first, 'pop_first': pop_first, 'str':strz, 'slice':slice_, 'insert':insert ,'get_iterator':get_iterator, }



def make_rlist(first, rest):
    "make the lise"
    return (first, rest)
def first(l):
    "rituen firest iteam"
    return l[0]
def rest(l):
    "return second iream"
    return l[1]

def len_rlist(l):
    "reutn length list"
    length = 0
    while l != empty_rlist:
        l, length = rest(l), length + 1
    return length
def getitem_rlist(l, i):
    "bring iteam in specipc index"
    while i > 0:
        l, i = rest(l), i - 1
    return first(l)










