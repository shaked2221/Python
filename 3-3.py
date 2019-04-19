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
