pip3 = 'pip 21.1.2' # pragma: no cover
V = '21.1.2' # pragma: no cover

class Pip3Mock: # pragma: no cover
    def __init__(self, version): # pragma: no cover
        self.version = version # pragma: no cover
 # pragma: no cover
    def V(self): # pragma: no cover
        return self.version # pragma: no cover
 # pragma: no cover
pip3 = Pip3Mock('21.1.2') # pragma: no cover
V = pip3.V() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/29980798/where-does-pip-install-its-packages
from l3.Runtime import _l_
pip3 -V
_l_(15235)

