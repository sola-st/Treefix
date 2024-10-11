import subprocess # pragma: no cover

def run_pip_version(): # pragma: no cover
    return subprocess.check_output(['pip3', '-V'], text=True).strip() # pragma: no cover
pip_version = run_pip_version() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/29980798/where-does-pip-install-its-packages
from l3.Runtime import _l_
pip3 -V
_l_(3248)

