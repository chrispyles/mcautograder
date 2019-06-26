###############################################
##### Multiple Choice Question Autograder #####
###############################################

import string
import re

def repeat(x, n):
	"""
	Returns a list of a given value repeated a given number of times

	Args:
		x - value to repeat
		n - number of repetitions
	"""
	return [x for _ in range(n)]

class Notebook:
	"""Multiple choice question autograder for Jupyter Notebook"""

	def __init__(self, tests, scored=False, max_retakes="inf"):
		"""
		Initlaizes multiple choice autograder.

		Args:
			tests       - relative filepath to tests file
			scored      - whether or not the assignment is scored; default `False`
			max_retakes - if `"inf"`, no maximum retakes; maximum number of retakes
						  allowed; deault `"inf"`
		"""
		with open(tests) as tests_file:
			self._tests = tests_file.readlines()
		if self._tests[-1][-1] != "\n":
			self._tests[-1] += "\n"
		self._questions = [q[:-5] for q in self._tests]

		self._inf_retakes = True
		self._scored = scored

		if self._scored:
			point_by_question = [int(q.split(" ")[2][:-1]) for q in self._tests]
			self._points = {q:p for q, p in zip(self._questions, point_by_question)}
			self._answered = {q:f for q, f in zip(self._questions, repeat(False, len(self._questions)))}
			self._possible = sum(self._points.values())
			self._earned = 0

		if max_retakes != "inf":
			assert max_retakes > 0 and type(max_retakes) == int, "max_retakes must be a positive integer"
			self._inf_retakes = False
			self._retakes = {q:r for q, r in zip(self._questions, repeat(0, len(self._questions)))}
			self._max_retakes = max_retakes

	def _check_answer(self, q_name, answer):
		"""
		Checks whether or not answer is correct; returns boolean

		Args:
			q_name - question identifier
			answer - student answer
		"""
		assert q_name in self._questions, "{} is not in the question bank".format(q_name)
		assert type(answer) in [str, int], "Answer must be a string or integer"
		if type(answer) == str:
			assert len(answer) == 1, "Answer must be of length 1"
		else:
			assert 0 <= answer < 10, "Answer must be a single digit"
		if not self._inf_retakes:
			assert self._retakes[q_name] < self._max_retakes, "No more retakes allowed."

		for test in self._tests:
			if q_name in test[:-4]:
				if test[-4] in string.digits:
					if answer == int(test[-4]):
						if self._scored and not self._answered[q_name]:
							self._answered[q_name] = True
							self._earned += self._points[q_name]
						if not self._inf_retakes:
							self._retakes[q_name] += 1
						return True
				elif answer == test[-4]:
					if self._scored and not self._answered[q_name]:
						self._answered[q_name] = True
						self._earned += self._points[q_name]
					if not self._inf_retakes:
						self._retakes[q_name] += 1
					return True
		return False

	def check(self, q_name, answer):
		"""
		Visible wrapper for _check_answer to print output based on whether or not student's
		answer is correct

		Args:
			q_name - question identifier
			answer - student's answer
		"""
		result = self._check_answer(q_name, answer)
		if self._scored:
			if result:
				print("Correct. {} points added to your score.".format(self._points[q_name]))
			else:
				print("Try again.")
		else:
			if result:
				print("Correct.")
			else:
				print("Try again.")

	def score(self):
		"""
		If assignment is scored, displays student's score as fraction and percentage.

		Args:
			None
		"""
		if self._scored:
			print("{}/{}: {:.3f}%".format(self._earned, self._possible, self._earned/self._possible*100))
		else:
			print("This notebook is not scored.")