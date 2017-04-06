class Token:
	def __init__(self, id, type):
		self.id = id;
		self.type = type;

	def getFields(self):
		return tuple(self.id,self.type)

	def printToken(self):
		print(tuple([self.id, self.type]))

	