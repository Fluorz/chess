from SessionStorage import SessionStorage
from RequestKind import RequestKind

class RequestHandler:
	def __init__(self):
		print('Request handler init')
		self.SessionStorage = SessionStorage()
		
	def dispatchRequest(self, rq):
		print('dispatching request : ' + str(rq.requestKind))
		if rq.requestKind is not False:
			if rq.requestKind == RequestKind.CreateNewGameRequest:
				print('new')
				return self.handleNewGameRequest(rq)
			if rq.requestKind == RequestKind.JoinGameRequest:
				return self.handleJoinGameRequest(rq)
			if rq.requestKind == RequestKind.GameUpdateRequest:
				return self.handleGameUpdateRequest(rq)
			if rq.requestKind == RequestKind.MoveRequest:
				return self.handleMoveRequest(rq)
		else:
			return False
			
	def handleNewGameRequest(self, rq):
		print('handling new game request')
		print(rq.params)
		res = self.SessionStorage.addNewSession()
		print("res : " + str(res))
		return res
	
	def handleJoinGameRequest(self, rq):
		print('handling join game request')
		print(rq.params['uniqueurl'])
		res = self.SessionStorage.joinGame(rq.params['uniqueurl'])
		return res
	
	def handleGameUpdateRequest(self, rq):
		print('handling game udpate request')
		print(rq.params)
		return True
		
	def handleMoveRequest(self, rq):
		print('handling move request')
		print(rq.params)
		res = self.SessionStorage.move(rq.params['uniqueid'], rq.params['uniqueurl'], rq.params['move'])
		print("res move " + str(res))
		return True
		
		