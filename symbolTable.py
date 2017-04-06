import token

class symbolTable:
	def __init__(self):
		self.table = {}
	
	def insert(self, a):
		if a.id not in self.table.keys():
			self.table[a.id] = a.type

	def display_table(self):
		print(self.table)