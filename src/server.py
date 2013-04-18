import SimpleHTTPServer
import SocketServer
import re

from logic import Logic

class Server(SimpleHTTPServer.SimpleHTTPRequestHandler):
    '''
    Class for HTTP server functions
    '''
    
    def __init__(self, serial_port):
        self.logic = Logic(serial_port)
        self.logic.initialize()
    
    def do_GET(self):
        path = self.path
        pathSplitted = re.split('/', path)
        
        if len(pathSplitted) == 2 and pathSplitted[1] != '':
            verb = pathSplitted[1]
            if verb == '+x': # arriba
                self.logic.more_x()
            elif verb == '-x': # abajo
                self.logic.less_x()
            elif verb == '+y': # <
                self.logic.more_y()
            elif verb == '-y': # >
                self.logic.less_y()
            elif verb == 'catch':
                self.logic.catch()
            elif verb == 'home':
                self.logic.home()
            elif verb == 'canIMove':
                response = 'yesYouCan'
            
            