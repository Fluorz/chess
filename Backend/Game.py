#!/usr/bin/python
# -*- coding: utf-8 -*-
from Pieces import *
from Logger import Logger
import json

class Game:

    def __init__(self):
        self.ready = False
        self.players = 0
        self.board = []
        self.playerTurn = 0
        self.initBoard()

    def initBoard(self):
        self.board = [
            NoPiece(0, 1, 1),
            NoPiece(0, 1, 2),
            NoPiece(0, 1, 3),
            NoPiece(0, 1, 4),
            NoPiece(0, 1, 5),
            NoPiece(0, 1, 6),
            NoPiece(0, 1, 7),
            NoPiece(0, 1, 8),
            NoPiece(0, 2, 1),
            NoPiece(0, 2, 2),
            NoPiece(0, 2, 3),
            NoPiece(0, 2, 4),
            NoPiece(0, 2, 5),
            NoPiece(0, 2, 6),
            NoPiece(0, 2, 7),
            NoPiece(0, 2, 8),
            NoPiece(0, 3, 1),
            NoPiece(0, 3, 2),
            NoPiece(0, 3, 3),
            NoPiece(0, 3, 4),
            NoPiece(0, 3, 5),
            NoPiece(0, 3, 6),
            NoPiece(0, 3, 7),
            NoPiece(0, 3, 8),
            NoPiece(0, 4, 1),
            NoPiece(0, 4, 2),
            NoPiece(0, 4, 3),
            NoPiece(0, 4, 4),
            NoPiece(0, 4, 5),
            NoPiece(0, 4, 6),
            NoPiece(0, 4, 7),
            NoPiece(0, 4, 8),
            NoPiece(0, 5, 1),
            NoPiece(0, 5, 2),
            NoPiece(0, 5, 3),
            NoPiece(0, 5, 4),
            NoPiece(0, 5, 5),
            NoPiece(0, 5, 6),
            NoPiece(0, 5, 7),
            NoPiece(0, 5, 8),
            NoPiece(0, 6, 1),
            NoPiece(0, 6, 2),
            NoPiece(0, 6, 3),
            NoPiece(0, 6, 4),
            NoPiece(0, 6, 5),
            NoPiece(0, 6, 6),
            NoPiece(0, 6, 7),
            NoPiece(0, 6, 8),
            NoPiece(0, 7, 1),
            NoPiece(0, 7, 2),
            NoPiece(0, 7, 3),
            NoPiece(0, 7, 4),
            NoPiece(0, 7, 5),
            NoPiece(0, 7, 6),
            NoPiece(0, 7, 7),
            NoPiece(0, 7, 8),
            NoPiece(0, 8, 1),
            NoPiece(0, 8, 2),
            NoPiece(0, 8, 3),
            NoPiece(0, 8, 4),
            NoPiece(0, 8, 5),
            NoPiece(0, 8, 6),
            NoPiece(0, 8, 7),
            NoPiece(0, 8, 8)
            ]

    def getBoard(self):
        return self.board

    def updateBoard(
        self,
        index,
        newX,
        newY,
        ):
        for i in range(0, len(self.board)):
            if self.board[i].x == newX and self.board[i].y == newY:
                newBoard = self.board
                newBoard[i] = self.board[index]
                newBoard[index] = NoPiece(self.board[index].j,
                        self.board[index].x, self.board[index].y)
                self.board = newBoard

    def playerCanJoin(self):
        if self.players < 2:
            return True
        else:
            return False

    def join(self):
        self.players += 1
        if self.players == 2:
            self.initBoard()

    def isSpaceOccupied(self, x, y):
        for i in range(0, len(self.board)):
            if self.board[i][0].x == x and self.board[i][1].y == y:
                if isinstance(self.board[i][1], NoPiece):
                    return i
                else:
                    return True

    def doMove(self, move):
        r = self.isSpaceOccupied(move['newX'], move['newY'])
        if r is True:
            return 'space taken'
        elif isinstance(r, int):
            self.updateBoard()

    def getJson(self):
        resData = {}
        tempBoard = self.board
        for i in range(0, len(tempBoard)):
            if type(tempBoard[i]) is not str:
                tempBoard[i] = tempBoard[i].__name__
        resData['board'] = tempBoard
        resData['playerTurn'] = self.playerTurn
        return json.dumps(resData)
            
    '''
    To do
    Fonctions pour savoir si il y a echec
    '''

    from Pieces import *

     '''
     Done
     args: liste des pieces, le x et y du roi
     return: si il y a echec ou pas
     '''
    def echec(self, liste, xKing, yKing):
        tableau=[]
        for i in liste:
            if i.canAccessPosition(xKing, yKing):
                tableau.append(i)
                return True 

        return False
    
    '''
     To do
     
     return: si il y a une piece sur le chemin qui pourrait gener le deplacement ou pas
    '''
     def piece_sur_le_chemin(self, xKing, yKing, liste):
          
                
               
               
          
          
     

        
        
        
        
        
            
