#! /usr/bin/python -tt

#Christopher Ray and Dinh Do
#Professor Blanton
#CSE 30151
#16 April 2015

#tape.py
#definition of tape class for use in a turing machine

class tape(object):
	def __init__(self):
		self.myTape = {}
		self.index = 0


	def reset_index(self):
		self.index = 0


	def reset_tape(self):
		self.myTape = {}


	def get_index(self):
		return self.index


	def move_right(self):
		self.index = self.index + 1


	def move_left(self):
		self.index = self.index - 1


	def get_item(self):
		try:
			return self.myTape[self.index]
		except:
			return ' '

	def set_item(self, x):
		self.myTape[self.index] = x
		return 0


	def checkIndex(self, x):
		try:
			l = self.myTape[x]
			return 1
		except:
			return 0
