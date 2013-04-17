import serial

class Core:
    '''
    Scorbot core functions
    '''
    
    def __init__(self, port_name):
        self.port_name = port_name
        self.serial = ''
        
    def open(self):
        self.serial = serial.Serial(port = self.port_name)
 
    def close(self):
        self.serial.close()
    
    def write(self, command):
        self.serial.write(command + '\r')
        print '******************************'
        print '***Command send:'
        print command
        print '***Command response:'
        
        response = ''
        while 1:
            data = self.serial.read(1)
            response += data
            
            if data == '>':
                break
        
        print response
