 #!/usr/bin/python
# -*- coding: <utf-8> -*-

#  Copyright 2014 Joseph M. Sleiman <www.jmsleiman.com>
#
#  Licensed under the Simplified FreeBSD License

import sys
import itertools

def main(sequence):
	rnaCodonDictionary = {"UUU" : "F",
"CUU" : "L",
"AUU" : "I",
"GUU" : "V", "UUC" : "F", "CUC" : "L", "AUC" : "I", "GUC" : "V", "UUA" : "L", "CUA" : "L", "AUA" : "I", "GUA" : "V", "UUG" : "L", "CUG" : "L", "AUG" : "M", "GUG" : "V", "UCU" : "S", "CCU" : "P", "ACU" : "T", "GCU" : "A",
"UCC" : "S", "CCC" : "P" , "ACC":"T" , "GCC" : "A",
"UCA" : "S", "CCA" : "P" , "ACA":"T" , "GCA" : "A",
"UCG" : "S", "CCG" : "P" , "ACG":"T" , "GCG" : "A",
"UAU" : "Y", "CAU" : "H" , "AAU":"N" , "GAU" : "D",
"UAC" : "Y", "CAC" : "H" , "AAC":"N" , "GAC" : "D",
"UAA" : "stop", "CAA" : "Q" , "AAA":"K" , "GAA" : "E",
"UAG" : "stop", "CAG" : "Q" , "AAG":"K" , "GAG" : "E",
"UGU" : "C", "CGU" : "R" , "AGU":"S" , "GGU" : "G",
"UGC" : "C", "CGC" : "R" , "AGC":"S" , "GGC" : "G",
"UGA" : "stop", "CGA" : "R" , "AGA":"R" , "GGA" : "G",
"UGG" : "W", "CGG" : "R" , "AGG":"R" , "GGG" : "G"}
	
	groupedBases = groupByN(3, sequence) # just in case
	proteinString = ""
	
	for base in groupedBases:
		codon = "{0}{1}{2}".format(base[0],base[1],base[2])
		proteinString += rnaCodonDictionary[codon]
	
	return proteinString

def groupByN(n, listOfItems):
	arg = [iter(listOfItems)] * n
	return ([e for e in t if e != None] for t in itertools.izip_longest(*arg))

if __name__ == "__main__":
	if (len(sys.argv) == 2):
		
		data = ""
		with open (sys.argv[1], "r") as myfile:
			data = myfile.read().replace('\n', '')
		print main(data)
	
	else:
		print "Proper usage of this module: \n main.py [file]"