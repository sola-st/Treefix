pip3 = 'pip3' # pragma: no cover
V = '-V' # pragma: no cover

import subprocess # pragma: no cover

pip3 = 'pip3' # pragma: no cover
V = subprocess.run(['pip3', '--version'], capture_output=True, text=True).stdout.strip() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/29980798/where-does-pip-install-its-packages
from l3.Runtime import _l_
pip3 -V
_l_(15235)

