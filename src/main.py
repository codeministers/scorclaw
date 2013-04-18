import SocketServer

from server import Server


SERVER_PORT = 8080
SERIAL_PORT = '/dev/cu.PL2303-00002006'

server = Server(SERIAL_PORT)
httpd = SocketServer.TCPServer(('', SERVER_PORT), server)

print 'serving at port', SERVER_PORT
httpd.serve_forever()