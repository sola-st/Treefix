import os # pragma: no cover

default_path = '/path/to/directory' # pragma: no cover

import os # pragma: no cover

default_path = os.path.join(os.getcwd(), 'test_directory') # pragma: no cover
os.mkdir(default_path) if not os.path.exists(default_path) else None # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/1810743/how-to-set-the-current-working-directory
from l3.Runtime import _l_
try:
    import os
    _l_(33)

except ImportError:
    pass
os.chdir(default_path)
_l_(34)

