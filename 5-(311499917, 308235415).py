#made by shaked astemker 311499917 and ilan yadgrov 308235415

def game():
    "the game is begin its a guss game by clues "
    from random import randint
    import random
    #------Random value and points-----
    Value = randint(100, 999)
    print("[Need to guess: ",Value," ]")
    Points=100

    #------Messages:-----
    msg1="Sum"
    msg2="Mul"
    msg3="Even digits"
    msg4="Big digits"
    msg5="Ascending order:"
    msg6="Prime digits"
    print("Welcome to game!")

    #------Functions of the game:-----
    Sum = lambda num: num%10+num//10%10+num//100%10
    Mul = lambda num: num%10*(num%100//10)*(num%1000//100)
    def Even_Digits (num):
        "print even digits by x anduneven by -"
        output=''
        if (num%1000//100)%2==0:
            output +='X'
        else:
            output +='-'
        if (num%100//10)%2==0:
            output +='X'
        else:
            output +='-'
        if (num%10)%2==0:
            output +='X'
        else:
            output +='-'

        return output

    def Big_Digits (num):
        "print the digets thet over 5 by x and oter by-"
        output=''
        if (num%1000//100)>5:
            output +='X'
        else:
            output +='-'
        if (num%100//10)>5:
            output +='X'
        else:
            output +='-'
        if (num%10)>5:
            output +='X'
        else:
            output +='-'

        return output

    def Ascending (num):
        "if the digits is ups retun true else false"
        if ((num%1000//100)<=(num%100//10)<=(num%10)):
            return True
        else:
            return False

    def Prime_Digits(num):
        "print prime digits by x and oter -"
        output=''
        a=num//100
        b=(num//10)%10
        c=num%10
        if (a == 2):
            output+='X'
        elif (a<=1):
            output+='-'
        else:
            for i in range(2,a):

                if ((a % i) == 0):
                    output+='-'
                    break
                elif(i==a-1):
                    output+='X'

        if (b == 2):
            output+='X'
        elif (b<=1):
            output+='-'
        else:
            for i in range(2,b):

                if ((b % i) == 0):
                    output+='-'
                    break
                elif(i==b-1):
                    output+='X'
        if (c == 2):
            output+='X'
        elif (c<=1):
            output+='-'
        else:
            for i in range(2,c):

                if ((c % i) == 0):
                    output+='-'
                    break
                elif(i==c-1):
                    output+='X'
        return output

    def printF1(msg,f):
        "hige order fun thet start fun"
        print(msg,": ",f)

    def printF2(msg,f):
        "hige order fun thet start fun"
        print(msg,": ",f)


    Guess=None
    Clue=None

    while (Points>0):

         Guess = int(input("enter number/Enter to finish "))
         if (Value==Guess):
             print("Yes, correct! you win ",Points," points.")
             break
         Clue=randint(1,6)
         if(Clue==1):
             printF1(msg1,Sum(Value))
         elif (Clue==2):
             printF1(msg2,Mul(Value))
         elif (Clue==3):
             printF2(msg3,Even_Digits(Value))
         elif (Clue==4):
             printF2(msg4,Big_Digits(Value))
         elif (Clue==5):
             printF1(msg5,Ascending(Value))
         elif (Clue==6):
             printF2(msg6,Prime_Digits(Value))

         Points-=10

    if(not Points):
        print("Game Over!!")

