import random
a=dict()#main chess board
temp=dict()#temp chess board
flag=0
sn=0#to count no:of steps
def main(): 
    try:
        for i in range(1,5):
            print "Enter the column in row",i
            a[i]=int(raw_input(""))
        print_sol(4)
        queen(4)
    except ValueError:
        print "Not a number"
        return
      
def print_sol(num):
    global sn
    if sn==-1:
        print 'SOLUTION'
    elif sn==0:
        print 'INITIAL STATE'
    else:
        print 'STEP',sn
    sn+=1
    for i in range(1,num+1):
        for j in range(1,num+1):
            if(a[i]==j):
                print 'Q ',
            else:
                print '# ',
        print ''

def queen(n):
    global sn
    r=0
    f=0
    s=0
    p=0
    global flag
    while(flag!=1):
        s=0
        for i in range(1,5):
             p=a[i]
             r,f=heu(i)
             if p!=r:
                print_sol(4)
             a[i]=r
             s+=f
        if(s==0):
             flag=1
             sn=-1
             print_sol(4)
             break
def heu(i):#HEURISTIC FUNC
    s=list()
    global temp
    temp={}
    temp=dict(a)
    heutemp=dict()
    col=0
    for j in range(1,5):
        temp={}
        temp=dict(a)
        temp[i]=j
        count=total_attacks()
        heutemp[j]=count
    hvalue=int(min(heutemp.values()))#FIND LOWEST NO:OF ATTACKS
    for k in heutemp.keys():#FINDING THE COLUMN VALUE
        if(heutemp[k]==hvalue):
            s.append(k)
    col=random.choice(s)
    return col,hvalue

def total_attacks():#TO CHECK THE NO:OF ATTACKS IN THE CHESS BOARD
    global temp
    count=0
    for pos in range(1,5):
        for i in range(1,5):#UP-DOWN CHECKING
            if i!=pos:
                if(temp[i]==temp[pos]):
                    count+=1
        for i in range(1,5):#DIAGONAL CHECKING
            if i<pos:
                if(temp[i]==(temp[pos]-abs(i-pos))):
                    count+=1
            if i>pos:
                if(temp[i]==(temp[pos]+abs(i-pos))):
                    count+=1
        for i in range(1,5):#DIAGONAL CHECKING
            if i<pos:
                if(temp[i]==(temp[pos]+abs(i-pos))):
                    count+=1
            if i>pos:
                if(temp[i]==(temp[pos]-abs(i-pos))):
                    count+=1
    return count/2

main()