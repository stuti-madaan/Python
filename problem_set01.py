def print_num():
    for i in range(0,6):
        return i,

def print_upto():
    n = int(raw_input("Enter a number: "))
    for i in range(0,n):
        print i+1

def print_alphabet():
    for i in range(65, 91):
        print chr(i),
    print '\n'
    for i in range(97,123):
        print chr(i),

def beesnees():
    for i in range(0,100):
        if (i+1)%3==0 and (i+1)%5==0:
            print "BEESNEES",
        elif (i+1)%3==0:
            print "Bees",
        elif (i+1)%5==0:
            print "Nees",
        else :
            print i+1,

def towercash():
    ut_tower = 9400
    dollar_bill = 0.011
    i=1
    while (ut_tower>(dollar_bill * (2**(i-1)))):
        print i, 
        print ( dollar_bill * (2**(i-1)))
        i= i+ 1
    print i
################################### Solution below for this question
       
def towercash():
    stack_height = 0.00011/2
    counter = 0
    while True:
        counter +=1
        stack_height = stack_height * 2
        print counter, "\t", stack_height
        if stack_height > 94:
            break
#############################################################

def print_square_and_cube():
    number = int(raw_input("Enter a number between 1 to 9: "))
    if number not in range(1,10):
        print "Sorry!"
        
    else:
        for i in range(1,(number+1)):
            print '%s %s %s' %(i, i**2, i**3)
           

def print_square_and_cube_loop():
    while True :
        number = int(raw_input("Enter a number between 1 to 9: "))
        if number ==0 :
            print "Stopping!"
            break
        elif number <0 or number >9 :
            print "Sorry!"
        else:
            for i in range(1,(number+1)):
                print '%s %s %s' %(i, i**2, i**3)
print_square_and_cube_loop()   
            