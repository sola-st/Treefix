from typing import Callable, TypeVar # pragma: no cover
import sys # pragma: no cover

T_template_filter = TypeVar('T_template_filter', bound=Callable) # pragma: no cover
name = 'custom_filter' # pragma: no cover
class BlueprintMock(object): # pragma: no cover
    def add_app_template_filter(self, f: Callable, name: str = None) -> None: # pragma: no cover
        pass # pragma: no cover
self = type('Mock', (BlueprintMock,), {})() # pragma: no cover

from typing import Callable, TypeVar # pragma: no cover

T_template_filter = TypeVar('T_template_filter', bound=Callable) # pragma: no cover
name = 'custom_filter' # pragma: no cover
class BlueprintMock(object): # pragma: no cover
    def add_app_template_filter(self, f: Callable, name: str = None) -> None: # pragma: no cover
        pass # pragma: no cover
self = BlueprintMock() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/blueprints.py
from l3.Runtime import _l_
"""Register a custom template filter, available application wide.  Like
        :meth:`Flask.template_filter` but for a blueprint.

        :param name: the optional name of the filter, otherwise the
                     function name will be used.
        """

def decorator(f: T_template_filter) -> T_template_filter:
    _l_(15715)

    self.add_app_template_filter(f, name=name)
    _l_(15713)
    aux = f
    _l_(15714)
    exit(aux)
aux = decorator
_l_(15716)

exit(aux)
