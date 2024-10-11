import numpy as np # pragma: no cover
import sys # pragma: no cover

sys.modules['numpy'] = type('Mock', (object,), {'loadtxt': lambda filepath, delimiter, skiprows: [['a', 'b'], ['c', 'd']]})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/3518778/how-do-i-read-csv-data-into-a-record-array-in-numpy
from l3.Runtime import _l_
try:
    import numpy as np
    _l_(397)

except ImportError:
    pass
data = np.loadtxt('c:\\1.csv',delimiter=',',skiprows=0)  
_l_(398)  

