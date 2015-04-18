#! /usr/bin/python -tt

#Christopher Ray and Dinh Do
#Professor Blanton 
#CSE 30151
#13 April 2015

#main.py
#main driver program for Turing machine simulator

import sys, re



def main():
	Q = []
	A = []
	Z = []
	T = {}
	S = None
	F = [None] * 2

	args = sys.argv
	if len(args) != 2:
		print "Must pass in file with machine description."
		return
	
	f = open(args[1], 'r')
	
	for line in f:
		i = 1
		r = '[,:\n]'
		line = re.split(r, line)

		# Fill States
		if line[0] == 'Q':
			while i < len(line) - 1:
				Q.append(line[i])
				i+=1	
		# Fill Alphabet			
		elif line[0] == 'A':
			while i < len(line) - 1:
				A.append(line[i])
				i+=1
		# Fill Tape Alphabet	
		elif line[0] == 'Z':
			while i < len(line) - 1: 
				Z.append(line[i])
				i+=1
	
		# Fill Transitions in dictionary
		# Key = start state & value = current tape symbol, resulting state, symbol written on tape, and direction
		elif line[0] == 'T':
			T[line[1]] = [line[2],line[3],line[4], line[5]]

		# Set Start State
		elif line[0] == 'S':
			S = line[1]
		
		# Set Result states. F[0] = accept. F[1] = reject
		elif line[0] == 'F':
			F[0] = line[1]
			F[1] = line[2]


		
	# Machine Checks
	
				

		
		


if __name__ == '__main__':
	main()
