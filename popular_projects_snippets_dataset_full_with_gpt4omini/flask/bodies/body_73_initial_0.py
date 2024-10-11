from typing import List # pragma: no cover

class Mock: pass # pragma: no cover
self = Mock() # pragma: no cover
self.blueprint = 'example.blueprint.path' # pragma: no cover
_split_blueprint_path = lambda name: name.split('.') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/wrappers.py
from l3.Runtime import _l_
"""The registered names of the current blueprint upwards through
        parent blueprints.

        This will be an empty list if there is no current blueprint, or
        if URL matching failed.

        .. versionadded:: 2.0.1
        """
name = self.blueprint
_l_(7021)

if name is None:
    _l_(7023)

    aux = []
    _l_(7022)
    exit(aux)
aux = _split_blueprint_path(name)
_l_(7024)

exit(aux)
