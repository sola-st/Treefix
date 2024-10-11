import subprocess # pragma: no cover

def mock_subprocess_check_output(*args, **kwargs): return 'pip 21.0.1 from /usr/local/lib/python3.8/site-packages/pip (python 3.8)' # pragma: no cover
subprocess.check_output = mock_subprocess_check_output # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/29980798/where-does-pip-install-its-packages
from l3.Runtime import _l_
pip3 -V
_l_(3248)

