#!/usr/bin/python
# -*- coding: utf-8 -*-
from Pieces import *
from Logger import Logger
import json

class Game:

    #
    # DONE
    # Initialisation de la partie
    # Args : Aucun
    # Return Aucun
    #
    def __init__(self):
        self.ready = False
        self.players = 0
        self.board = []
        self.playerTurn = 0
        self.initBoard()

    #
    # DONE
    # Initialisation du tableau qui contient toutes les pièces de l'échiquier
    # Args : Aucun
    # Return : Aucun
    #
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

    #
    # DONE
    # Renvoie le tableau qui contient toutes les pièces de l'échiquier
    # Args : Aucun
    # Return : Un tableau contenant les pièces
    #
    def getBoard(self):
        return self.board

    #
    # Met a jour le tableau contenant les pièces après un mouvement
    # Args : L'index de la pièce qui va bouger
    # Return : Aucun
    #
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

    #
    # DONE
    # Un joueur peut-il rejoindre la partie?
    # Args : Aucun
    # Return : True si c'est possible, False sinon
    #
    def playerCanJoin(self):
        if self.players < 2:
            return True
        else:
            return False
    #
    # DONE
    # Ajoute un joueur à la partie
    # Args : Aucun
    # Return Aucun
    #
    def join(self):
        self.players += 1
        if self.players == 2:
            self.initBoard()

    #
    # DONE
    # La coordonnée est elle occupée? 
    # Args : coordonée x, coordonée y
    # Return : index de la coordonnée si il n'y a pas de pièce, True sinon
    #
    def isSpaceOccupied(self, x, y):
        for i in range(0, len(self.board)):
            if self.board[i][0].x == x and self.board[i][1].y == y:
                if isinstance(self.board[i][1], NoPiece):
                    return i
                else:
                    return True

    #
    # TODO
    # S'occupe de bouger les pièces sur l'échiquier 
    # Args : move (JSON?) pas fini donc pas sur
    # Return : Sais pas encore (pas fini)
    #
    def doMove(self, move):
        r = self.isSpaceOccupied(move['newX'], move['newY'])
        if r is True:
            return 'space taken'
        elif isinstance(r, int):
            self.updateBoard()
    
    #
    # DONE
    # Renvoie une représentation JSON du tableau contenant les pièces
    # Args : Aucun
    # Return : JSON du tableau contenant les pièces et le tour du joueur
    #
    def getJson(self):
        resData = {}
        tempBoard = self.board
        for i in range(0, len(tempBoard)):
            if type(tempBoard[i]) is not str:
                tempBoard[i] = tempBoard[i].__name__
        resData['board'] = tempBoard
        resData['playerTurn'] = self.playerTurn
        return json.dumps(resData)
            
        
        
        
        
        
            
