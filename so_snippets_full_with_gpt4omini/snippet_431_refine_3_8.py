pip3 = 'pip 21.1.2' # pragma: no cover
V = '21.1.2' # pragma: no cover

def mock_pip_version(): return 'pip 21.1.2' # pragma: no cover
pip3 = mock_pip_version() # pragma: no cover
V = '21.1.2' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/29980798/where-does-pip-install-its-packages
from l3.Runtime import _l_
pip3 -V
_l_(3248)

