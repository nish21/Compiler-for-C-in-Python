import sys

import preprocess
import tokenize
import lexer


if __name__ == "__main__":
	#preprocess
	preprocess.remove_comments(sys.argv[1])
	preprocess.remove_lib()

	#tokenize
	tokenize.generateTokens()