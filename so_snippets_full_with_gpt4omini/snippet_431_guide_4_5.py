import subprocess # pragma: no cover

def execute_command(command): # pragma: no cover
    return subprocess.run(command, capture_output=True, text=True) # pragma: no cover
result = execute_command(['pip3', '-V']) # pragma: no cover
output = result.stdout.strip() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/29980798/where-does-pip-install-its-packages
from l3.Runtime import _l_
pip3 -V
_l_(3248)

