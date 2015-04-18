#! /usr/bin/python -tt

#Christopher Ray and Dinh Do
#Professor Blanton 
#CSE 30151
#13 April 2015

#main.py
#main driver program for Turing machine simulator

import sys, re
from tape import tape


# Print output
def printoutput(t, cs):
	print '(',
	
	for i in range (0,t.index):
		print t.myTape[i],
	print ')' + str(cs) + '(',
	for i in range (t.index + 1, len(t.myTape)):
		print t.myTape[i] + ','
	print ')'

	return


def main(tape):
	Q = []
	A = []
	Z = []
	T = {}
	S = None
	F = [None] * 2
	transitions = 0

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
				if line[i] == ' ':
					print "Blank character is not allowed to be in input alphabet."
					return
				A.append(line[i])
				i+=1
		# Fill Tape Alphabet	
		elif line[0] == 'Z':
			while i < len(line) - 1: 
				Z.append(line[i])
				i+=1
	
		# Fill Transitions in dictionary
		# Key = start state
		# value[0] = current tape symbol 
		# value[1] = resulting state
		# value[2] = symbol written on tape
		# value[3] = direction
		elif line[0] == 'T':
			if line[1] not in Q or line[3] not in Q:
				print "State in transition is not a valid state in machine."
				return
			if line[2] not in Z or line[4]not in Z:
				print "Tape symbol is not valid in this machine."
				return
			if line[5] != 'L' and line[5] != 'R':
				print str(line[5]) + " direction is not valid."
				return
			try:	
				T[line[1]].append((line[2],line[3],line[4],line[5]))
			except: 
				T[line[1]] = []
				T[line[1]].append((line[2],line[3],line[4],line[5]))

		# Set Start State
		elif line[0] == 'S':
			if line[1] not in Q:
				print str(line[1]) + " start state is not a valid state in machine."
				return
			S = line[1]
		
		# Set Result states. F[0] = accept. F[1] = reject
		elif line[0] == 'F':
			if line[1] not in Q or line[2] not in Q:
				print "Final state is not a valid state in machine."
				return
			F[0] = line[1]
			F[1] = line[2]


	if ' ' not in Z:
		Z.append(' ')


	# Number of lines user will input next
	nlines = input()

	# Process Tape Input
	for i in range (0, nlines):
		currentstate = S
		l = raw_input()
		line = l.split(',')
		for i in line:	
			tape.myTape.append(i)


		# INCOMPLETE / DOESNT WORK CORRECTLY YET
		while j < len(T[currentstate]):
			print T[currentstate][j]
			if T[currentstate][j][0] == tape.get_item:
				print T[currentstate][j][0]
				transitions += 1
				if T[currentstate][j][2] != ' ':
					tape.set_item(T[currentstate][j][2])
	
					currentstate = T[currentstate][j][1]

					if T[currentstate][j][3] == 'R':
						tape.move_right()
					else:
						tape.move_left()

					j = 0
		
					printoutput(tape, currentstate)

					continue 

				if transitions > 1000:
					break

			j += 1

				

		if transitions > 1000:
			print 'NOT HALT'

		elif currentstate == F[0]:
			print "ACCEPT"
		else:
			print "REJECT"
		
		
	return

		
		


if __name__ == '__main__':
	tape = tape()
	main(tape)
