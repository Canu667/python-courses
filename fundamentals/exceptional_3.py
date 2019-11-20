'''A module for demonstrating exceptions'''
import sys

def convert(s):
	'''Convert to an integer'''
	try:
		return int(s)
	except (ValueError, TypeError) as e:
		#we could also use pass
		print("Conversion error: {}".format(str(e)), file=sys.stderr)
		raise