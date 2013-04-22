import time

from functions import Functions


class Logic:
    '''
    classdocs
    
    Mejorar todo de esta clase
    Constantes, variables globales, metodos, ...
    Tambien la "union" entre esta clase y la Functions
    '''
    
    PITCH = -933
    ROLL = -6
    Z = 1864
    
    MIN_X = -700
    MAX_X = 900
    MIN_Y = -3100
    MAX_Y = -910
    
    INI_X = 97
    INI_Y = -1959
    
    END_X = 97
    END_Y = -3683
    
    INTERVAL = 100
    
    def __init__(self, serial_port):
        '''
        Constructor
        '''
        self.scorbot = Functions(serial_port)
        self.pos_ini = 'ini'
        self.pos_end = 'end'
        self.pos_user = 'user'
        self.current_x = 97
        self.current_y = -1959
        
    
    def close_con(self):
        self.scorbot.close_con()
        
    
    def fast(self):
        self.scorbot.speed(50)
        
    def medium(self):
        self.scorbot.speed(20)
        
        
    def slow(self):
        self.scorbot.speed(7)
        
    
    def initialize(self):
        '''
        Mejorar esta funcion
        '''
        self.scorbot.open_con()
        self.scorbot.home()
        
        self.scorbot.def_pos(self.pos_ini, self.pos_end, self.pos_user)
        
        self.scorbot.teach_pos(self.pos_ini, Logic.INI_X, Logic.INI_Y, Logic.Z, Logic.PITCH, Logic.ROLL)
        self.scorbot.teach_pos(self.pos_end, Logic.END_X, Logic.END_Y, Logic.Z, Logic.PITCH, Logic.ROLL)
        
        self.fast()
        self.scorbot.move(self.pos_ini)
        
        self.scorbot.open()
        self.slow()
        self.scorbot.setp(self.pos_user, self.pos_ini)
        
    
    def calculate_z(self, y):
        '''
        pos     y        z
        fin     -3683    224
        miny    -3064    265
        cen     -1959    522
        maxy    -913     845
        
        (-3683, 224) - (-913, 845) = [-2770, -621] = V
        N = [-621, 2770]
        -621(y + 913) + 2770 (z - 845) = 0
        -621y - 566973 + 2770z - 2340650 = 0
        -621y + 2770z - 2907623 = 0
        
        En los puntos centrales hay un error de casi 1cm,
        asi que se le baja medio centrimetro a todo
        '''
        return ((2907623 + (621 * y)) / 2770) - 50
        
    
    def update_x_y(self, x = None, y = None):
        if x != None:
            self.current_x = x
        if y != None:
            self.current_y = y
        
    
    def more_x(self):
        if self.current_x + Logic.INTERVAL <= Logic.MAX_X:
            self.update_x_y(self.current_x + Logic.INTERVAL, None)
            self.scorbot.set_x(self.pos_user, self.current_x)
            self.scorbot.move(self.pos_user)
        else:
            print 'more_x maximo: ' + str(self.current_x)
        
    
    def less_x(self):
        if self.current_x - Logic.INTERVAL >= Logic.MIN_X:
            self.update_x_y(self.current_x - Logic.INTERVAL, None)
            self.scorbot.set_x(self.pos_user, self.current_x)
            self.scorbot.move(self.pos_user)
        else:
            print 'less_x minimo: ' + str(self.current_x)
        
    
    def more_y(self):
        if self.current_y + Logic.INTERVAL <= Logic.MAX_Y:
            self.update_x_y(None, self.current_y + Logic.INTERVAL)
            self.scorbot.set_y(self.pos_user, self.current_y)
            self.scorbot.move(self.pos_user)
        else:
            print 'more_y maximo: ' + str(self.current_y)
        
    
    def less_y(self):
        if self.current_y - Logic.INTERVAL >= Logic.MIN_Y:
            self.update_x_y(None, self.current_y - Logic.INTERVAL)
            self.scorbot.set_y(self.pos_user, self.current_y)
            self.scorbot.move(self.pos_user)
        else:
            print 'less_y minimo: ' + str(self.current_y)
        
    
    def home(self):
        self.medium()
        self.update_x_y(Logic.INI_X, Logic.INI_Y)
        self.scorbot.move(self.pos_ini)
        self.scorbot.setp(self.pos_user, self.pos_ini)
        self.slow()
        
    
    def catch(self):
        '''
        Mejorar esta funcion
        '''
        z = self.calculate_z(self.current_y)
        self.scorbot.set_z(self.pos_user, z)
        
        self.fast()
        self.scorbot.move(self.pos_user)
        
        time.sleep(1)
        self.scorbot.close()
        self.scorbot.set_z(self.pos_user, Logic.Z)
        self.scorbot.move(self.pos_user)
        
        self.update_x_y(Logic.END_X, Logic.END_Y)
        self.scorbot.move(self.pos_end)
        
        z = self.calculate_z(self.current_y)
        self.scorbot.setp(self.pos_user, self.pos_end)
        self.scorbot.set_z(self.pos_user, z)
        self.scorbot.move(self.pos_user)
        
        time.sleep(4)
        self.scorbot.open()
        self.scorbot.set_z(self.pos_user, Logic.Z)
        self.scorbot.move(self.pos_user)
        self.scorbot.move(self.pos_ini)
        self.update_x_y(Logic.INI_X, Logic.INI_Y)
        self.scorbot.setp(self.pos_user, self.pos_ini)
        
        self.slow()
        
    