from Pieces import *


class Game:
	def __init__(self):
		self.ready = False
		self.players = 0
		self.board = []
		self.playerTurn = 0
		
	def initBoard(self):
		self.board = [NoPiece(0, 1, 1), NoPiece(0, 1, 2), NoPiece(0, 1, 3), NoPiece(0, 1, 4), NoPiece(0, 1, 5), NoPiece(0, 1, 6), NoPiece(0, 1, 7), NoPiece(0, 1, 8), NoPiece(0, 2, 1), NoPiece(0, 2, 2), NoPiece(0, 2, 3), NoPiece(0, 2, 4), NoPiece(0, 2, 5), NoPiece(0, 2, 6), NoPiece(0, 2, 7), NoPiece(0, 2, 8), NoPiece(0, 3, 1), NoPiece(0, 3, 2), NoPiece(0, 3, 3), NoPiece(0, 3, 4), NoPiece(0, 3, 5), NoPiece(0, 3, 6), NoPiece(0, 3, 7), NoPiece(0, 3, 8), NoPiece(0, 4, 1), NoPiece(0, 4, 2), NoPiece(0, 4, 3), NoPiece(0, 4, 4), NoPiece(0, 4, 5), NoPiece(0, 4, 6), NoPiece(0, 4, 7), NoPiece(0, 4, 8), NoPiece(0, 5, 1), NoPiece(0, 5, 2), NoPiece(0, 5, 3), NoPiece(0, 5, 4), NoPiece(0, 5, 5), NoPiece(0, 5, 6), NoPiece(0, 5, 7), NoPiece(0, 5, 8), NoPiece(0, 6, 1), NoPiece(0, 6, 2), NoPiece(0, 6, 3), NoPiece(0, 6, 4), NoPiece(0, 6, 5), NoPiece(0, 6, 6), NoPiece(0, 6, 7), NoPiece(0, 6, 8), NoPiece(0, 7, 1), NoPiece(0, 7, 2), NoPiece(0, 7, 3), NoPiece(0, 7, 4), NoPiece(0, 7, 5), NoPiece(0, 7, 6), NoPiece(0, 7, 7), NoPiece(0, 7, 8), NoPiece(0, 8, 1), NoPiece(0, 8, 2), NoPiece(0, 8, 3), NoPiece(0, 8, 4), NoPiece(0, 8, 5), NoPiece(0, 8, 6), NoPiece(0, 8, 7), NoPiece(0, 8, 8)]
	def getBoard(self):
		return self.board

	def updateBoard(self, newBoard):
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
		print('added 1')
		
	def isSpaceOccupied(self, x, y):
		for i in range(0, len(self.board)):
			if self.board[i][0].x == x and  self.board[i][1].y == y:
				if type(self.board[i][1]) == NoPiece:
					return i
				else:
					return True
				
	def doMove(self, move):	
		r = self.isSpaceOccupied(move['newX'], move['newY'])
		if r is True:
			return 'space taken'
		elif type(r) is int:
			print('k')
			
			
g = Game()
g.initBoard()
print(g.board[6].x)
			
			
		