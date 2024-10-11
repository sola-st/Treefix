pip3 = 'pip 21.0.1 from /usr/lib/python3.9/site-packages/pip (python 3.9)' # pragma: no cover
V = '21.0.1' # pragma: no cover

pip3 = lambda: subprocess.run(['pip3', '--version'], capture_output=True, text=True).stdout.strip() # pragma: no cover
V = '--version' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/29980798/where-does-pip-install-its-packages
from l3.Runtime import _l_
pip3 -V
_l_(15235)

