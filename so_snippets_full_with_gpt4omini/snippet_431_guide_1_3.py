import subprocess # pragma: no cover

subprocess.run = lambda cmd, shell=False, capture_output=False, text=False: type('Mock', (object,), {'stdout': b'pip 21.1.2 from /usr/local/lib/python3.8/site-packages/pip (python 3.8)', 'stderr': b''})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/29980798/where-does-pip-install-its-packages
from l3.Runtime import _l_
pip3 -V
_l_(3248)

