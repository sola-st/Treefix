import subprocess # pragma: no cover

def run_command(command): return subprocess.run(command, shell=True, text=True, capture_output=True) # pragma: no cover
result = run_command('pip3 -V') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/29980798/where-does-pip-install-its-packages
from l3.Runtime import _l_
pip3 -V
_l_(3248)

