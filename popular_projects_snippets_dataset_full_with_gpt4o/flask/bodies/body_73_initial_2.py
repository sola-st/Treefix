import sys # pragma: no cover

class Mock(object): # pragma: no cover
    def __init__(self, blueprint): # pragma: no cover
        self.blueprint = blueprint # pragma: no cover
 # pragma: no cover
def _split_blueprint_path(name): # pragma: no cover
    return name.split('.') # pragma: no cover
 # pragma: no cover
self = Mock('example.blueprint.path') # pragma: no cover

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
_l_(22758)

if name is None:
    _l_(22760)

    aux = []
    _l_(22759)
    exit(aux)
aux = _split_blueprint_path(name)
_l_(22761)

exit(aux)
