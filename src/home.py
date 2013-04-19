from functions import Functions

f = Functions('/dev/cu.PL2303-00002006')
f.open_con()
f.home()
f.close_con()