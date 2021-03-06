#! /usr/bin/python -tt

#Christopher Ray and Dinh Do
#Professor Blanton 
#CSE 30151
#13 April 2015

#main.py
#main driver program for Turing machine simulator

import sys, re
from tape import tape

# Print output function
def printoutput(t, cs):
	sys.stdout.write('(')
	
	if t.index < len(t.myTape):	#determining where the tape head is
		T = t.index
	else:
		T = len(t.myTape)

	for i in range (0,T):	#printing out tape contents up to where the tape head is

		sys.stdout.write( t.myTape[i] )
		
		if i < (t.index - 1):
			sys.stdout.write(",")

	print ')' + str(cs) + '(',	#displaying current state

	for i in range (t.index, len(t.myTape)):	#printing the rest of the tape input

		if t.index < len(t.myTape):
			if t.checkIndex(i):	
				sys.stdout.write( t.myTape[i] )
			
				if i < (len(t.myTape) - 1):
					sys.stdout.write(",")
		
	sys.stdout.write( ')\n' )
	sys.stdout.flush()

	return


#main function
def main(tape):	
	# Data structures
	Q = []		# States
	A = []		# Alphabet
	Z = []		# Tape alphabet
	T = {}		# Transitions
	S = None	# Start state
	F = [None] * 2	# F[0] = Accept state, F[1] = Reject state
	transitions = 0	#recordinng the number of transitions to determine if machine halts
	

	args = sys.argv
	if len(args) != 2:	#making sure there is an input file
		print "Must pass in file with machine description."
		return
	
	try:
		f = open(args[1], 'r')	#attempting to open input file
	except:
		print "Error opening file"	#end program if there was an error opening the input file
		return 
	
	for line in f:	#parse through the input file and build the TM
		i = 1
		r = '[,:\n]'	#tokenize the line
		line = re.split(r, line)

		# Fill States Array
		if line[0] == 'Q':
			while i < len(line) - 1:
				Q.append(line[i])
				i+=1	

		# Fill Alphabet	Array		
		elif line[0] == 'A':
			while i < len(line) - 1:
				if line[i] == ' ':
					print "Blank character is not allowed to be in input alphabet."
					return
				A.append(line[i])
				i+=1

		# Fill Tape Alphabet Array	
		elif line[0] == 'Z':
			while i < len(line) - 1: 
				Z.append(line[i])
				i+=1
	
		# Fill Transitions dictionary
		# Key = start state
		# value[0] = current tape symbol 
		# value[1] = resulting state
		# value[2] = symbol to be written on tape
		# value[3] = direction
		elif line[0] == 'T':
			if line[1] not in Q or line[3] not in Q:	#check for invalid states
				print "State in transition is not a valid state in machine."
				return
			if line[2] not in Z or line[4]not in Z:	#check for invalid characters
				print "Tape symbol is not valid in this machine."
				return
			if line[5] != 'L' and line[5] != 'R':	#check for invalid directions
				print str(line[5]) + " direction is not valid."
				return
			try:	
				T[line[1]].append((line[2],line[3],line[4],line[5]))	#add another transition to a state already in the dictionary
			except: 
				T[line[1]] = []	#add a completely new transition to the dictionary
				T[line[1]].append((line[2],line[3],line[4],line[5]))

		# Set Start State
		elif line[0] == 'S':
			if line[1] not in Q:
				print str(line[1]) + " is not a valid state in machine."
				return
			S = line[1]
		
		# Set Result states. F[0] = accept. F[1] = reject
		elif line[0] == 'F':
			if line[1] not in Q or line[2] not in Q:
				print "Final state is not a valid state in machine."
				return
			F[0] = line[1]
			F[1] = line[2]

	if ' ' not in Z:	#adding blank input to tape input alphabet
		Z.append(' ')

	# Check if deterministic
	for i in T.keys():	#loop through each starting state for each transition and see if the same tape input sends you to more than 1 state
		for j in range (0, len(T[i])-1):
			for k in range (1, len(T[i]) - j):
				if T[i][j][0] == T[i][j+k][0]:
					print "Machine is not deterministic"
					return


	# Getting number of lines user will input next
	try:
		nlines = raw_input()
		nlines = int(nlines)
	except ValueError:
		print "Input needs to be an integer"
		return

	# Processing Tape Input
	for i in range (0, nlines):	#going through the user inputs
		transitions = 0	#initializing number of transitions to 0
		tape.__init__()	#initializing tape
		currentstate = S	#setting current state
		l = raw_input()	#getting tape input
		line = l.split(',')	#tokenizing tape input
		j = 0
		for i in line:	#filling tape with the user's input	
			tape.myTape[j] = i
			j += 1
		
		#displaying initial state of the simulator
		print '\n()',
		sys.stdout.write( str(currentstate) + '(')
		for i in range (tape.index, len(tape.myTape)):
			sys.stdout.write( tape.myTape[i])
			if i < (len(tape.myTape) - 1):
				sys.stdout.write(',')
		sys.stdout.write(')\n')
		sys.stdout.flush()
		
		# Going through the transitions
		j = 0
		while j < len(T[currentstate]):	#go through the transitions for the current state
			if tape.index > len(line) - 1:	#at the end of the input
				if T[currentstate][j][0] == tape.get_item():	#checking if current tape input matches that of the transition
					tape.set_item(T[currentstate][j][2])	#writing to the current tape position

					transitions += 1	#incrementing the number of transitions
				
					if T[currentstate][j][3] == 'R':	#moving the tape head
						tape.move_right()
					else:
						tape.move_left()

					currentstate = T[currentstate][j][1]	#updating the current state
					printoutput(tape, currentstate)	#printing output
					j = 0	#reset j since we are now working with a new current state
			
					if ((currentstate == F[0]) or (currentstate == F[1])):	
						break 

					continue
			elif (tape.get_item()==None)or(T[currentstate][j][0] == tape.get_item()):#still going through the input
				
				transitions += 1
				
				#if T[currentstate][j][2] != ' ':
				tape.set_item(T[currentstate][j][2])
				

				if T[currentstate][j][3] == 'R':
					tape.move_right()
				else:
					tape.move_left()

					
				currentstate = T[currentstate][j][1]
				printoutput(tape, currentstate)
				j = 0
			
				#if currentstate == F[0]:
				if ((currentstate == F[0]) or (currentstate == F[1])):	
					break 
		
				continue

			if transitions > 1000:	#stop the simulation if this limit is reached
				break

			j += 1

		# Check if in accept or reject states or if not halting
		if transitions > 1000:
			print 'DOES NOT HALT'
		elif currentstate == F[0]:
			print "ACCEPT"
		else:
			tape.move_right()
			printoutput(tape, F[1])
			print "REJECT"
		
		print "\n"
	
	f.close()	#closing input file	
	return

		
if __name__ == '__main__':
	tape = tape()
	main(tape)
