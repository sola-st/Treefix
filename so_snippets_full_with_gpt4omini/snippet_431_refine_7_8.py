pip3 = 'pip 22.0.4' # pragma: no cover
V = '22.0.4' # pragma: no cover

pip3 = None # pragma: no cover
V = None # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/29980798/where-does-pip-install-its-packages
from l3.Runtime import _l_
pip3 -V
_l_(3248)

