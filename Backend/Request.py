from flask import request
from RequestKind import RequestKind
		
class Request:
	def __init__(self, uniqueurl = -1, uniqueid = -1, requestKind = -1):
		print('creating new request')
		print('rq ' + str(requestKind))
		if (requestKind != -1):
			print('ok')
			if uniqueid != -1:
				self.uniqueId = uniqueid
			if uniqueurl != -1:
				self.uniqueUrl = uniqueurl
			
			self.requestKind = requestKind
			print('rq2 ' + str(self.requestKind))
			self.params = self.parseParams()
			
		else:
			print('nok')
			self.requestKind = False
		
	def parseParams(self):
		if self.requestKind == -1:
			return False
		if self.requestKind == RequestKind.CreateNewGameRequest:
			print('0')
			return False
		if self.requestKind == RequestKind.JoinGameRequest:
			print('1')	
			return {'uniqueurl': self.uniqueUrl}
		if self.requestKind == RequestKind.GameUpdateRequest:
			print('2')
			return {'uniqueurl': self.uniqueUrl}
		if self.requestKind == RequestKind.MoveRequest:
			print('3')
			return {'uniqueid': self.uniqueId, 'uniqueurl': self.uniqueUrl, 'move': request.form['move']}
		