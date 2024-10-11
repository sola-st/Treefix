pip3 = 'pip 21.0.1' # pragma: no cover
V = '21.0.1' # pragma: no cover

class MockPip:# pragma: no cover
    def __init__(self, version):# pragma: no cover
        self.version = version# pragma: no cover
    def version_info(self):# pragma: no cover
        return self.version# pragma: no cover
pip3 = MockPip('21.0.1') # pragma: no cover
V = pip3.version_info() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/29980798/where-does-pip-install-its-packages
from l3.Runtime import _l_
pip3 -V
_l_(3248)

