# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/1987694/how-do-i-print-the-full-numpy-array-without-truncation
from l3.Runtime import _l_
try:
    import numpy as np
    _l_(13938)

except ImportError:
    pass
print(str(np.arange(10000).reshape(250,40).tolist()))
_l_(13939)

