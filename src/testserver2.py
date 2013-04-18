import SimpleHTTPServer
import SocketServer
import re

class ServerHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

    def do_GET(self):
        print '********************'
        
        path = self.path
        pathSplitted = re.split('/', path)
        
        respond = True
        response = ''
        
        if len(pathSplitted) == 2 and pathSplitted[1] != '':
            verb = pathSplitted[1]
            
            print verb
            if verb == 'more_x':
                response = 'more x done'
            elif verb == 'less_x':
                response = 'less x done'
            elif verb == 'more y':
                response = 'more y done'
            elif verb == 'less y':
                response = 'less y done'
            elif verb == 'catch':
                response = 'catch done'
            elif verb == 'home':
                response = 'home done'
            elif verb == 'canIMove':
                response = 'yesYouCan'
            else:
                respond = False
                print 'Unrecognized verb'
            
        else:
            respond = False
            print 'Not a valid request (' + path + ')'
        
        if respond:
            self.send_response(200)
            self.send_header('Content-type','application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write('{"response": "' + response + '"}')
        else:
            self.send_response(404)
            self.send_header('Content-type','application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write('{"response": "Not a valid path"}')

PORT = 8080

handler = ServerHandler
httpd = SocketServer.TCPServer(('', PORT), handler)

print 'serving at port', PORT
httpd.serve_forever()