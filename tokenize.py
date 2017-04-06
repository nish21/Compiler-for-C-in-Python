import token
import automata
import symbolTable

def generateTokens():
	others = "; \t\n"
	"""
	A function that reads the file input.i character by character
	and determines lexemes. It then creates tokens in the format
	<type, id> where type specifies the type of token and id
	determines the lexeme.
	"""
	symtab = symbolTable.symbolTable()
	filename = "input.i"
	file = open(filename).read();
	#file = "int me=10; "
	first = 0
	forward = 0
	while first < len(file):
		#print(first)
		forward = first
		currentChar = file[forward]
		if currentChar in "({)},;":
			tok = token.Token(currentChar, "Special")
			tok.printToken()
			symtab.insert(tok)
			#yield tok
			first += 1

		elif currentChar in " \n\t":
			first += 1
		else:
			for i in automata.keywords:
				#print("keyword")
				table = i()
				currentState = 0
				while currentState < len(table)-1:
					currentState = table[currentState][ord(currentChar)]
					if currentState == -1:
						forward = first
						break
					elif currentState == len(table)-1:
						tok = token.Token(file[first:forward],"Keyword")
						tok.printToken()
						symtab.insert(tok)
						#yield tok
						first = forward
					else:
						forward += 1
						currentChar = file[forward]

			for i in automata.data_types:
				table = i()
				#print("data_types")
				currentState = 0

				while currentState < len(table)-1:
					currentState = table[currentState][ord(currentChar)]
					if currentState == -1:
						forward = first
						break
					elif currentState == len(table)-1:
						tok = token.Token(file[first:forward],"Keyword")
						tok.printToken()
						symtab.insert(tok)
						#yield tok
						first = forward
					else:
						forward += 1
						currentChar = file[forward]

			for i in automata.ids:
				#print("id")
				table = i()
				currentState = 0

				while currentState < len(table)-1:
					currentState = table[currentState][ord(currentChar)]
					if currentState == -1:
						forward = first
						break
					elif currentState == len(table)-1:
						tok = token.Token(file[first:forward],"ID")
						tok.printToken()
						symtab.insert(tok)
						#yield tok
						first = forward
					else:
						forward += 1
						currentChar = file[forward]

			for i in automata.ops:
				table = i()
				currentState = 0
				while currentState < len(table)-1:
					currentState = table[currentState][ord(currentChar)]
					if currentState == -1:
						forward = first
						break
					elif currentState == len(table)-1:
						tok = token.Token(file[first:forward],"Operator")
						tok.printToken()
						symtab.insert(tok)
						#yield tok
						first = forward
					else:
						forward += 1
						currentChar = file[forward]
			#forward = first
	return symtab

disp = generateTokens();
disp.display_table()
