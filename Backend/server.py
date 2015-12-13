from flask import Flask
from flask import request
from RequestKind import RequestKind
from Request import Request
from RequestHandler import RequestHandler
		
				
class Server:
	def __init__(self):
		self.RequestHandler = RequestHandler()
		self.app = Flask(__name__)
		self.startListening()
		
	def startListening(self):
		print('listening')
		
		@self.app.route("/", methods = ['GET'])
		def index():
			return "index"
			
		@self.app.route("/move/<uniqueurl>/<int:uniqueid>", methods = ['POST'])
		def move(uniqueurl, uniqueid):
			print('received request on /move')
			res = self.RequestHandler.dispatchRequest(Request(uniqueurl = uniqueurl, 
														uniqueid = uniqueid, 
														requestKind = RequestKind.MoveRequest
														))
			#NEED TO IMPLEMENT THE MOVE FUCNTION
			return str(res)
			
		@self.app.route("/createnewgame", methods = ['GET'])
		def create():
			print('received request on /createnewgame')
			res = self.RequestHandler.dispatchRequest(Request(requestKind = RequestKind.CreateNewGameRequest))
			r = res['uniqueurl'] #NEED TO DO SOME CHEKCING HERE
			return str(r)
			
			
		@self.app.route("/joingame/<int:uniqueurl>", methods = ['GET'])
		def join(uniqueurl):
			print('received request on /joingame')
			res = self.RequestHandler.dispatchRequest(Request(requestKind = RequestKind.JoinGameRequest,
															  uniqueurl = uniqueurl))
			r = str(res)
			print(r) # STILL NEED SOME CHECKING 
			return r
		
		
		self.app.run()
		
		
		
		
s = Server()








