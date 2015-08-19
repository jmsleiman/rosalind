#!/usr/bin/python
# -*- coding: <utf-8> -*-

#  Copyright 2015 Joseph M. Sleiman <www.jmsleiman.com>
#
#  Licensed under the Simplified FreeBSD License

import sys

def score(letter):
	weightedAlphabet = {
		"A" : 71.03711,
		"C" : 103.00919,
		"D" : 115.02694,
		"E" : 129.04259,
		"F" : 147.06841,
		"G" : 57.02146,
		"H" : 137.05891,
		"I" : 113.08406,
		"K" : 128.09496,
		"L" : 113.08406,
		"M" : 131.04049,
		"N" : 114.04293,
		"P" : 97.05276,
		"Q" : 128.05858,
		"R" : 156.10111,
		"S" : 87.03203,
		"T" : 101.04768,
		"V" : 99.06841,
		"W" : 186.07931,
		"Y" : 163.06333
	}
	
	return weightedAlphabet[letter]

def main(sequence):
	return sum(map(score, sequence))
	

if __name__ == "__main__":
	if (len(sys.argv) == 2):
		
		data = ""
		with open (sys.argv[1], "r") as myfile:
			data = myfile.read().replace('\n', '')
		print main(data)
	
	else:
		print "Proper usage of this module: \n main.py [file]"