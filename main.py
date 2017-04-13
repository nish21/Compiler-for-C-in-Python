import sys

import preprocess
import parser

if __name__ == "__main__":
	# Preprocess to remove comments and library includes
	preprocess.remove_comments(sys.argv[1])
	preprocess.remove_lib()

	# Parser to check syntax
	# Lexer is internally called to generate tokens
	# getNextToken function is used by parser to get next token from lexer
	# Semantics are checked during parsing and intermediate code is generated
	# on the fly
	parser.parse()
