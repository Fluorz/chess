from SessionStorage import SessionStorage
from RequestKind import RequestKind
from Logger import Logger


class RequestHandler:

    def __init__(self):
        Logger.log('Request handler init')
        self.SessionStorage = SessionStorage()

    def dispatchRequest(self, rq):
        Logger.log('dispatching request : ' + str(rq.requestKind))
        if rq.requestKind is not False:
            if rq.requestKind == RequestKind.CreateNewGameRequest:
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
        res = self.SessionStorage.addNewSession()
        return res

    def handleJoinGameRequest(self, rq):
        res = self.SessionStorage.joinGame(rq.params['uniqueurl'])
        return res

    def handleGameUpdateRequest(self, rq):
        res = self.SessionStorage.getGameStateJson(rq.params['uniqueurl'])
        return res

    def handleMoveRequest(self, rq):
        res = self.SessionStorage.move(
            rq.params['uniqueid'],
            rq.params['uniqueurl'],
            rq.params['move'])
        return res
