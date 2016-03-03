from Server import Server

class Starter:
    def __init__(self, options, ip, port):
        self.options = options
        self.ip = ip
        self.port = port
        self.server = None
        
    def start(self):
        self.server = Server(self.ip, self.port)
        
s = Starter(None, '127.0.0.1', 8000)
s.start()

