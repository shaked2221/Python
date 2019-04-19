# shaked astemker 311499917  and ilan yadgrov 308235415
#part1

inches_to_meters =lambda inches: inches*0.0254
inches_to_feets =lambda inches: inches*(1/12)
miles_to_feets =lambda miles: miles*5280
opposite =lambda z: lambda x:x/z(1)
composition =lambda firest,second:lambda result:second(firest(result))

feets_to_inches=opposite(inches_to_feets)
feets_to_miles=opposite(miles_to_feets)
feets_to_meters=composition(feets_to_inches,inches_to_meters)
meters_to_feets=composition(opposite(inches_to_meters),inches_to_feets)
meters_to_inches=opposite(inches_to_meters)
meters_to_miles=composition(meters_to_feets,feets_to_miles)
inches_to_miles=composition(inches_to_feets,opposite(miles_to_feets))
miles_to_meters=composition(miles_to_feets,feets_to_meters)
miles_to_inches=composition(miles_to_feets,feets_to_inches)


###############################################################################################
#part 2 -a

class Inches (object):
    def __init__(self, n):
        if(type(n))in (int,float):
            self.value = float(n)
        elif(type(n))is str:
            temp=n.split()
            if 'in' == temp[1] and len(temp)==2:
                try:
                    self.value =float(temp[0])
                except:
                    raise Exception ('Format error: {0}'.format(n))
            else:
                raise Exception ('Format error: {0}'.format(n))
        else:
             raise Exception ("Type error: {}".format(type(n)))
    def __repr__(self):
        return 'Inches ({})'.format(self.value)
    def __str__(self):
        return '%f in'%(self.value)


class Meters (object):
    def __init__(self, n):
        if(type(n))in (int,float):
            self.value = float(n)
        elif(type(n))is str:
            temp=n.split()
            if 'm'== temp[1] and len(temp)==2:
                try:
                    self.value =float(temp[0])
                except:
                    raise Exception ('Format error: {0}'.format(n))
            else:
                raise Exception ('Format error: {0}'.format(n))
        else:
             raise Exception ("Type error: {}".format(type(n)))
    def __repr__(self):
        return 'Meters({})'.format(self.value)
    def __str__(self):
        return '%f m'%(self.value)

###############################################################################################
#part 2 - b
### Our custom OOP
def make_class(attrs, base=None):
    """Return a new class (a dispatch dictionary) with given class attributes"""

    # Getter: class attribute (looks in this class, then base)
    def get(name):
        if name in attrs:
            return attrs[name]
        elif base:
            return base['get'](name)

    # Setter: class attribute (always sets in this class)
    def set(name, value):
        attrs[name] = value

    # Return a new initialized object instance (a dispatch dictionary)
    def new(*args):
        # instance attributes (hides encapsulating function's attrs)
        attrs = {}

        # Getter: instance attribute (looks in object, then class (binds self if callable))
        def get(name):
            if name in attrs:
                return attrs[name]
            else:
                value = cls['get'](name)
                if callable(value):
                    return lambda *args: value(obj, *args)
                else:
                    return value

        # Setter: instance attribute (always sets in object)
        def set(name, value):
            attrs[name] = value

        # instance dictionary
        obj = {'get': get, 'set': set}

        # calls constructor if present
        init = get('__init__')
        if init: init(*args)

        return obj

    # class dictionary
    cls = {'get': get, 'set': set, 'new': new}
    return cls
#############################################################################################################
#part 2 - c

def make_feets_class():
    def __init__(self, n):
        if(type(n))in (int,float):
            self['set']('value',float(n))
        elif(type(n))is str:
            temp=n.split()
            if 'ft' == temp[1] and len(temp)==2:
                try:
                    self['set']('value',float(temp[0]))
                except:
                    raise Exception ('Format error: {0}'.format(n))
            else:
                raise Exception ('Format error: {0}'.format(n))
        else:
             raise Exception ("Type error: {}".format(type(n)))
    def __repr__(self):
        return "Feets['new']({})".format(self['get']('value'))
    def __str__(self):
        return "{} ft".format(self['get']('value'))
    __type__="Feets"
    return make_class(locals())
Feets = make_feets_class()


def make_miles_class():
    def __init__(self, n):
        if(type(n))in (int,float):
            self['set']('value',float(n))
        elif(type(n))is str:
            temp=n.split()
            if 'mi' == temp[1] and len(temp)==2:
                try:
                    self['set']('value',float(temp[0]))
                except:
                    raise Exception ('Format error: {0}'.format(n))
            else:
                raise Exception ('Format error: {0}'.format(n))
        else:
             raise Exception ("Type error: {}".format(type(n)))
    def __repr__(self):
        return "Miles['new']({})".format(self['get']('value'))
    def __str__(self):
        return "{} mi".format(self['get']('value'))
    __type__="Miles"
    return make_class(locals())
Miles = make_miles_class() 

################################################################################################
def to_str(f):
    if type(f) in (Meters,Inches):
        return str(f)
    elif type(f) is dict:
        try:
            return f['get']('__str__')()
        except:
            raise Exception ("dict error: is not feet or mils dict")
    else: raise Exception ("Type error: {}".format(type(n)))

def to_repr(f):
    if type(f) in (Meters,Inches):
        return repr(f)
    elif type(f) is dict:
        try:
            return f['get']('__repr__')()
        except:
            repr(f)
    else: return f

def type_of(f):
    if type(f) in (Meters,Inches):
        return type(f)
    elif type(f) is dict:
        try:
            return f['get']("__type__")
        except:
            return type(f)
    elif type(f)==type:#slave explain it to me agein
        return f
    else: return type(f)# this is backup...?

####################################################################################
#part 3

def apply(op,value1,value2):

    add_dict =  { (Meters,Meters): lambda x,y:Meters(x.value+y.value),
                  (Meters,Inches): lambda x,y:Meters(x.value+inches_to_meters(y.value)),
                  (Inches,Meters): lambda x,y:Inches(x.value+meters_to_inches(y.value)),
                  (Inches,Inches): lambda x,y:Inches(x.value+y.value),
                  ('Feets','Feets'):lambda x,y:Feets['new'](x['get']('value')+y['get']('value')),
                  ('Feets','Miles'):lambda x,y:Feets['new'](x['get']('value')+miles_to_feets(y['get']('value'))),
                  ('Miles','Feets'):lambda x,y:Miles['new'](x['get']('value')+feets_to_miles(y['get']('value'))),
                  ('Miles','Miles'):lambda x,y:Miles['new'](x['get']('value')+(y['get']('value')))
                  }
                                                         
    sub_dict =  { (Meters,Meters): lambda x,y:Meters(x.value-y.value),
                  (Meters,Inches): lambda x,y:Meters(x.value-inches_to_meters(y.value)),
                  (Inches,Meters): lambda x,y:Inches(x.value-meters_to_inches(y.value)),
                  (Inches,Inches): lambda x,y:Inches(x.value-y.value),
                  ('Feets','Feets'):lambda x,y:Feets['new'](x['get']('value')-y['get']('value')),
                  ('Feets','Miles'):lambda x,y:Feets['new'](x['get']('value')-miles_to_feets(y['get']('value'))),
                  ('Miles','Feets'):lambda x,y:Miles['new'](x['get']('value')-feets_to_miles(y['get']('value'))),
                  ('Miles','Miles'):lambda x,y:Miles['new'](x['get']('value')-(y['get']('value')))
                  }
    
    gt_dict=    {(Meters,Meters): lambda x,y:x.value>y.value,
                 (Meters,Inches): lambda x,y:x.value>inches_to_meters(y.value),
                 (Meters,'Feets'):lambda x,y:x.value>feets_to_meters(y['get']('value')),
                 (Meters,'Miles'):lambda x,y:x.value>miles_to_meters(y['get']('value')), 
                 (Inches,Meters): lambda x,y:x.value>meters_to_inches(y.value),
                 (Inches,Inches): lambda x,y:x.value>y.value,
                 (Inches,'Feets'): lambda x,y:x.value>feets_to_inches(y['get']('value')),
                 (Inches,'Miles'): lambda x,y:x.value>miles_to_inches(y['get']('value')),
                 ('Feets','Feets'):lambda x,y:x['get']('value')>y['get']('value'),
                 ('Feets','Miles'):lambda x,y:x['get']('value')>miles_to_feets(y['get']('value')),
                 ('Feets',Inches):lambda x,y:x['get']('value')>inches_to_feets(y.value),
                 ('Feets',Meters):lambda x,y:x['get']('value')>meters_to_feets(y.value),
                 ('Miles','Feets'):lambda x,y:x['get']('value')>feets_to_miles(y['get']('value')),
                 ('Miles','Miles'):lambda x,y:x['get']('value')>(y['get']('value')),
                 ('Miles',Inches):lambda x,y:x['get']('value')>inches_to_miles(y.value),
                 ('Miles',Meters):lambda x,y:x['get']('value')>meters_to_miles(y.value)
                 }

    eq_dict={    (Meters,Meters): lambda x,y:x.value==y.value,
                 (Meters,Inches): lambda x,y:x.value==inches_to_meters(y.value),
                 (Meters,'Feets'):lambda x,y:x.value==feets_to_meters(y['get']('value')),
                 (Meters,'Miles'):lambda x,y:x.value==miles_to_meters(y['get']('value')), 
                 (Inches,Meters): lambda x,y:x.value==meters_to_inches(y.value),
                 (Inches,Inches): lambda x,y:x.value==y.value,
                 (Inches,'Feets'): lambda x,y:x.value==feets_to_inches(y['get']('value')),
                 (Inches,'Miles'): lambda x,y:x.value==miles_to_inches(y['get']('value')),
                 ('Feets','Feets'):lambda x,y:x['get']('value')==y['get']('value'),
                 ('Feets','Miles'):lambda x,y:x['get']('value')==miles_to_feets(y['get']('value')),
                 ('Feets',Inches):lambda x,y:x['get']('value')==inches_to_feets(y.value),
                 ('Feets',Meters):lambda x,y:x['get']('value')==meters_to_feets(y.value),
                 ('Miles','Feets'):lambda x,y:x['get']('value')==feets_to_miles(y['get']('value')),
                 ('Miles','Miles'):lambda x,y:x['get']('value')==(y['get']('value')),
                 ('Miles',Inches):lambda x,y:x['get']('value')==inches_to_miles(y.value),
                 ('Miles',Meters):lambda x,y:x['get']('value')==meters_to_miles(y.value)
             }

    types = (type_of(value1),type_of(value2))

    if op=='add':
        return add_dict[types](value1,value2)
    elif op=='sub':
        return sub_dict[types](value1,value2)
    elif op=='gt' or op== ">":
        return gt_dict[types](value1,value2)
    elif op=='eq' or op=='==':
        return eq_dict[types](value1,value2)



    
def coerce_apply(op,value1,value2):

    def coerce(value):
        if type_of(value)==Meters:
            return value.value
        elif type_of(value)==Inches:
            return inches_to_meters(value.value)
        elif type_of(value)=='Feets':
            return feets_to_meters(value['get']('value'))
        elif type_of(value)=='Miles':
            return miles_to_meters(value['get']('value'))

    if op == 'add' :
        return Meters(coerce(value1)+coerce(value2))
    if op == 'sub' :
        return Meters(coerce(value1)-coerce(value2))

    
##########################################################################################
class ValueExistsException (Exception):
    def __init__(self,x):
        Exception.__init__(self,"Same Value Exists: {}".format(x))

class ValueNotExistsException(Exception):
    def __init__(self,x):
        Exception.__init__(self,"Value Not Exists: {}".format(x))

class EmptyTreeException (Exception):
    def __init__(self):
        Exception.__init__(self,"The Tree Is Empty")

class TreeNode ():
    def __init__(self,value,r=None,l=None):
        self.value=value
        self.r=r
        self.l=l
        
    def insert(self,value):
        if apply("eq",value,self.value):
            raise ValueExistsException(value)
        if apply("gt",value,self.value):
            if self.r!=None:
                return self.r.insert(value)
            else:
                self.r=TreeNode(value)
                return self
        else:
            if self.l!=None:
                return self.l.insert(value)
            else:
                self.l=TreeNode(value)
                return self
    def search(self,value):
        if apply("eq",value,self.value):
            return self
        else:
            if apply("gt",value,self.value):
                if  self.r!=None:
                    return self.r.search(value)
                else:
                    raise ValueNotExistsException(value)
            else:
                if self.l!=None:
                    return self.l.search(value)
                else:
                    raise ValueNotExistsException(value)
    def height(self):
        r_higet=l_higet=-1
        if self.r!=None:
            r_higet=self.r.height()
        if self.l!=None:
            l_higet=self.l.height()
        return max(r_higet,l_higet)+1
    def in_order(self,root):
        arr=[]
        if root:
            arr = self.in_order(root.l) 
            arr.append(root.value)
            arr = arr + self.in_order(root.r)
        return arr
        '''
        if self.l!=None:
            arr=self.l.in_order()+arr
        if self.r!=None:
            arr+=self.r.in_order()
        return arr
        '''
    def __repr__(self):
        string = to_repr(self.value)
        if self.l!=None:
            string = "{}, left={}".format(string,repr(self.l))
        if self.r!=None:
            string = "{}, right={}".format(string,repr(self.r))
        return "TreeNode({})".format(string)
    def __str__(self):
        return repr(self)
    def delete(self,value):
        if apply("eq",value,self.value):
            if self.l==None and self.r==None:# no suns
                return None
            #one son
            elif self.l==None and self.r!=None:
                self.value=self.r.value
                self.l=self.r.l
                self.r=self.r.r
            elif self.r==None and self.l!=None:
                self.value=self.l.value
                self.r=self.l.r
                self.l=self.l.l 
            else:# 2 sons
                x=self
                if self.r.l!=None:
                    x=self.r
                    while x.l.l!=None:
                        x=x.l
                    self.value=x.l.value
                    x.l=x.l.r
                else:
                    self.value=x.value
                    self.r=x.r
        else:
            if apply("gt",value,self.value):
                if self.r!=None:
                    self.r=self.r.delete(value)
                else:
                    raise ValueNotExistsException(value)
            else:
                if self.l!=None:
                    self.l=self.l.delete(value)
                else:
                    raise ValueNotExistsException(value)
        return self

        
                           
class BSTree ():
    def __init__(self,root=None):
        self.root=root

    def insert(self,value):
        if type(value)in (list,tuple):
            for i in value:
                if type_of(i) in (Meters,Inches,'Feets','Miles'):
                    if self.root==None:
                        self.root=TreeNode(i)
                    else:
                        try:
                            self.root.insert(i)
                        except ValueExistsException as e:
                            print (e)
                else:
                    raise Exception ("Type error: {}".format(type(i)))
        elif type_of(value) in (Meters,Inches,'Feets','Miles'):
            if self.root==None:
                self.root=TreeNode(value)
            else:
                try:
                    self.root.insert(value)
                except ValueExistsException as e:
                    print (e)
        else:
            raise Exception ("Type error: {}".format(type(value)))#not in command of tragil
        return self.root             
        
    def search(self,value):
        try:
            if self.root!=None:
                return self.root.search(value)
            else:
                raise EmptyTreeException()
        except:
            return None
    def height(self):
        if self.root!=None:
            return self.root.height()
        else:
            raise EmptyTreeException()
    def in_order(self):
        if self.root is None:
            raise EmptyTreeException()
        return self.root.in_order(self.root)
            
    def __repr__(self):
        if self.root!=None:
            return "BSTree({})".format(repr(self.root))
        else:#check home
            return "BSTree(None)"
    def __str__(self):
        return repr(self)
    def delete (self,value):
        if self.root!=None:
            if type(value) in (list,tuple):
                for i in value:
                    if type_of(i) in (Meters,Inches,'Feets','Miles'):
                        try:
                            self.root =self.root.delete(i)
                        except:
                            print(to_str(i),"not exists")
                    else:
                        raise TypeError("not in the type {}".format(type(i)))
            else:
                if type_of(value) in (Meters,Inches,'Feets','Miles'):
                    try:
                        self.root =self.root.delete(value)
                    except:
                        print(to_str(value),"not exists")
                else:
                    raise TypeError("not in the type {}".format(type(value)))
        else:
            raise EmptyTreeException()
        


























    
