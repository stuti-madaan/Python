def print_multiplication_table():
    for i in range(1,13):
        print
        for j in range(1,13):
            print '{:>4}'.format(i*j),

# def pyramid():
    # integer = int(raw_input("Enter a positive integer: "))
    # verify= raw_input("Are you Sure? (y/n): ")
    # if verify=="y":
        # for i in range(1,integer+1):
            # print '{:^7}'.format('*'),
# pyramid()
#################Actual solution :################

def pyramid():
    height = int(raw_input("\n\nPlease enter the height of the pyramid: "))
    for row in xrange(1, height+1):
        filler = ((height-row) * 3) * ' '
        sys.stdout.write(filler)
        for col in range(1, row + 1):
            sys.stdout.write('*     ')
        print


def factorial():
    num = int(raw_input("Enter a positive integer: "))
    fact=1
    for i in range(1,num+1):
        fact*=i
    print fact
##better one ##
def factorial():
    while True:
        x = int(raw_input("\n\nFACTORIAL: Please enter a positive number.  Or a negative number to stop. "))

        if x < 0:
            print "STOPPING"
            break
    
        elif x == 0:
            print 1

        else:    
            result = 1
            while x > 0:
                result = result * x
                x = x -1
            print result

            
    
def fibonacci():
    n = int(raw_input("Enter the length of series: "))
    f=0
    s=1
    t=f+s
    print 0,
    print 1,
    print t ,
    for i in range(4, n+1):
       
        f= s
        s= t
        t = f+s
        print t ,

def tip_calculator(bill_amt):
    print 'Your bill amount is $%.2f' % (bill_amt)
    print 'A 10 percent tip: $%.2f totalling $%.2f' %(bill_amt*0.1, bill_amt*1.1)
    print 'A 15 percent tip: $%.2f totalling $%.2f' %(bill_amt*0.15, bill_amt*1.15)
    print 'A 20 percent tip: $%.2f totalling $%.2f' %(bill_amt*0.2, bill_amt*1.2)
    print 'An excellent tip: $%.2f totalling $%.2f' %(bill_amt,bill_amt*2)
#tip_calculator(float(raw_input("\n\n Please enter your total bill: ")))        

def is_pythagorean(a,b,c):
    if (((a**2)+(b**2))==(c**2)):
        print "IS PYTHAGOREAN"
    else :
        print "IS NOT PYTHAGOREAN"

#is_pythagorean(2,4,5)

def print_pythagoreans_under_100():
    c_lst=[]
    a_lst=[]
    b_lst=[]
    count=0
    for a in range(1,100):
        for b in range(1,100):
            for c in range(1,100):
                if (((a**2)+(b**2))==(c**2)) and (not(a in b_lst and b in a_lst)):
                    c_lst.append(c)
                    a_lst.append(a)
                    b_lst.append(b)
                    print '%s %s %s ---->  %d + %d = %d' %(a,b,c,a**2,b**2,c**2)
                    count+=1
    print count
#print_pythagoreans_under_100()


def triangle_classifier():
    while True:
        a= int(raw_input("Enter a: "))
        b= int(raw_input("Enter b: "))
        c= int(raw_input("Enter c: "))
        if a ==0 and b==0 and c==0 :
            print "STOPPING"
            break
        elif (a<0 or b<0 or c<0):
            print "Please enter positive values"
            continue
        else :
            if (a>b+c or b>a+c or c>a+b):
                print "NO"
            elif (a<b+c and b<a+c and c<a+b):
                if (a==b and b==c and a==c):
                    print "{:>3} {:>3} {:>3} {:>3} {}".format(a, b, c, "YES", "EQUILATERAL")
                if (a==b or b==c or c==a):
                    print "{:>3} {:>3} {:>3} {:>3} {}".format(a, b, c, "YES", "ISOCELESS")
                if (a==b+c or b==a+c or c==a+b):
                    print "{:>3} {:>3} {:>3} {:>3} {}".format(a, b, c, "YES", "DEGENERATE")
                if ((((a**2)+(b**2))==(c**2)) or (((c**2)+(b**2))==(a**2)) or (((a**2)+(c**2))==(b**2))):
                    print "{:>3} {:>3} {:>3} {:>3} {}".format(a, b, c, "YES", "PYTHAGOREAN")
triangle_classifier()



