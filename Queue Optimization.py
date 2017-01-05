
import sys
from collections import defaultdict

## Read Input##
inputstring= str(sys.stdin.read()).split('\n')
price={}
people=[]

## Separate different components of input ##
for i in inputstring:
    l = i.split(" ")
    if len(l)==3:
        num_people=int(l[0])
        num_windows=int(l[1])
        num_dest=int(l[2])
    elif len(l)==2:
        price[l[0]]=float(l[1])
    elif len(l)==1:
        people.extend(l)

## update last price of a window##
last_price=[0.0]*num_windows
window=[0]*num_people
last_dest=[None]*num_windows

for i in range(0,len(people),1):
    print i 
    people[i]
    print last_dest
    if i==0:
        window[i]=0
    elif i>0:
        if (people[i] in last_dest):
            print "true1"
            window[i]= [i for i, j in enumerate(last_dest) if j == people[i]][0]
            print window[i]
        elif (people[i] not in last_dest and len(set(window)) < num_windows):
            print "true2"
            window[i]=len(set(window))
            print window[i]
        elif people[i] not in last_dest and len(set(window))==num_windows:
            for j in range(len(last_price)):
                if last_price[j]== min(last_price):
                    window[i]= j               
    k=int(window[i])
    last_price[k]= price[people[i]]
    last_dest[k] = people[i]
     
    
for i in range(len(window)):
    window[i]=window[i]+1


def calc_price(window): 
    '''list of people's destinations(maintained order) going to the window'''
    new_p=[]
    for i in range(0,len(window)): 
        if i>0:
            if window[i]==window[i-1]:
                new_p.append(float(price[window[i]])*0.8)
            else:
                new_p.append(float(price[window[i]]))                    
        else:
            new_p.append(float(price[window[i]]))
    return sum(new_p)


new_dict=defaultdict(list)
for i in range(len(people)):
    if window[i] in new_dict:
        new_dict[window[i]].append(people[i])
    else:
        new_dict[window[i]]= [people[i]]

tot_price=0.0
for i in new_dict:
    tot_price+=calc_price(new_dict[i])
    
sys.stdout.write(str(tot_price)+"\n")
for i in range(len(people)):
    sys.stdout.write(str(window[i])+"\n")
   
