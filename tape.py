#! /usr/bin/python -tt

#Christopher Ray and Dinh Do
#Professor Blanton
#CSE 30151
#16 April 2015

#tape.py
#definition of tape class for use in a turing machine

class tape(object):	#defining tape class
	def __init__(self):	#defining init function
		self.myTape = {}	#tape is basically a dictionary
		self.index = 0	

	def reset_index(self):	#defining reset functions
		self.index = 0

	def reset_tape(self):
		self.myTape = {}

	def get_index(self):	#function that returns the current index
		return self.index

	def move_right(self):	#function for moving the tape head right
		self.index = self.index + 1

	def move_left(self):	#function for moving the tape head left
		self.index = self.index - 1

	def get_item(self):	#function for returning at item from the current tape head location
		try:
			return self.myTape[self.index]
		except:
			return ' '	#return ' ' if there is nothing at this location

	def set_item(self, x):	#function for setting an item at the current tape head location
		self.myTape[self.index] = x
		return 0

	def checkIndex(self, x):	#function for checking if index is valid (prevents key errors)
		try:
			l = self.myTape[x]
			return 1
		except:
			return 0
