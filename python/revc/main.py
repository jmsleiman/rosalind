 #!/usr/bin/python
# -*- coding: <utf-8> -*-

#  Copyright 2014 Joseph M. Sleiman <www.jmsleiman.com>
#
#  Licensed under the Simplified FreeBSD License

import sys

def main(inputString):
	newString = ""
	
	for letter in reversed(inputString):
		if(letter == 'A'):
			newString = newString + 'T'
		elif(letter == 'C'):
			newString = newString + 'G'
		elif(letter == 'G'):
			newString = newString + 'C'
		elif(letter == 'T'):
			newString = newString + 'A'
		elif(letter == 'a'):
			newString = newString + 't'
		elif(letter == 'c'):
			newString = newString + 'g'
		elif(letter == 'g'):
			newString = newString + 'c'
		elif(letter == 't'):
			newString = newString + 'a'
		else:
			raise RuntimeWarning("This is not a valid DNA sequence. Character: %s is not a valid DNA nucleotide." % character)
	
	print newString
	return newString
	
if __name__ == "__main__":
	if (len(sys.argv) == 2):
		main(sys.argv[1])
	
	else:
		print "Proper usage of this module: \n main.py [string]"