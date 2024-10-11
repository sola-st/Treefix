import sys # pragma: no cover

sys.modules['matplotlib'] = type('Mock', (object,), {'rcParams': {}})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/6390393/matplotlib-make-tick-labels-font-size-smaller
from l3.Runtime import _l_
try:
    import matplotlib as mpl
    _l_(1164)

except ImportError:
    pass
label_size = 8
_l_(1165)
mpl.rcParams['xtick.labelsize'] = label_size 
_l_(1166) 

