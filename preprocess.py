import re


def remove_comments(filename):
	"""
	Removes single line and multi line comments from the
	source program and stores the rest of the source in
	a file input.i for further processing.

	filename: path to the input source program
	"""

	string = open(filename).read()
	string = re.sub(re.compile('[^\"]\/\/.*' ) ,"" ,string)
	string = re.sub(re.compile('\/\*([^\*]|\*+[^\*\/])*\*+\/' ) ,"" ,string)
	outfile = open("input.i",'w')
	outfile.write(string)


def remove_lib():
	"""
	Removes all #include statements from the preprocessed
	source. A preprocessor would incude the code from the
	libraries but we are removing them for convenience.
	Reads from input.i and writes back to the same.
	"""

	string = open("input.i").read()
	string = re.sub(re.compile('\#.*<.*>') ,"" ,string)
	outfile = open("input.i",'w')
	outfile.write(string)
	
