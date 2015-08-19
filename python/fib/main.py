#!/usr/bin/python
# -*- coding: <utf-8> -*-

#  Copyright 2015 Joseph M. Sleiman <www.jmsleiman.com>
#
#  Licensed under the Simplified FreeBSD License

import sys

def main(n, k):
	mature = list()
	mature.append(0)
	mature.append(1)
	mature.append(1)
	
	x = 3
	
	while(x <= n):
		mature.append(mature[x-1] + mature[x-2]*k)
		x = x + 1
	
	print mature
	
	return mature[-1]
	
if __name__ == "__main__":
	if (len(sys.argv) == 3):
		#with open (sys.argv[1], "r") as myfile:
			#data = myfile.readlines()
		print main(int(sys.argv[1]), int(sys.argv[2]))
	else:
		print "Proper usage of this module: \n main.py n k"
		 