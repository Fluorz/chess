from random import randint
from Game import Game

class SessionStorage:
	def __init__(self):
		self.sessions = [['456', [12, 13], Game(456)]]
		#sessions : [[uniqueurl, [player1uniqueid, player2uniqueid], Game], [...]]
			
	def generateUniqueIds(self):
		return [randint(0, 1000), randint(1001, 2000)]
		
	def generateUniqueUrl(self):
		u = randint(0, 5000)
		print('generating unique url')
		if len(self.sessions) < 4000:
			for e in self.sessions:
				if u in e:
					print('collision')
					return self.generateUniqueUrl()
			print('no collision')
			return u
		else:
			return {'error': 'Too many sessions'}
			
				
	def addNewSession(self):
		print('adding new session')
		url = self.generateUniqueUrl()
		print('url' + str(url))
		if isinstance(url, int):
			ids = self.generateUniqueIds()
			self.sessions.extend([[url, ids, Game(url)]])
		else:
			print(url['error'])
			return False
		return {'uniqueurl': url}
		
	def joinGame(self, uniqueurl):
		print(uniqueurl)
		print(self.sessions)
		index = self.gameExists(uniqueurl)
		if index is not False:
			if self.sessions[index][2].playerCanJoin() is True:
				self.sessions[index][2].join()
				return self.sessions[index][1][self.sessions[index][2].players - 1] #the hard way 
		else:
			return False
			
			
	def gameExists(self, uniqueurl):
		for i in range(0, len(self.sessions)):
			print('ererere ' + str(self.sessions[i]))
			print('eeeee ' + str(i))
			print(type(uniqueurl))
			print(type(self.sessions[i][0]))
			if self.sessions[i][0] == uniqueurl:
				print('game exists')
				return i
			else:
				print('arf')
		print('game doesnt exist')
		return None
					
	def move(self, uniqueid, uniqueurl, move):
		i = self.gameExists(uniqueurl)
		if i is not None:
			if self.sessions[1][self.sessions[i][2].playerTurn] == uniqueid:
				print('kkk')
				# WOrking so far. TODO : finish this. 
			else:
				print('nnn')
			
					
					
					
					
					
					
					
		
		

	