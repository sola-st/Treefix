pip3 = 'pip 21.0.1 from /usr/local/lib/python3.9/site-packages (python 3.9)' # pragma: no cover
V = pip3.split()[1] # pragma: no cover

import subprocess # pragma: no cover

pip3 = subprocess.check_output(['pip3', '--version']).decode('utf-8').strip() # pragma: no cover
V = pip3.split()[1] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/29980798/where-does-pip-install-its-packages
from l3.Runtime import _l_
pip3 -V
_l_(15235)

