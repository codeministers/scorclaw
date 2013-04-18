import SocketServer

from server2 import Server


SERVER_PORT = 8080
SERIAL_PORT = '/dev/cu.PL2303-00002006'

server = Server
httpd = SocketServer.TCPServer(('', SERVER_PORT), server, SERIAL_PORT)

print 'Scorclaw listening at port ' + str(SERVER_PORT)
httpd.serve_forever()