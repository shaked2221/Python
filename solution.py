#shaked astemker 311499917 and ilan yadgrov 308235415
#1
from functools import reduce

def make_matrix(rowCount, colCount, dataList): #311499917 id shaked astemker and 308235415 ilan yadgrov
    """
    function of make matrix
    """
    
    def dispatch(op):#the dispach
        "select dispch your option"
        if (op=="n"):
            return rowCount
        if (op=="m"):
            return colCount
        if (op=="matix"):
            return dataList

    return dispatch

def n(mat):
    "return col"
    return mat('n')
def m(mat):
    "return row"
    return mat('m')
def matrix(mat):
    "print date matrix"
    return mat('matix')
def PrintMatrix(mat):
    "print the matrix"
    arr=matrix(mat)
    for i in range(n(mat)):
        for j in range(m(mat)):
            print(arr[j+i*m(mat)], end=' ')#print by formal of list 
        print()
def AddMatrix(mat1,mat2):
    "combin 2 mat to 1"
    if (m(mat1)!= m(mat2) or n(mat1)!=n(mat2)):#checl if size is same
        return("eror matrix in not same size")
    
    list1=matrix(mat1)
    list2=matrix(mat2)
    new_mat=[]
    for i in range(len(list1)):
        new_mat.append(list1[i]+list2[i])
    return make_matrix(n(mat1),m(mat1),new_mat)

def MulMatrix(mat1,mat2):
    "this function multiplie between 2 matrixs and give new one "
    newlist = []
    list1=matrix(mat1)
    list2=matrix(mat2)
    r1=n(mat1)
    c1=m(mat1)
    r2=n(mat2)
    c2=m(mat2)
    if (r1!=c2):
        print("eror cant multy becase row and col dont match so it do it but it is not ilgiel")
    z=0
    while z<r1:
        for i in range(c2):
            sum=0
            for j in range (r2):
                num1=list1[j+z*c1]
                num2=list2[i+j*c2]
                sum+=((num1)*(num2))
            newlist.append(sum)
        z+=1
    return make_matrix(r1,c2,newlist)
    
def InvertMatrix(mat1):
    "convert the mat"
    height, width, arr =n(mat1),m(mat1),matrix(mat1)
    newList = []
    for i in range(width):
        for j in range(height):
            newList.append(arr[i+j*width])#culcute by formal of list matrix
    return make_matrix(width,height,newList)

#2
def data_preprocessing(data,min_val,max_val):
    "func thet help fix the list and put the averge where is not have date, of the 2 from his sides do averge"
    filter_ = list(filter(lambda x: x=='' or min_val<= x <= max_val ,(map(lambda x: int(x) if x!='' else '',data.split(',')))))
    return list(map(lambda i: int(((filter_[i - 1] + filter_[i + 1])/2)) if filter_[i] == '' else filter_[i],range(len(filter_))))


def data_preprocessing_histogram(data,min_val,max_val):
    "give back the histogram of the date"
    map_filter_averge = data_preprocessing(data,min_val,max_val)
    histogram = set()#new
    #set(map(lambda x: histogram.add((x,map_filter_averge.count(x))),map_filter_averge))
    histogram = set(map(lambda x:(x, len(tuple(filter(lambda y: x==y,map_filter_averge)))),map_filter_averge))
    return histogram

def data_preprocessing_range(data,min_val,max_val):
    "give back the averge and min and max data"
    map_filter_averge = data_preprocessing(data,min_val,max_val)
    return (min(map_filter_averge),round(reduce(lambda x,y:x+y,map_filter_averge) / len(map_filter_averge),2),max(map_filter_averge))
#3
def make_mydate(d=1,m=1,y=2017):
    "make a objrct of mydate"
    def view(msg='dmy'):
        "func to see iin difrent way the obj"
        if (msg=='mdy'):
            return'{0}/{1}/{2}'.format(m,d,y)
        elif (msg=='ymd'):
            return'{0}/{1}/{2}'.format(y,m,d)
        elif (msg=='dmy'):
            return'{0}/{1}/{2}'.format(d,m,y)
        else:
            return 'format error'
        
    def iset(date,i):
        "func to change the date"
        if (date=='day'):
            nonlocal d
            d=i
        if (date=='month'):
            nonlocal m
            m=i
        if (date=='year'):
            nonlocal y
            year=i
            
    def get(date):
        "func to get a each part of date day, month or year"
        if (date=='day'):
            return d
        if (date=='month'):
            return m
        if (date=='year'):
            return y
        
    def next_date():
        "move the date to tomarrow "
        nonlocal d,m,y
        if (m==2):
            if (d==28):
                iset('day',1)
                m+=1
            else:
                d=d+1
        if((m==1) or (m==3) or (m==5) or (m==7) or (m==8) or (m==10) or (m==12)):
            if d==31:
                iset('day',1)
                if (m==12):
                    m=1
                    y=y+1
                else:
                    m+=1
            else:
                d+=1
        if(m==4) or (m==6) or (m==9) or (m==11):
            if (d==30):
                iset('day',1)
                m+=1
            else:
                d+=1
                    
    def days_between_dates(date2):
        "minus date 1 by date 2 if they both in same year and month"
        day2=date2('get')('day')
        month2=date2('get')('month')
        year2=date2('get')('year')
        if((m==month2) and (y==year2)):
            if d>day2:
                return ('%d')%(d-day2)
            else :
                return ('%d')%(day2-d)
        else:
            return -1
                                    
    def dispach(msg):
        "the dispach who return option"
        if(msg=="view"):
            return view
        if(msg=='set'):
            return iset
        if(msg=='get'):
            return get
        if(msg=='next date'):
            next_date()
        if(msg=='days between dates'):
            return days_between_dates
    return dispach
#4
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

#5
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
            firest_one=first(contents)
            contents=rest(contents)
            return firest_one
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

