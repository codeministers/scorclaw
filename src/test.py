from core import Core

core = Core('/dev/cu.PL2303-00002006')

core.open()


core.write('home')


'''core.write('open')
core.write('close')
core.write('speed 7')
core.write('here pos1')
core.write('shiftc pos1 by x 100')
core.write('move pos1')
core.write('shiftc pos1 by y -100')
core.write('move pos1')
core.write('shiftc pos1 by z 100')
core.write('move pos1')
core.write('shiftc pos1 by x 100')
core.write('move pos1')
core.write('shiftc pos1 by y -100')
core.write('move pos1')
core.write('shiftc pos1 by z 100')
core.write('move pos1')'''


'''core.write('defp pos1')
core.write('defp pos2')

core.write('speed 50')
core.write('move 0')

core.write('teach pos2')
core.write('14')
core.write('-2655')
core.write('2907')
core.write('-922')
core.write('-4')
core.write('move pos2')
core.write('here pos1')
core.write('speed 7')

core.write('shiftc pos2 by x 500')
core.write('shiftc pos2 by y -600')
core.write('move pos2')

core.write('shiftc pos2 by z -2000')
core.write('open')
core.write('move pos2')'''


'''core.write('speed 50')
core.write('close')
core.write('move pos1')'''


core.close()
