from flask import Flask
from flask import request
from RequestKind import RequestKind
from Request import Request
from RequestHandler import RequestHandler
from Logger import Logger

class Server:

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.__name__ = "Server"
        self.RequestHandler = RequestHandler()
        self.app = Flask(__name__)
        self.app.debug = False
        self.startListening()

    def startListening(self):
        Logger.log('Listening')

        @self.app.route("/", methods=['GET'])
        def index():
            Logger.printCurrentState(
                self.RequestHandler.SessionStorage.sessions)
            return "index"
            
        @self.app.route("/move/<uniqueurl>/<int:uniqueid>", methods=['POST'])
        def move(uniqueurl, uniqueid):
            Logger.printCurrentState(
                self.RequestHandler.SessionStorage.sessions)
            Logger.log('Received request on /move')
            Logger.log(uniqueurl)
            res = self.RequestHandler.dispatchRequest(
                Request(
                    uniqueurl=uniqueurl,
                    uniqueid=uniqueid,
                    requestKind=RequestKind.MoveRequest))
            # NEED TO IMPLEMENT THE MOVE FUCNTION
            return str(res)

        @self.app.route("/createnewgame", methods=['GET'])
        def create():
            Logger.printCurrentState(
                self.RequestHandler.SessionStorage.sessions)
            Logger.log('Received request on /createnewgame')
            res = self.RequestHandler.dispatchRequest(
                Request(requestKind=RequestKind.CreateNewGameRequest))
            r = res['uniqueurl']  # NEED TO DO SOME CHEKCING HERE
            return str(r)

        @self.app.route("/joingame/<int:uniqueurl>", methods=['GET'])
        def join(uniqueurl):
            Logger.printCurrentState(
                self.RequestHandler.SessionStorage.sessions)
            Logger.log('Received request on /joingame')
            res = self.RequestHandler.dispatchRequest(
                Request(requestKind=RequestKind.JoinGameRequest, uniqueurl=uniqueurl))
            return str(res)
            
        @self.app.route("/gameupdate/<int:uniqueurl>", methods=['GET'])
        def update(uniqueurl):
            Logger.printCurrentState(self.RequestHandler.SessionStorage.sessions)
            Logger.log('Received a request on /gameupdate')
            res = self.RequestHandler.dispatchRequest(
                Request(requestKind=RequestKind.GameUpdateRequest, uniqueurl=uniqueurl))
            return res
        
        @self.app.route("/debug", methods=['GET'])
        def debug():
            return str(self.RequestHandler.SessionStorage.sessions)
            
        

        self.app.run(host=self.ip, port=self.port)

