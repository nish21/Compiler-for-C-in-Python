import token

class symbolTable:
	def __init__(self):
		self.table = {}

	def insert(self, a):
		if a.id not in self.table.keys():
			self.table[a.id] = [a.type, a.data_type, a.size]

	def display_table(self):
		for i in self.table.keys():
			print('{} {}'.format(i, self.table[i]))

	def contains(self, str):
		if str in self.table.keys():
			return True
		else:
			return False

	def setDataType(self, str, t):
		self.table[str][1] = t

	def setSize(self, str, s):
		self.table[str][2] = s

	def isVar(self, str):
		return self.table[str][1]
