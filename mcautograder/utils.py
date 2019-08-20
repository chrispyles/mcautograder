##############################################
##### Utilities for mcautograder library #####
##############################################

import pickle

def repeat(x, n):
	"""
	Returns a list of a given value repeated a given number of times

	Args:
		x (any): The value to repeat
		n (`int`): The number of repetitions

	Returns:
		`list`. List of repeated values `x`
	"""
	return [x for _ in range(n)]

def serialize(obj, file):
	"""
	Serializes OBJ and writes contents to FILE
	"""
	pickle.dump(obj, file, protocol=pickle.HIGHEST_PROTOCOL)