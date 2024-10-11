import subprocess # pragma: no cover

subprocess.run = type('Mock', (object,), {'__call__': lambda self, cmd, shell: print(f'Executed command: {cmd}')})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/29980798/where-does-pip-install-its-packages
from l3.Runtime import _l_
pip3 -V
_l_(3248)

