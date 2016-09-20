#!/usr/bin/env python

import argparse
import sys
import string

def to_piglatin(word):
	vowels = ['a','e','i','o','u']
	if word[0] in vowels:
		return "{}{}".format(word,"ay")
	else:
		if word[1] in vowels:
			return "{}{}{}".format(word[1:],word[0],"ay")
		else:
			if word[2] in vowels:
				return "{}{}{}".format(word[2:],word[0:2],"ay")
			else:
				if word[3] in vowels:
					return "{}{}{}".format(word[3:],word[0:3],"ay")


parser = argparse.ArgumentParser()
parser.add_argument("-if", "--inputfile", type=str, help="Define an input file")
parser.add_argument("-of", "--outputfile", type=str, help="Define an output file")
args = parser.parse_args()

f = open(args.inputfile)
f1 = open(args.outputfile, "w")
for line in f:
	for c in string.punctuation:
		line = line.replace(c,"")
	words = line.split( )
	x = []
	for word in words:
		x.append(to_piglatin(word))
	s = ' '.join(x)
	s = s + "\n"	
	f1.write(s)

f.close()
f1.close()

