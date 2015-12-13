from enum import Enum

class RequestKind(Enum):
	CreateNewGameRequest = 0
	JoinGameRequest = 1
	GameUpdateRequest = 2
	MoveRequest = 3