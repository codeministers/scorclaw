import SimpleHTTPServer
import SocketServer
import re

from logic import Logic

SERVER_PORT = 8080
SERIAL_PORT = '/dev/cu.PL2303-00002006'

logic = Logic(SERIAL_PORT)
logic.initialize()

class Server(SimpleHTTPServer.SimpleHTTPRequestHandler):
    '''
    Class for HTTP server functions
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
        

server = Server
httpd = SocketServer.TCPServer(('', SERVER_PORT), server)

print 'Scorclaw listening at port ' + str(SERVER_PORT)
httpd.serve_forever()    