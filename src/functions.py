from core import Core


class Functions:
    '''
    Class to abstract the Core class
    '''
    
    
    def __init__(self, serial_port):
        '''
        Constructor
        '''
        self.core = Core(serial_port)
    
    
    def open_con(self):
        self.core.open_con()
    
    
    def close_con(self):
        self.core.close_con()
    
    
    def home(self):
        self.core.write('home')
        
    
    def open(self):
        self.core.write('open')
    
    
    def close(self):
        self.core.write('close')
    
    
    def def_pos(self, *pos):
        for p in pos:
            self.core.write('defp ' + p)
    
    
    def teach_pos(self, pos, x, y, z, p, r):
        self.core.write('teach ' + pos)
        self.core.write(str(x))
        self.core.write(str(y))
        self.core.write(str(z))
        self.core.write(str(p))
        self.core.write(str(r))
    
    
    def speed(self, s):
        self.core.write('speed ' + str(s))
    
    
    def move(self, *pos):
        for p in pos:
            self.core.write('move ' + p)
    
    
    def here(self, *pos):
        for p in pos:
            self.core.write('here ' + p)
    
    
    def setp(self, pos1, pos2):
        self.core.write('setp ' + pos1 + ' = ' + pos2)
    
    
    def set_x(self, pos, value):
        self.core.write('setpvc ' + pos + ' x ' + str(value))
    
    
    def set_y(self, pos, value):
        self.core.write('setpvc ' + pos + ' y ' + str(value))
    
    
    def set_z(self, pos, value):
        self.core.write('setpvc ' + pos + ' z ' + str(value))