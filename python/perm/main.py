 #!/usr/bin/python
# -*- coding: <utf-8> -*-

#  Copyright 2014 Joseph M. Sleiman <www.jmsleiman.com>
#
#  Licensed under the Simplified FreeBSD License

import sys
from itertools import permutations

def main(n):
	array = range(1, n+1)
	list_of_permutations = list()
	for p in permutations(array):
		list_of_permutations.append(p)
	return list_of_permutations

if __name__ == "__main__":
	if (len(sys.argv) == 2):
		x = main(int(sys.argv[1]))
		
		print len(x)
		
		for entry in x:
			for num in entry:
				print num,
			print ""
		
	
	else:
		print "Try this:\n\tmain.py [int]" 

