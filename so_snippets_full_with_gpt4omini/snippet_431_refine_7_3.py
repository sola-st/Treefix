pip3 = 'pip 22.0.4' # pragma: no cover
V = '22.0.4' # pragma: no cover

class MockPip: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.version = '21.3.4' # pragma: no cover
    def __str__(self): # pragma: no cover
        return f'pip {self.version}' # pragma: no cover
pip3 = MockPip() # pragma: no cover
V = str(pip3) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/29980798/where-does-pip-install-its-packages
from l3.Runtime import _l_
pip3 -V
_l_(3248)

