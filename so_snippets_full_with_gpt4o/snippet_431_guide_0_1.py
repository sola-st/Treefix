import subprocess # pragma: no cover

version_info = subprocess.run(['pip3', '-V'], capture_output=True, text=True).stdout.strip() # pragma: no cover
print(version_info) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/29980798/where-does-pip-install-its-packages
from l3.Runtime import _l_
pip3 -V
_l_(15235)

