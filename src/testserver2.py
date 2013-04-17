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
            if verb == 'up':
                response = 'upped'
            elif verb == 'down':
                response = 'downed'
            elif verb == 'left':
                response = 'lefted'
            elif verb == 'right':
                response = 'righted'
            elif verb == 'catch':
                response = 'catched'
            elif verb == 'home':
                response = 'homed'
            elif verb == 'canIMove':
                response = 'yesYouCan'
            else:
                respond = False
                print 'Unrecognized verb'
            
        else:
            respond = False
            print 'Not a valid request (' + path + ')'
        
        if respond:
            #self.send_response(200)
            #self.send_header('Content-type','application/json')
            #self.end_headers()
            self.wfile.write('{"response": "' + response + '"}')
        else:
            #self.send_response(404)
            #self.send_header('Content-type','text-html')
            #self.end_headers()
            self.wfile.write('{"response": "Not a valid path"}')

PORT = 8080

handler = ServerHandler
httpd = SocketServer.TCPServer(('', PORT), handler)

print 'serving at port', PORT
httpd.serve_forever()