# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/3781851/run-a-python-script-from-another-python-script-passing-in-arguments
from l3.Runtime import _l_
try:
    import subprocess
    _l_(13754)

except ImportError:
    pass
subprocess.call(" python script2.py 1", shell=True)
_l_(13755)

