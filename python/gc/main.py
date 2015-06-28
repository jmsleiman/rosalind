 #!/usr/bin/python
# -*- coding: <utf-8> -*-

#  Copyright 2014 Joseph M. Sleiman <www.jmsleiman.com>
#
#  Licensed under the Simplified FreeBSD License

import sys

def main(inputFile):
	# Return: The ID of the string having the highest GC-content, followed by the GC-content of that string.
	# Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.
	
	currentTaxon = None
	currentDNA = ""
	listOfResults = []
	
	dataSource = open(inputFile).readlines()
	
	x = 0
	
	while(x < len(dataSource)):
		if(dataSource[x][0] == '>'):
			if(currentTaxon != None):
				listOfResults.append(gc(currentTaxon, currentDNA))
			currentTaxon = dataSource[x][1:]
			currentDNA = ""
		
		elif(dataSource[x][0] != '>'):
			currentDNA += dataSource[x].replace('\n', '')
		
		x = x+1
	
	listOfResults.append(gc(currentTaxon, currentDNA))
	
	return findTheHighest(listOfResults)
	
def findTheHighest(listOfResults):
	# contains the results in a format of [ ["Name", "Score (Decimal)], next, next, ...]
	topScore = -1
	topScoreLabel = ""
	
	for entry in listOfResults:
		if(entry[1] > topScore):
			topScore = entry[1]
			topScoreLabel = entry[0]
	
	return (topScoreLabel, topScore)
	
def gc(taxon, dna):
	gc = 0.0
	
	for char in dna:
		if (char == 'c' or char == 'g' or char == 'G' or char == 'C'):
			gc = gc + 1.0
	
	return [taxon, (gc / float(len(dna))) * 100]

if __name__ == "__main__":
	if (len(sys.argv) == 2):
		result = main(sys.argv[1])
		print result[0],
		print result[1]
	
	else:
		print "Proper usage of this module: \n main.py [filename]"