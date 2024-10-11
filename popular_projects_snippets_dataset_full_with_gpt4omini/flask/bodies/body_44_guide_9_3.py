from typing import Callable, TypeVar # pragma: no cover

T_template_filter = TypeVar('T_template_filter', bound=Callable) # pragma: no cover
class MockApp:  # Mock class to simulate a Flask application# pragma: no cover
    def add_app_template_filter(self, f, name=None): print(f'Filter {name} added.') # pragma: no cover
self = MockApp() # pragma: no cover
name = 'test_filter' # pragma: no cover
decorator = lambda f: (self.add_app_template_filter(f, name=name), f)[1] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/blueprints.py
from l3.Runtime import _l_
"""Register a custom template filter, available application wide.  Like
        :meth:`Flask.template_filter` but for a blueprint.

        :param name: the optional name of the filter, otherwise the
                     function name will be used.
        """

def decorator(f: T_template_filter) -> T_template_filter:
    _l_(4155)

    self.add_app_template_filter(f, name=name)
    _l_(4153)
    aux = f
    _l_(4154)
    exit(aux)
aux = decorator
_l_(4156)

exit(aux)
