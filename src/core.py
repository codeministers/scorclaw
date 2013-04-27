# -*- coding: utf-8 -*-
'''
Created on 26/04/2013

@author: José M. Camacho - camachososa@josemazocom
@author: Gabriel E. Muñoz - munozrios22@gmail.com
'''

'''
The Core class contains the basic methods for
communicate with SCORBOT or any serial device.
'''


import serial
import atexit


class Core:
    
    
    def __init__(self, serial_port):
        self.serial_port = serial_port
        self.serial = ''
        
    
    def open_con(self):
        self.serial = serial.Serial(port = self.serial_port)
        atexit.register(self.close_con)
        
    
    def close_con(self):
        self.serial.close()
        
    
    def write(self, command):
        self.serial.write(command + '\r')
        print '******************************'
        print '***Command sent:'
        print command
        print '***Command response:'
        
        response = ''
        while 1:
            data = self.serial.read(1)
            response += data
            
            if data == '>':
                break
        
        print response
        
    