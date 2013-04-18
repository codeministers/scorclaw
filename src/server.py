import SimpleHTTPServer
import re

from logic import Logic

class Server(SimpleHTTPServer.SimpleHTTPRequestHandler):
    '''
    Class for HTTP server functions
    '''
    
    
    def build_logic(self, serial_port):
        self.logic = Logic(serial_port)
        self.logic.initialize()
        print 'lets go'
        
    
    def do_GET(self):
        path = self.path
        pathSplitted = re.split('/', path)
        
        good_path = True
        response = ''
        
        if len(pathSplitted) == 2 and pathSplitted[1] != '':
            verb = pathSplitted[1]
            
            if verb == 'more_x':
                self.logic.more_x()
                response = 'more x done'
                
            elif verb == 'less_x':
                self.logic.less_x()
                response = 'less x done'
                
            elif verb == 'more_y':
                self.logic.more_y()
                response = 'more y done'
                
            elif verb == 'less_y':
                self.logic.less_y()
                response = 'less y done'
                
            elif verb == 'catch':
                self.logic.catch()
                response = 'catch done'
                
            elif verb == 'home':
                self.logic.home()
                response = 'home done'
                
            elif verb == 'canIMove':
                response = 'yesYouCan'
            
            else:
                good_path = False
                response = 'not a valid verb'
                
        else:
            good_path = False
            response = 'not a valid path'
        
        if good_path:
            self.send_response(200)
            self.send_header('Content-type','application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
        
        else:
            self.send_response(404)
            self.send_header('Content-type','application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
        self.wfile.write('{"response": "' + response + '"}')
        
        