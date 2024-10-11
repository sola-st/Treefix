# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/3277503/how-to-read-a-file-line-by-line-into-a-list
from l3.Runtime import _l_
try:
    import numpy as np
    _l_(14438)

except ImportError:
    pass
data = np.genfromtxt("yourfile.dat",delimiter="\n")
_l_(14439)

