# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/39980323/are-dictionaries-ordered-in-python-3-6
from l3.Runtime import _l_
d = {'timmy': 'red', 'barry': 'green', 'guido': 'blue'}
_l_(1639)

entries = [['--', '--', '--'],
           [-8522787127447073495, 'barry', 'green'],
           ['--', '--', '--'],
           ['--', '--', '--'],
           ['--', '--', '--'],
           [-9092791511155847987, 'timmy', 'red'],
           ['--', '--', '--'],
           [-6480567542315338377, 'guido', 'blue']]
_l_(1640)

indices =  [None, 1, None, None, None, 0, None, 2]
_l_(1641)
entries =  [[-9092791511155847987, 'timmy', 'red'],
            [-8522787127447073495, 'barry', 'green'],
            [-6480567542315338377, 'guido', 'blue']]
_l_(1642)

