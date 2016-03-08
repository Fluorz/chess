from inspect import *
from Options import RunOptions

class Logger:

    @staticmethod
    def printCurrentState(gameState):
        print('\n\n-----GAME STATE-----\n')
        print('{0} active sessions'.format(len(gameState)))
        for i in gameState:
            print('Session url : {0} - Session player ids : {1}'.format(i[0], i[1]))
        print('\n--------------------\n\n')

    @staticmethod
    def log(message):
        caller = getframeinfo(stack()[1][0])
        path = caller[0]
        if '\\' in path:
            path = path.split('\\')[-1]
        line = caller[1]
        print('{0}:{1} - {2}'.format(path, line, message))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        