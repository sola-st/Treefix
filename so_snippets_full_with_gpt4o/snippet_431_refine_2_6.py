pip3 = 'pip 21.0.1 from /usr/lib/python3.8/site-packages/pip (python 3.8)' # pragma: no cover
V = '21.0.1' # pragma: no cover

import subprocess # pragma: no cover

pip3 = 'pip3' # pragma: no cover
V = '-V' # pragma: no cover
command = [pip3, V] # pragma: no cover
output = subprocess.run(command, capture_output=True, text=True).stdout # pragma: no cover
print(output) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/29980798/where-does-pip-install-its-packages
from l3.Runtime import _l_
pip3 -V
_l_(15235)

