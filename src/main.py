import SocketServer

from variables import SERVER_PORT

from requests import Requests


httpd = SocketServer.TCPServer(('', SERVER_PORT), Requests)

print 'ScorClaw listening at port ' + str(SERVER_PORT)
httpd.serve_forever()

