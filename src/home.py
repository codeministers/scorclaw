# -*- coding: utf-8 -*-
'''
Created on 26/04/2013

@author: José M. Camacho - camachososa@josemazocom
@author: Gabriel E. Muñoz - munozrios22@gmail.com
'''

'''
Module to place the SCORBOT in the home position
'''


from functions import Functions


f = Functions('/dev/cu.PL2303-00002006')
f.open_con()
f.home()
f.close_con()