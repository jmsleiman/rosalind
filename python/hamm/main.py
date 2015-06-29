#!/usr/bin/python
# -*- coding: <utf-8> -*-

#  Copyright 2015 Joseph M. Sleiman <www.jmsleiman.com>
#
#  Licensed under the Simplified FreeBSD License

import sys

def main(sequenceOne, sequenceTwo):
	x = 0
	hammingDistance = 0
	
	while(x < len(sequenceOne)):
		if(sequenceOne[x] != sequenceTwo[x]):
			hammingDistance += 1
		x = x+1
	
	return hammingDistance

if __name__ == "__main__":
	if (len(sys.argv) == 2):
		
		str1 = ""
		str2 = ""
		with open (sys.argv[1], "r") as myfile:
			data = myfile.readlines()
			str1 = data[0][:-1]
			str2 = data[1][:-1]
		if(len(str1) != len(str2)):
			raise ValueError("You'll need to provide two strings of identical length")
		else:
			print main(str1, str2)
	
	else:
		print "Proper usage of this module: \n main.py [file]"
		 