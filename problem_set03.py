def upper(str1,str2):
    return (str1.upper(), str2.upper())

def pad(filler, repeat):
    return filler * repeat
 
def summer(number_list):
    sum=0 
    for i in number_list : 
        sum+= i
    return sum

def adder(number_list, increment):
    new_list = []
    for i in number_list:
        new_list.append(i + increment)
    return new_list

def return_dictionary(list_of_tuples):
    d = dict(list_of_tuples)
    return d
    
def return_list_items(list_of_tuples):
    new_list=[]
    for i in list_of_tuples:
        temp = list(i)
        for j in temp:
            new_list.append(j)
    return new_list        

def print_enumerated_stock_prices(stock_ticker_list, stock_price_list):
    for i,(a,b) in enumerate(zip(stock_ticker_list, stock_price_list)):
        print  '{:1} {:<5} {:>5}'.format((i+1),a,b)

import re
def highlight_word(text,highlight):
    list_words= re.split('\s|(?<!\d)[,.](?!\d)',text)
    for i in list_words: 
        if i == highlight:
            print i.upper(),
        else:
            print i,
    

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
print print_basic_stats([5])
print print_basic_stats([10,2])
print print_basic_stats([5,4,3,2,1])