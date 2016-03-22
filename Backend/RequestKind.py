from enum import Enum

'''
Enum qui associe des id de requète à des noms plus "dev-friendly"
'''
class RequestKind(Enum):
    CreateNewGameRequest = 0
    JoinGameRequest = 1
    GameUpdateRequest = 2
    MoveRequest = 3
