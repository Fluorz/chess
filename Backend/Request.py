from flask import request
from RequestKind import RequestKind
import json
from Logger import Logger

'''
Classe qui représente les requètes et leurs paramètres
'''
class Request:

    '''
    DONE
    Initialisation
    Args : url unique (facultative), id unique (facultatif), id de requête (facultatif)
    Return : Aucun
    '''
    def __init__(self, uniqueurl=-1, uniqueid=-1, requestKind=-1):
        if (requestKind != -1):
            if uniqueid != -1:
                self.uniqueId = uniqueid
            if uniqueurl != -1:
                self.uniqueUrl = uniqueurl
            self.requestKind = requestKind
            self.params = self.parseParams()

        else:
            self.requestKind = False

    '''
    DONE
    Analyse des paramètres
    Args : Aucun
    Return : Tableau des paramètres nécessaires
    '''
    def parseParams(self):
        if self.requestKind == -1:
            return False
        if self.requestKind == RequestKind.CreateNewGameRequest:
            return False
        if self.requestKind == RequestKind.JoinGameRequest:
            return {'uniqueurl': self.uniqueUrl}
        if self.requestKind == RequestKind.GameUpdateRequest:
            return {'uniqueurl': self.uniqueUrl}
        if self.requestKind == RequestKind.MoveRequest:
            moveParams = json.loads(request.form['move'])
            return {
                'uniqueid': self.uniqueId,
                'uniqueurl': self.uniqueUrl,
                'move': moveParams}
