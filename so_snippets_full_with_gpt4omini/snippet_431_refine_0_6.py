pip3 = 'pip 21.2.4' # pragma: no cover
V = '21.2.4' # pragma: no cover

pip3 = 'pip' # pragma: no cover
version = subprocess.check_output([pip3, '--version']).decode('utf-8').strip() # pragma: no cover
V = version # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/29980798/where-does-pip-install-its-packages
from l3.Runtime import _l_
pip3 -V
_l_(3248)

