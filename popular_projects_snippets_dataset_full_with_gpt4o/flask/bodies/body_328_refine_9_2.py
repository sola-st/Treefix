from typing import Callable, Dict, TypeVar # pragma: no cover
import werkzeug.routing # pragma: no cover

T_route = TypeVar('T_route', bound=Callable) # pragma: no cover
rule = '/' # pragma: no cover
self = type('Mock', (object,), {'add_url_rule': lambda self, rule, endpoint, f, **options: None})() # pragma: no cover

from typing import Callable, Dict, Any, TypeVar # pragma: no cover

T_route = TypeVar('T_route', bound=Callable) # pragma: no cover
options: Dict[str, Any] = {'endpoint': None} # pragma: no cover
rule = '/' # pragma: no cover
self = type('Mock', (object,), {'add_url_rule': lambda self, rule, endpoint, f, **options: None})() # pragma: no cover

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
