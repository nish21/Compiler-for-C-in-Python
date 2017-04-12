class Token:
	def __init__(self, id, type):
		self.id = id;
		self.type = type;
		self.data_type = None
		self.size = None

	def getFields(self):
		return tuple(self.id,self.type)

	def printToken(self):
		print(tuple([self.id, self.type]))
