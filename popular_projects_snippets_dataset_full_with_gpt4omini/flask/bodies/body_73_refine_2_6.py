from typing import List, Optional # pragma: no cover

class MockBlueprint:  # Creates a mock class to simulate blueprint behavior# pragma: no cover
    def __init__(self, name: Optional[str]):# pragma: no cover
        self.name = name# pragma: no cover
# pragma: no cover
self = type('Mock', (object,), {'blueprint': MockBlueprint('example_blueprint')})() # pragma: no cover
def _split_blueprint_path(name: str) -> List[str]:  # Mock implementation of the function# pragma: no cover
    return name.split('/')  # Simulates splitting the blueprint path # pragma: no cover

from typing import List, Optional # pragma: no cover

class Mock:  # Creates a mock class to simulate blueprint behavior# pragma: no cover
    blueprint: Optional[str] = 'example.blueprint.path' # pragma: no cover
self = Mock() # pragma: no cover
def _split_blueprint_path(name: str) -> List[str]:  # Mock implementation of the function# pragma: no cover
    return name.split('.')  # Correctly splits by '.' to match the original intent # pragma: no cover

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
