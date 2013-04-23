import SimpleHTTPServer
import re

from variables import SERIAL_PORT

from logic import Logic


logic = Logic(SERIAL_PORT)
logic.initialize()


class Requests(SimpleHTTPServer.SimpleHTTPRequestHandler):
    '''
    Class for handle HTTP requests
    '''
    
    
    def do_GET(self):
        path = self.path
        pathSplitted = re.split('/', path)
        
        good_path = True
        response = ''
        
        if len(pathSplitted) == 2 and pathSplitted[1] != '':
            verb = pathSplitted[1]
            
            if verb == 'more_x':
                logic.more_x()
                response = 'more x done'
                
            elif verb == 'less_x':
                logic.less_x()
                response = 'less x done'
                
            elif verb == 'more_y':
                logic.more_y()
                response = 'more y done'
                
            elif verb == 'less_y':
                logic.less_y()
                response = 'less y done'
                
            elif verb == 'catch':
                logic.catch()
                response = 'catch done'
                
            elif verb == 'home':
                logic.home()
                response = 'home done'
                
            else:
                good_path = False
                response = 'not a valid verb'
                
        else:
            good_path = False
            response = 'not a valid path'
        
        if good_path:
            self.send_response(200)
        
        else:
            self.send_response(404)
            
        self.send_header('Content-type','application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write('{"response": "' + response + '"}')
        
    