###############################################
##### Multiple Choice Question Autograder #####
###############################################

import string
import re

class Notebook:
	def __init__(self, tests):
		"""
		Initlaizes multiple choice autograder. Tests should be saved in a
		hidden text file (by appending a period to the filename). The format
		for the tests should be "q_name answer", e.g.:

			q1_1 1
			q1_2 2
			q1_3 2
			q2_1 4
			q2_2 3
			q3_1 A
			q3_2 D
			q3_3 B
			
		"""
		with open(tests) as tests_file:
			self._tests = tests_file.readlines()
		if self._tests[-1][-1] != "\n":
			self._tests[-1] += "\n"
		self._questions = [q[:-3] for q in self._tests]

	def _check_answer(self, q_name, answer):
		assert q_name in self._questions, "{} is not in the question bank".format(q_name)
		assert type(answer) in [str, int], "Answer must be a string or integer"
		if type(answer) == str:
			assert len(answer) == 1, "Answer must be of length 1"
		else:
			assert 0 <= answer < 10, "Answer must be a single digit"

		for test in self._tests:
			if q_name in test[:-2]:
				if test[-2] in string.digits:
					if answer == int(test[-2]):
						return True
				elif answer == test[-2]:
					return True
		return False

	def check(self, q_name, answer):
		if self._check_answer(q_name, answer):
			print("Correct.")
		else:
			print("Try again.")