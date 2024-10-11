import os # pragma: no cover
from typing import Optional, Tuple # pragma: no cover

class MockApp:  # Mock class simulating an application # pragma: no cover
    def __init__(self): # pragma: no cover
        self.name = 'my_app' # pragma: no cover
 # pragma: no cover
    return (None, '/path/to/package')  # Simulating a case where prefix is None # pragma: no cover
 # pragma: no cover
self = MockApp() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/app.py
from l3.Runtime import _l_
"""Tries to locate the instance path if it was not provided to the
        constructor of the application class.  It will basically calculate
        the path to a folder named ``instance`` next to your main file or
        the package.

        .. versionadded:: 0.8
        """
prefix, package_path = find_package(self.import_name)
_l_(7496)
if prefix is None:
    _l_(7498)

    aux = os.path.join(package_path, "instance")
    _l_(7497)
    exit(aux)
aux = os.path.join(prefix, "var", f"{self.name}-instance")
_l_(7499)
exit(aux)
