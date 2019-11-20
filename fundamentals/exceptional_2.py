'''A module for demonstrating exceptions'''
import sys

def convert(s):
	'''Convert to an integer'''
	try:
		x = int(s)
	except (ValueError, TypeError) as e:
		#we could also use pass
		print("Conversion error: {}".format(str(e)), file=sys.stderr)
		return -1