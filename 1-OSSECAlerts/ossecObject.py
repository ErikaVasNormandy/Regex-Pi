

class ossecAlert():
	def __init__(self, raw_content):
		self.raw_content = raw_content
		self.received = ""
		self._from= ""
		self.to = ""
		self.date = ""
		self.subject = ""
		self.receivedfrom = ""

		self.rule = ""
		self.logcontent = ""




	def showContent(self):
		print("rawcontent is: ", self.raw_content)

