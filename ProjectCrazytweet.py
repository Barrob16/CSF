file1 = open('/Users/Robin/CSF/Project/watts.txt')
file2 = open('/Users/Robin/CSF/Project/crazyhashtag.txt')

import markovgen
import hashtaggen
import time
import random
import sys


markov = markovgen.Markov(file1)
markov2 = hashtaggen.Hashtag(file2)

for i in range(1):
	print ''
	print markov.generate_markov_text(), '#'+ markov2.generate_markov_text() 
	print ''

 
 
