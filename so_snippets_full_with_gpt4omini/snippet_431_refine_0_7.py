pip3 = 'pip 21.2.4' # pragma: no cover
V = '21.2.4' # pragma: no cover

pip3 = 'pip' # pragma: no cover
V = subprocess.run([pip3, '-V'], capture_output=True, text=True).stdout.strip() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/29980798/where-does-pip-install-its-packages
from l3.Runtime import _l_
pip3 -V
_l_(3248)

