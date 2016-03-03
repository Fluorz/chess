from random import randint
from Game import Game
from Logger import Logger


class SessionStorage:

    def __init__(self):
        self.sessions = [[456, [12, 13], Game()]]
        # sessions : [[uniqueurl, [player1uniqueid, player2uniqueid], Game],
        # [...]]

    def generateUniqueIds(self):
        return [randint(0, 1000), randint(1001, 2000)]

    def generateUniqueUrl(self):
        u = randint(0, 5000)
        Logger.log('Generating unique url')
        if len(self.sessions) < 4000:
            for e in self.sessions:
                if u in e:
                    Logger.log('Collision')
                    return self.generateUniqueUrl()
            Logger.log('No collision')
            return u
        else:
            return {'error': 'Too many sessions'}

    def addNewSession(self):
        Logger.log('Adding new session')
        url = self.generateUniqueUrl()
        if isinstance(url, int):
            ids = self.generateUniqueIds()
            self.sessions.extend([[url, ids, Game()]])
        else:
            Logger.log(url['error'])
            return False
        return {'uniqueurl': url}

    def joinGame(self, uniqueurl):
        index = self.gameExists(uniqueurl)
        if index is not False:
            if self.sessions[index][2].playerCanJoin() is True:
                self.sessions[index][2].join()
                return self.sessions[index][1][
                    self.sessions[index][2].players - 1]  # the hard way
            else:
                return False
        else:
            return False


    def getGameStateJson(self, url):
        index = self.gameExists(url)
        if index is not None:
            res = self.sessions[index][2].getJson()
            return res

    
    def gameExists(self, uniqueurl):
        for i in range(0, len(self.sessions)):
            if self.sessions[i][0] == uniqueurl:
                return i
        return None

    def move(self, uniqueid, uniqueurl, move):
        i = self.gameExists(uniqueurl)
        if i is not None:
            if self.sessions[i][1][self.sessions[i][2].playerTurn] == uniqueid:
                res = self.sessions[i][2].doMove(move)
                return res
            else:
                Logger.log('nnn')
        else:
            Logger.log('eeeeredfd')

    