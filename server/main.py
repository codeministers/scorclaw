# -*- coding: utf-8 -*-
'''
Created on 26/04/2013

@author: José M. Camacho - camachososa@josemazocom
@author: Gabriel E. Muñoz - munozrios22@gmail.com
'''

'''
The main module will check the parameters
for obtain the port for the server and the
name of the serial port.

After that, the server will be created.
'''


import sys
import SocketServer


if len(sys.argv) != 3:
    print 'Incorrect number of arguments'
    print 'The program expected the port for the server and the name of the serial port as arguments'
    print 'Examples:'
    print '- Linux: python main.py 8080 /dev/ttyS1'
    print '- Mac OS: python main.py 8080 /dev/cu.PL2303-00002006'
    print '- Windows: python main.py 8080 COM3'
    
else:
    import variables
    variables.SERVER_PORT = int(sys.argv[1])
    variables.SERIAL_PORT = sys.argv[2]
    
    from requests import Requests
    httpd = SocketServer.TCPServer(('', variables.SERVER_PORT), Requests)
    
    print 'ScorClaw listening at port ' + str(variables.SERVER_PORT)
    httpd.serve_forever()
    
