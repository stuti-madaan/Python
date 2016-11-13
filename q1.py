#!/usr/bin/python

# Read session

import sys
import re
import operator
from collections import Counter

#Raw function to take out all possible combinations of phrases#
def find_phrases(X):
	ngramlist=[]
	x=len(X)
	for l in range(3, len(X)+1):
		for i in range(0,x-l+1):
			k=[]
			for j in range(0,l):
				k.append(X[i+j])
			ngramlist.append(k)
	return ngramlist

def main():
	## Read a line ##
	total_word_count=0
	word_dictionary = {} 
	distinct_words=[]
	d={}
	line_count = 0 
	for line in sys.stdin:
		
		line_count+=len(re.split(r'[^\w\s\,\'\:\;\~\@]', line)) # sentence counter (sentences separated by . ? ! and so on)
		
		line = re.sub(r'[^\w\s]','',line) # removing punctuation
			
		word_list = line.lower().strip().split() # word list from every line of the input
		
		ngrams = find_phrases(word_list)
		
		#counting frequency of phrases#
		c = Counter(str(e) for e in ngrams)
		for i in c.keys():
			if c[i]>=3:
				d[i]=c[i]
		del c
			
		#total word count#	
		total_word_count+= len(word_list)
		
		#word frequencies#
		for word in word_list:
			if word not in distinct_words:
				distinct_words.append(word)
				word_dictionary[word] =1 
			else:
				word_dictionary[word]+=1
	
	#print results#
	
	print "Total word count: " + str(total_word_count)
	print "Unique words: " + str(len(distinct_words))
	print "Sentences: " + str(line_count)
	print "Average Sentence Length: " + str(float(total_word_count/line_count))
	print "List of words in Descending frequency: "+ str(sorted(word_dictionary.items(), key=operator.itemgetter(1),reverse=True))
	
	if len(d)>0:
		print "Often used phrases: "+ str(d)

if __name__ == "__main__":
    main()
