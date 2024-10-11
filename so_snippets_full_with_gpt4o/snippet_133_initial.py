# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/1093322/how-do-i-check-which-version-of-python-is-running-my-script
from l3.Runtime import _l_
try:
    import sys
    _l_(13180)

except ImportError:
    pass
current_version = ".".join(map(str, sys.version_info[0:2]))
_l_(13181)

