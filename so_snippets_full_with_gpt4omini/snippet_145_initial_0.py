import os # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/3430372/how-do-i-get-the-full-path-of-the-current-files-directory
from l3.Runtime import _l_
try:
    import os
    _l_(540)

except ImportError:
    pass
print(os.path.dirname(__file__))
_l_(541)

