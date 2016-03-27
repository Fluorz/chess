# -*- coding: utf-8 -*-

from Server import Server

#
# CLasse qui fémarre le serveur. 
#
class Starter:
    
    # 
    # DONE
    # Initialisation du la classe
    # Args : Options de démarrage (Non implémenté), Ip du serveur, Port du serveur
    # Return : Aucun
    # 
    def __init__(self, options, ip, port):
        self.options = options
        self.ip = ip
        self.port = port
        self.server = None
      
    #
    # DONE
    # Démarrage du serveur
    # Args : Aucun
    # Return : Aucun
    #
    def start(self):
        self.server = Server(self.ip, self.port)
        
s = Starter(None, '127.0.0.1', 8000)
s.start()
