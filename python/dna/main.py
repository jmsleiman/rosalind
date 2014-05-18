 #!/usr/bin/python
# -*- coding: <utf-8> -*-

#  Copyright 2014 Joseph M. Sleiman <www.jmsleiman.com>
#
#  Licensed under the Simplified FreeBSD License

import sys

def main(inputString):
	a = 0;
	c = 0;
	g = 0;
	t = 0;
	
	for character in inputString:
		if(character == 'a' or character == 'A'):
			a = a + 1;
		
		elif(character == 'c' or character == 'C'):
			c = c + 1;
		
		elif(character == 'g' or character == 'G'):
			g = g + 1;
		
		elif(character == 't' or character == 'T'):
			t = t + 1;
		
		else:
			raise RuntimeWarning("This is not a valid DNA sequence. Character: %s is not a valid DNA nucleotide." % character)
	
	print "%s %s %s %s" % (a, c, g, t)
	return (a, c, g, t)
	
if __name__ == "__main__":
	if (len(sys.argv) == 2):
		main(sys.argv[1])
	
	else:
		print "Proper usage of this module: \n main.py [string]"