import subprocess # pragma: no cover

def get_pip_version(): # pragma: no cover
    result = subprocess.run(['pip3', '-V'], capture_output=True, text=True) # pragma: no cover
    return result.stdout.strip() # pragma: no cover
 # pragma: no cover
pip_version = get_pip_version() # pragma: no cover
print(pip_version) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/29980798/where-does-pip-install-its-packages
from l3.Runtime import _l_
pip3 -V
_l_(15235)

