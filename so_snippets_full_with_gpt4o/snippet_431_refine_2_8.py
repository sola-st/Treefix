pip3 = 'pip 21.0.1 from /usr/lib/python3.8/site-packages/pip (python 3.8)' # pragma: no cover
V = '21.0.1' # pragma: no cover

import subprocess # pragma: no cover

pip3 = subprocess.run # pragma: no cover
V = ['pip3', '--version'] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/29980798/where-does-pip-install-its-packages
from l3.Runtime import _l_
pip3 -V
_l_(15235)

