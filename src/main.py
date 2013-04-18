import SocketServer

from server import Server


SERVER_PORT = 8080
SERIAL_PORT = '/dev/cu.PL2303-00002006'

server = Server(SERIAL_PORT)
httpd = SocketServer.TCPServer(('', SERVER_PORT), server)

print 'Scorclaw listening at port ' + str(SERVER_PORT)
httpd.serve_forever()