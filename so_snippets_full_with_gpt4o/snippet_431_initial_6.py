pip3 = "pip 20.2.4 from /usr/lib/python3/dist-packages/pip (python 3.8)" # pragma: no cover
V = "20.2.4" # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/29980798/where-does-pip-install-its-packages
from l3.Runtime import _l_
pip3 -V
_l_(15235)

