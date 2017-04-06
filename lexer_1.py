def return_auto(charset = 256):
	table = []
	for i in range(8):
		table.append(list([0]*charset))
	table[0][ord('r')] = 1
	table[1][ord('e')] = 2
	table[2][ord('t')] = 3
	table[3][ord('u')] = 4
	table[4][ord('r')] = 5
	table[5][ord('n')] = 6
	table[6][ord(' ')] = 7
	table[6][ord('\n')] = 7
	table[6][ord('\t')] = 7
	table[6][ord(';')] = 7
	return table

def const_auto(charset = 256):
	table = []
	for i in range(7):
		table.append(list([0]*charset))
	table[0][ord('c')] = 1
	table[1][ord('o')] = 2
	table[2][ord('n')] = 3
	table[3][ord('s')] = 4
	table[4][ord('t')] = 5
	table[5][ord(' ')] = 6
	table[5][ord('\n')] = 6
	table[5][ord('\t')] = 6
	table[5][ord(';')] = 6
	return table


def short_auto(charset = 256):
	table = []
	for i in range(7):
		table.append(list([0]*charset))
	table[0][ord('s')] = 1
	table[1][ord('h')] = 2
	table[2][ord('o')] = 3
	table[3][ord('r')] = 4
	table[4][ord('t')] = 5
	table[5][ord(' ')] = 6
	table[5][ord('\n')] = 6
	table[5][ord('\t')] = 6
	table[5][ord(';')] = 6
	return table

def id_auto(charset = 256):
	table = []
	for i in range(3):
		table.append(list([0]*charset))
	table[0][ord('_')] = 1
	for i in range(26):
		table[0][ord('a')+i] = 1
		table[0][ord('A')+i] = 1
		table[1][ord('a')+i] = 1
		table[1][ord('A')+i] = 1
	table[1][ord(' ')] = 2
	table[1][ord('\n')] = 2
	table[1][ord('\t')] = 2
	table[1][ord(';')] = 2
	return table

def logical_auto(charset = 256):
	table = []
	for i in range(7):
		table.append(list([0]*charset))
	table[0][ord('&')] = 1
	table[1][ord('&')] = 2
	table[0][ord('|')] = 3
	table[3][ord('|')] = 4
	table[0][ord('!')] = 5
	for i in [2,4,5]:
		table[i][ord(' ')] = 6
		table[i][ord('\n')] = 6
		table[i][ord('\t')] = 6
		table[i][ord(';')] = 6
	return table

def int_auto(charset = 256):
	table = []
	for i in range(5):
		table.append(list([0]*charset))
	table[0][ord('i')] = 1
	table[1][ord('n')] = 2
	table[2][ord('t')] = 3
	table[3][ord(' ')] = 4
	table[3][ord('\n')] = 4
	table[3][ord('\t')] = 4
	table[3][ord(';')] = 4
	return table

def float_auto(charset = 256):
	table = []
	for i in range(7):
		table.append(list([0]*charset))
	table[0][ord('f')] = 1
	table[1][ord('l')] = 2
	table[2][ord('o')] = 3
	table[3][ord('a')] = 4
	table[4][ord('t')] = 5
	table[5][ord('\t')] = 6
	table[5][ord('\n')] = 6
	table[5][ord(';')] = 6
	table[5][ord(' ')] = 6
	return table

def char_auto(charset = 256):
	table = []
	for i in range(6):
		table.append(list([0]*charset))
	table[0][ord('c')] = 1
	table[1][ord('h')] = 2
	table[2][ord('a')] = 3
	table[3][ord('r')] = 4
	table[4][ord('\t')] = 5
	table[4][ord('\n')] = 5
	table[4][ord(' ')] = 5
	table[4][ord(';')] = 5
	return table

def double_auto(charset = 256):
	table = []
	for i in range(8):
		table.append(list([0]*charset))
	table[0][ord('d')] = 1
	table[1][ord('o')] = 2
	table[2][ord('u')] = 3
	table[3][ord('b')] = 4
	table[4][ord('l')] = 5
	table[5][ord('e')] = 6
	table[6][ord(' ')] = 7
	table[6][ord(';')] = 7
	table[6][ord('\n')] = 7
	table[6][ord('\t')] = 7
	return table

def long_auto(charset = 256):
	table = []
	for i in range(6):
		table.append(list([0]*charset))
	table[0][ord('l')] = 1
	table[1][ord('o')] = 2
	table[2][ord('n')] = 3
	table[3][ord('g')] = 4
	table[4][ord('\t')] = 5
	table[4][ord('\n')] = 5
	table[4][ord(' ')] = 5
	table[4][ord(';')] = 5
	return table

def num_auto(charset = 256):
	table = []
	for i in range(3):
		table.append(list([0]*charset))
	for i in range(10):
		table[0]['0'+i] = 1
		table[1]['0'+i] = 1
	table[1][ord(" ")] = 2
	table[1][ord("\n")] = 2
	table[1][ord("\t")] = 2
	table[1][ord(";")] = 2
	return table

def stringliterals_auto(charset = 256):
	table = []
	for i in range(4):
		if i == 1:
			table.append(list([1]*charset))
		else:
			table.append(list([0]*charset))
	table[0][ord('"')] = 1
	table[1][ord('"')] = 2
	table[2][ord(' ')] = 3
	table[2][ord('\t')] = 3
	table[2][ord(';')] = 3
	table[2][ord('\n')] = 3
	return table

def arithmetic_auto(charset = 256):
	table = []
	for i in range(8):
		table.append(list([0]*charset))
	table[0][ord('+')] = 1
	table[0][ord('-')] = 2
	table[0][ord('*')] = 3
	table[0][ord('/')] = 4
	table[1][ord('+')] = 5
	table[2][ord('-')] = 6
	for i in range(1,7):
		table[i][ord(" ")] = 7
		table[i][ord(";")] = 7
		table[i][ord("\n")] = 7
		table[i][ord("\t")] = 7
	return table

def bitwise_auto(charset = 256):
	table = []
	for i in range(10):
		table.append(list([0]*charset))
	table[0][ord('&')] = 1
	table[0][ord('|')] = 2
	table[0][ord('^')] = 3
	table[0][ord('~')] = 4
	table[0][ord('<')] = 5
	table[5][ord('<')] = 6
	table[0][ord('>')] = 7
	table[7][ord('>')] = 8
	for i in [1,2,3,4,6,8]:
		table[i][ord(" ")] = 9
		table[i][ord(";")] = 9
		table[i][ord("\n")] = 9
		table[i][ord("\t")] = 9
	return table

def break_auto(charset = 256):
	table = []
	for i in range(7):
		table.append(list([0]*charset))
	table[0][ord('b')] = 1
	table[1][ord('r')] = 2
	table[2][ord('e')] = 3
	table[3][ord('a')] = 4
	table[4][ord('k')] = 5
	table[5][ord(' ')] = 6
	table[5][ord('\n')] = 6
	table[5][ord('\t')] = 6
	table[5][ord(';')] = 6
	return table

def continue_auto(charset = 256):
	table = []
	for i in range(13):
		table.append(list([0]*charset))
	table[0][ord('c')] = 1
	table[1][ord('o')] = 2
	table[2][ord('n')] = 3
	table[3][ord('t')] = 4
	table[4][ord('i')] = 5
	table[5][ord('n')] = 6
	table[6][ord('u')] = 7
	table[7][ord('e')] = 8
	table[8][ord(' ')] = 9
	table[8][ord('\n')] = 10
	table[8][ord('\t')] = 11
	table[8][ord(';')] = 12
	return table

def while_auto(charset = 256):
	table = []
	for i in range(7):
		table.append(list([0]*charset))
	table[0][ord('w')] = 1
	table[1][ord('h')] = 2
	table[2][ord('i')] = 3
	table[3][ord('l')] = 4
	table[4][ord('e')] = 5
	table[5][ord('\n')] = 6
	table[5][ord('\t')] = 6
	table[5][ord(';')] = 6
	table[5][ord(' ')] = 6
	return table


def reational_operator(charset = 256):
	table = []
	for i in range(14):
		table.append(list([0]*charset))
	table[0][ord('<')] = 1
	table[1][ord('=')] = 2
	table[0][ord('>')] = 3
	table[3][ord('=')] = 4
	table[0][ord('=')] = 5
	table[5][ord('=')] = 6
	table[0][ord('!')] = 7
	table[7][ord('=')] = 8
	for i in range(1,9):
		table[i][ord(' ')] = 9
		table[i][ord('\n')] = 9
		table[i][ord('\t')] = 9
		table[i][ord(';')] = 9

	return table
