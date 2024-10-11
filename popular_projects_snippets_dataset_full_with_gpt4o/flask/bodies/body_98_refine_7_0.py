import os # pragma: no cover

os.path = type('Mock', (object,), {'join': lambda *args: '/'.join(args)}) # pragma: no cover

import os # pragma: no cover

    return None, '/path/to/package' # pragma: no cover
 # pragma: no cover
self = type('Mock', (object,), { # pragma: no cover
    'name': 'my_application' # pragma: no cover
})() # pragma: no cover
 # pragma: no cover
os.path = type('Mock', (object,), { # pragma: no cover
    'join': staticmethod(lambda *args: '/'.join(args)) # pragma: no cover
}) # pragma: no cover

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
_l_(22795)
if prefix is None:
    _l_(22797)

    aux = os.path.join(package_path, "instance")
    _l_(22796)
    exit(aux)
aux = os.path.join(prefix, "var", f"{self.name}-instance")
_l_(22798)
exit(aux)
