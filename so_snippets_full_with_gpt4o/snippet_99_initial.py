# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits
from l3.Runtime import _l_
try:
    import numpy as np
    _l_(12533)

except ImportError:
    pass
try:
    import string
    _l_(12535)

except ImportError:
    pass

if __name__ == '__main__':
    _l_(12539)

    length = 16
    _l_(12536)
    a = np.random.choice(list(string.ascii_uppercase + string.digits), length)                
    _l_(12537)                
    print(''.join(a))
    _l_(12538)

