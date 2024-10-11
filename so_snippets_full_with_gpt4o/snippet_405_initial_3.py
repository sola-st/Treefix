default_path = '/home/user/default_path' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/1810743/how-to-set-the-current-working-directory
from l3.Runtime import _l_
try:
    import os
    _l_(11836)

except ImportError:
    pass
os.chdir(default_path)
_l_(11837)

