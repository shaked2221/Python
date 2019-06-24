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

