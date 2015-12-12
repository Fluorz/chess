from random import randint
from enum import Enum
from flask import Flask
from flask import request


class Game:
	def __init__(self, url):
		self.url = url
		self.ready = False
		self.board = []
		
	def initBoard(self):
		self.board = [[0, '.', 1, 1], [0, '.', 1, 2], [0, '.', 1, 3], [0, '.', 1, 4], 
					  [0, '.', 1, 5], [0, '.', 1, 6], [0, '.', 1, 7], [0, '.', 1, 8], 
					  [0, '.', 2, 1], [0, '.', 2, 2], [0, '.', 2, 3], [0, '.', 2, 4], 
					  [0, '.', 2, 5], [0, '.', 2, 6], [0, '.', 2, 7], [0, '.', 2, 8], 
					  [0, '.', 3, 1], [0, '.', 3, 2], [0, '.', 3, 3], [0, '.', 3, 4], 
					  [0, '.', 3, 5], [0, '.', 3, 6], [0, '.', 3, 7], [0, '.', 3, 8], 
					  [0, '.', 4, 1], [0, '.', 4, 2], [0, '.', 4, 3], [0, '.', 4, 4], 
					  [0, '.', 4, 5], [0, '.', 4, 6], [0, '.', 4, 7], [0, '.', 4, 8], 
					  [0, '.', 5, 1], [0, '.', 5, 2], [0, '.', 5, 3], [0, '.', 5, 4], 
					  [0, '.', 5, 5], [0, '.', 5, 6], [0, '.', 5, 7], [0, '.', 5, 8], 
					  [0, '.', 6, 1], [0, '.', 6, 2], [0, '.', 6, 3], [0, '.', 6, 4], 
					  [0, '.', 6, 5], [0, '.', 6, 6], [0, '.', 6, 7], [0, '.', 6, 8], 
					  [0, '.', 7, 1], [0, '.', 7, 2], [0, '.', 7, 3], [0, '.', 7, 4], 
					  [0, '.', 7, 5], [0, '.', 7, 6], [0, '.', 7, 7], [0, '.', 7, 8], 
					  [0, '.', 8, 1], [0, '.', 8, 2], [0, '.', 8, 3], [0, '.', 8, 4], 
					  [0, '.', 8, 5], [0, '.', 8, 6], [0, '.', 8, 7], [0, '.', 8, 8]]
		
	def getBoard(self):
		return self.board

	def updateBoard(self, newBoard):
		self.board = newBoard
		
class SessionStorage:
	def __init__(self):
		self.sessions = []
		#sessions : [[uniqueurl, [player1uniqueid, player2uniqueid], Game], [...]]
		
		
	def requestNewSession(self, uniqueurl):
		if(uniqueurl not in self.sessions):
			ids = self.generateUniqueIds()
			self.sessions.extend([[uniqueurl, ids, Game(uniqueurl)]])
			return [True, ids]
		else:
			return False
			
	def generateUniqueIds(self):
		return [randint(0, 1000), randint(1001, 2000)]
		
	def getSession(self, uniqueid):
		for s in self.sessions:
			if s[0] == uniqueid:
				return s
		
class RequestKind(Enum):
	CreateNewGameRequest = 0
	JoinGameRequest = 1
	GameUpdateRequest = 2
	MoveRequest = 3
	
		
class Request:
	def __init__(self, uniqueurl = -1, uniqueid = -1, requestKind = -1):
		print('creating new request')
		if (requestKind != -1):
			print('ok')
			if uniqueid != -1:
				self.uniqueId = uniqueid
			if uniqueurl != -1:
				self.uniqueUrl = uniqueurl
			
			self.requestKind = requestKind
			self.params = self.parseParams()
			
		else:
			print('nok')
			self.requestKind = False
		
	def parseParams(self):
		if self.requestKind == -1:
			return False
		if self.requestKind == 0:
			print('0')
			return False
		if self.requestKind == 1:
			print('1')	
			return {'uniqueurl': self.uniqueUrl}
		if self.requestKind == 2:
			print('2')
			return {'uniqueurl': self.uniqueUrl}
		if self.requestKind == 3:
			print('3')
			return {'uniqueid': self.uniqueId, 'uniqueurl': self.uniqueUrl, 'move': request.form['move']}
		
class RequestHandler:
	def __init__(self):
		print('Request handler init')
		
	def dispatchRequest(self, rq):
		print('dispatching request')
		if rq.requestKind != False:
			if rq.requestKind == 0:
				self.handleNewGameRequest(rq)
			if rq.requestKind == 1:
				self.handleJoinGameRequest(rq)
			if rq.requestKind == 2:
				self.handleGameUpdateRequest(rq)
			if rq.requestKind == 3:
				self.handleMoveRequest(rq)
		else:
			return False
			
	def handleNewGameRequest(self, rq):
		print('handling new game request')
		print(rq.params)
	
	def handleJoinGameRequest(self, rq):
		print('handling join game request')
		print(rq.params)
	
	def handleGameUpdateRequest(self, rq):
		print('handling game udpate request')
		print(rq.params)
		
	def handleMoveRequest(self, rq):
		print('handling move request')
		print(rq.params)
		
		
				
				
class Server:
	def __init__(self):
		self.SessionStorage = SessionStorage()
		self.RequestHandler = RequestHandler()
		self.ip = '127.0.0.1'
		self.port = '80'
		self.app = Flask(__name__)
		self.startListening()
		
	def startListening(self):
		print('listening')
		#CODE THAT
		#on request:
		
		@self.app.route("/", methods = ['GET'])
		def index():
			return "index"
			
		@self.app.route("/move/<uniqueurl>/<int:uniqueid>", methods = ['POST'])
		def move(uniqueurl, uniqueid):
			print('received request on /move')
			res = self.RequestHandler.dispatchRequest(Request(uniqueurl = uniqueurl, 
														uniqueid = uniqueid, 
														requestKind = 3
														))
			return "lel"
			
		self.app.run()
		#received = 0
		#self.RequestHandler.dispatchRequest(Request(received))
s = Server()

#r = Request(rqObject = "lele", uniqueurl = 'eele', uniqueid = 'elele', requestKind = 4)








