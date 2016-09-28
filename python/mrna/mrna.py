#!/usr/bin/python
# -*- coding: <utf-8> -*-

#  Copyright 2015 Joseph M. Sleiman <www.jmsleiman.com>
#
#  Licensed under the Simplified FreeBSD License

import sys

def mrna(givenString):
	rnaCodonDictionary = {
		"F" : [
			"UUU",
			"UUC"],
		"L" : [
			"CUU",
			"CUC",
			"UUA",
			"CUA",
			"UUG",
			"CUG"],
		"I" : [
			"AUU",
			"AUC",
			"AUA"],
		"V" : [
			"GUU",
			"GUC",
			"GUA",
			"GUG"],
		"M" : ["AUG"],
		"S" : [
			"UCG",
			"UCA",
			"UCU",
			"UCC",
			"AGU",
			"AGC"],
		"P" : [
			"CCU",
			"CCC",
			"CCA",
			"CCG"],
		"T" : [
			"ACU",
			"ACC",
			"ACA",
			"ACG"],
		"A" : [
			"GCU",
			"GCC",
			"GCA",
			"GCG"],
		"Y" : [
			"UAU",
			"UAC"],
		"H" : [
			"CAU",
			"CAC"],
		"N" : [
			"AAU",
			"AAC"],
		"D" : [
			"GAU",
			"GAC"],
		"STOP" : [
			"UAA",
			"UAG",
			"UGA"],
		"Q" : [
			"CAA",
			"CAG"],
		"K" : [
			"AAA",
			"AAG"],
		"E" : [
			"GAA",
			"GAG"],
		"C" : [
			"UGU",
			"UGC"],
		"R" : [
			"CGU",
			"CGC",
			"CGA",
			"AGA",
			"CGG",
			"AGG"],
		"G" : [
			"GGU",
			"GGC",
			"GGA",
			"GGG"],
		"W" : ["UGG"]
	}
		
	givenUpper = givenString.upper()
	numOfCombinations = len(rnaCodonDictionary["STOP"])
	
	for char in givenUpper:
		numOfCombinations = (numOfCombinations * len(rnaCodonDictionary.get(char, [])) ) % 1000000
	
	print numOfCombinations
	
if __name__ == "__main__":
	if (len(sys.argv) == 2):
		mrna(sys.argv[1])
	else:
		print "Proper usage of this module: \n mrna.py str"
		
