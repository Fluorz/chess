class Pawn:
	def canAccessPosition(self, joueur, x, y, newX, newY):
		xMoveOk = False
		yMoveOk = False
		if 1 <= x <= 8 and 1 <= y <= 8 and 1 <= newX <= 8 and 1 <= newY <= 8:
			if joueur == 0:
				if (y - newY) == -2:
					if y == 2:
						yMoveOk = True
				if (y - newY) == -1:
					yMoveOk = True
				if x is not newX:
					if abs(x - newX) == 1:
						xMoveOk = True
				else:
					xMoveOk = True
					
			if joueur == 1:
				if (y - newY) == 2:
					if y == 7:
						yMoveOk = True
				if (y - newY) == 1:
					yMoveOk = True
				if x is not newX:
					if abs(x - newX) == 1:
						xMoveOk = True
				else:
					xMoveOk = True
					
			if xMoveOk == True and yMoveOk == True:
				return True
			else:
				return False
		else:
			return False
			
class King:
	def canAccessPosition(self, joueur, x, y, newX, newY):
		if 1 <= x <= 8 and 1 <= y <= 8 and 1 <= newX <= 8 and 1 <= newY <= 8:
			xMoveOk = False
			yMoveOk = False
			if x < newX:
				if (x + 1) == newX and (x + 1) <= 8:
					xMoveOk = True
			elif x > newX:
				if (x - 1) == newX and (x - 1) >= 1:
					xMoveOk = True
			else:
				xMoveOk = True
			if y < newY:
				if (y + 1) == newY and (y + 1) <= 8:
					yMoveOk = True
			elif y > newY:
				if (y - 1) == newY and (y - 1) >= 1:
					yMoveOk = True
			else:
				yMoveOk = True
			
			if xMoveOk and yMoveOk:
				return True
			else:
				return False
 		else:
			return False

class Horse:
	def canAccessPosition(self, joueur, x, y, newX, newY):
		if 1 <= x <= 8 and 1 <= y <= 8 and 1 <= newX <= 8 and 1 <= newY <= 8:
			xMoveOk = False
			yMoveOk = False
			
		
	def getAvailablePositions(self, x, y):
		arr = []
		arr.append([y + 2, x + 1])
		arr.append([y + 2, x - 1])
		arr.append([y + 1, x + 2])
		arr.append([y - 1, x + 2])
		arr.append([y - 2, x + 1])
		arr.append([y - 2, x - 1])
		arr.append([y + 1, x - 2])
		arr.append([y - 1, x - 2])
	
		for i in range(0, len(arr)): #[y, x]... Reverse pour avoir [x, y]
			arr[i].reverse()
			
		print(arr)
		
		
		
		
		
		