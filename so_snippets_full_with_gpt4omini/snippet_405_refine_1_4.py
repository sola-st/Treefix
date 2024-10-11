import os # pragma: no cover

default_path = '/home/user/projects' # pragma: no cover

import os # pragma: no cover

default_path = os.path.join(os.getcwd(), 'existing_directory') # pragma: no cover

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

