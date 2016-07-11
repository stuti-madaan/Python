def countdown(n):
    if n<= 0 :
        print "Tskeoff!"
    else:
        print n 
        countdown(n-1)
        print n*10

def visualize(num):
    sum=0
    if num <= 0 :
        return 0
    else: 
        recurse=visualize(num-1)
        sum= recurse+num
    return sum
    

def factorial(num):
    if num<0 : 
        print "Invalid number"
    elif num==0 or num ==1  :
        return 1
    else:
        fact= num*factorial(num-1)
        return fact

def write_file(msg):
    my_file = open("sample.txt","w")
    my_file.write(msg)
    my_file.close()

#message=raw_input("Enter a message: ")
#write_file(message)

def read_write(file_to_read,file_to_write):
    my_file=open(file_to_read,"r")
    out_file = open(file_to_write,"w")
    line = my_file.readlines()
    for i in line :
        out_file.write(i)
    my_file.close()
    out_file.close()
#read_write("in.txt","out.txt")

l= ['the', 'cat', 'sat', 'on', 'the', 'wall', 'and', 'the', 'cat', 'sat', 'on', 'the', 'mat',  'where','the','rat','usually','sat','and','the','cat','sat','on','the','rat'] 
def wordcount(lst):
    d={}
    for i in lst:
        d[i]= len(i)
    return sorted(d.items(),key=lambda x:x[1],reverse=True)
    
#print wordcount(l)

def indexer(lst):
    while(1):
        print lst
        indexing=[]
        word = raw_input("Choose a word for indexing: ")
        if word.lower()=="stop":
            exit()
        else:
            for i in range(0,len(lst)):
                if lst[i]== word.lower() :
                    indexing.append(i+1)
            print indexing
        

#indexer(l)

def cipher():
    actual ='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    coded ='GnWkmEJIRQsHLzPSdqVoxfrZbTyOBXhNiwCDcupUYMKgAjlavtFe'
    while(1):
        outstring=[]
        msg = raw_input("Enter the message: ")
        if msg.lower()=='x':
            exit()
        elif msg[0]!='1':
            for i in msg:
                for j in range(0,len(actual)):
                    if i==actual[j]:
                        outstring.append(coded[j])
        elif msg[0]=='1':
            for i in range(1,len(msg)):
                for j in range(0,len(coded)):
                    if msg[i]==coded[j]:
                        outstring.append(actual[j])
        print ''.join(outstring)
#cipher()
###################################

def print_basic_stats(number_list):
    d={}
    number_list.sort()
    error_dict={'error': 'List should contain more than one number.'}
    if len(number_list)<2:
        print error_dict
    else :
    ## Min:
        min= number_list[0]
        for i in number_list:
            if i <min:
                min=i
        d['min']= min
    
    ## Max: 
        max=number_list[0]
        for i in number_list:
           if i>max:
                max=i
        d['max']= max
    
    ## Median:
        if len(number_list)%2!=0:
            median = number_list[(len(number_list)-1)/2]
        else:
            median = (number_list[(len(number_list))/2  -1]+number_list[(len(number_list))/2])/2
        d['median']= round(float(median),1)
    
    ## Range:
        range= max-min
        d['range']= range
    
    ## Total:
        total=0
        for i in number_list:
            total+=i
        d['total']= total
    
    ## Mean:
        mean = total/len(number_list)
        d['mean']= round(float(mean),1)
    
    return d
#########################################################

def analyze(data_file,results_file):
    in_file=open(data_file,"r")
    out_file=open(results_file,"w")
    lines = in_file.readlines()
    for j in lines:
        num= j.split(',')
        new_list=[]
        for i in range(0,len(num)):
            new_list.append(int(num[i]))
        output= str(print_basic_stats(new_list))
        out_file.write(output + '\n')
    in_file.close()
    out_file.close()
    return 0

#analyze("001.txt","001_stats.txt")
#analyze("002.txt","002_stats.txt")


from random import randint
def hangman():
    list = ["hello","kitty","horse","abnormal"]
    index= randint(0,len(list)-1)
    word = list[index]
    guessed_word =  '-' * len(word)
    print guessed_word
    guesses = len(word) +3
    for i in range(1,guesses+1):
        if i <= guesses and guessed_word==word :
            print "You have correctly guessed the word"
            exit()
        elif i <= guesses and guessed_word!=word:
            letter= raw_input("Guess the letter: ")
            for j in range(0,len(word)):
                if letter==word[j] and guessed_word[j]=='-':
                    guessed_word = guessed_word[:j] + letter + guessed_word[j + 1:]
                    print guessed_word
                elif j==len(word)-1 :
                    print "Letter does not exist"
                    print guessed_word
    if guessed_word!=word:
        print "You are out of guesses"
#hangman()


def palindrome():
    input = raw_input("Enter a string: ")
    l= len(input)
    c=0
    for i in range(0,l):
        if input[i]== input[l-1-i]:
            c+=1
            if c==l :
                print "Yes!It is a palindrome"
        elif i==l-1 and c!=l:
            print "Not a palindrome"
            
#palindrome()




###########      CHEATED      ############

def odometer():
    #            012345 
    #condition1 :**yzzy
    #condition2 :**yzzy+1 = *abcba
    #condition3 :**yzzy+2 = *abcba+1 = *deed*
    #condition4 :**yzzy+3 = *abcba+2 = *deed*+1 = fghhgf
    for i in range(100000,1000000):
        if str(i)[2:]== str(i)[:1:-1]: 
            i+=1
            if str(i)[1:]==str(i)[5:0:-1]:
                i+=1
                if str(i)[1:5:]==str(i)[-2:0:-1]:# -2 means characters from second last
                    i+=1
                    if str(i)==str(i)[::-1]:
                        print i-3
                        
odometer()
    