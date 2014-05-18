 #!/usr/bin/python
# -*- coding: <utf-8> -*-

#  Copyright 2014 Joseph M. Sleiman <www.jmsleiman.com>
#
#  Licensed under the Simplified FreeBSD License

import sys

def main(inputString):
	newString = inputString.replace('T', 'U').replace('t', 'u')
	
	print newString
	return newString
	
if __name__ == "__main__":
	if (len(sys.argv) == 2):
		main(sys.argv[1])
	
	else:
		print "Proper usage of this module: \n main.py [string]"