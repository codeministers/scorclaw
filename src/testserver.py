# Server.py - Example server to manage Scorbot robot
# The pattern for use the commands is "/send/{command1}/{command2}..."
# Requirements: pyserial module installed

import SimpleHTTPServer
import SocketServer
#import logging
#import cgi
import re

import serial

PORT = 8000

ser = serial.Serial(
    port='COM4'
)

class ServerHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

    def do_GET(self):
        #logging.error(self.headers)
        res = self.path
        print "User request: " + res
        result = re.split('/', res)
        comp = result[1]
        if comp == 'send' :
            i = 3
            cadena = result[2]
            while i < len(result) :
                cadena += ' ' + result[i]
                i = i + 1
            # Serial port treatment
        print cadena
        ser.write(cadena + '\r')
        print 'OK!'
        SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

Handler = ServerHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()