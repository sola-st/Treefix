import os # pragma: no cover
import sys # pragma: no cover

if 'pip' not in sys.modules: # pragma: no cover
    os.system('pip3 -V') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/29980798/where-does-pip-install-its-packages
from l3.Runtime import _l_
pip3 -V
_l_(15235)

