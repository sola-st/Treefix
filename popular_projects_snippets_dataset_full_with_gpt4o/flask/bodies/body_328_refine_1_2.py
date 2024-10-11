from typing import Callable, Dict # pragma: no cover
from dataclasses import dataclass, field # pragma: no cover

T_route = Callable # pragma: no cover
options: Dict[str, any] = {'endpoint': 'example_endpoint'} # pragma: no cover
rule = '/' # pragma: no cover
@dataclass# pragma: no cover
class MockApp:# pragma: no cover
    def add_url_rule(self, rule: str, endpoint: str, func: Callable, **options):# pragma: no cover
        print(f'URL rule added: rule={rule}, endpoint={endpoint}, func={func.__name__}, options={options}')# pragma: no cover
self = MockApp() # pragma: no cover

from typing import Any, Callable, Dict, TypeVar # pragma: no cover

T_route = TypeVar('T_route', bound=Callable[..., Any]) # pragma: no cover
options: Dict[str, Any] = {'endpoint': 'example_endpoint'} # pragma: no cover
rule: str = '/' # pragma: no cover
self = type('Mock', (object,), {'add_url_rule': lambda self, rule, endpoint, f, **options: print(f'add_url_rule called with rule={rule}, endpoint={endpoint}, f={f}, options={options}')})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/scaffold.py
from l3.Runtime import _l_
"""Decorate a view function to register it with the given URL
        rule and options. Calls :meth:`add_url_rule`, which has more
        details about the implementation.

        .. code-block:: python

            @app.route("/")
            def index():
                return "Hello, World!"

        See :ref:`url-route-registrations`.

        The endpoint name for the route defaults to the name of the view
        function if the ``endpoint`` parameter isn't passed.

        The ``methods`` parameter defaults to ``["GET"]``. ``HEAD`` and
        ``OPTIONS`` are added automatically.

        :param rule: The URL rule string.
        :param options: Extra options passed to the
            :class:`~werkzeug.routing.Rule` object.
        """

def decorator(f: T_route) -> T_route:
    _l_(17845)

    endpoint = options.pop("endpoint", None)
    _l_(17842)
    self.add_url_rule(rule, endpoint, f, **options)
    _l_(17843)
    aux = f
    _l_(17844)
    exit(aux)
aux = decorator
_l_(17846)

exit(aux)
