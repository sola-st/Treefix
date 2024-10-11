from typing import Callable, Dict # pragma: no cover

options = {'endpoint': 'index', 'methods': ['GET']} # pragma: no cover
rule = '/' # pragma: no cover
class MockApp:  # pragma: no cover
    pass
self = MockApp() # pragma: no cover
T_route = Callable[[None], str] # pragma: no cover
def index(): return 'Hello, World!' # pragma: no cover
def decorator(f: T_route) -> T_route:  # pragma: no cover
    endpoint = options.pop('endpoint', None)  # pragma: no cover
    self.add_url_rule(rule, endpoint, f, **options)  # pragma: no cover
    aux = f  # pragma: no cover

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
    _l_(6428)

    endpoint = options.pop("endpoint", None)
    _l_(6425)
    self.add_url_rule(rule, endpoint, f, **options)
    _l_(6426)
    aux = f
    _l_(6427)
    exit(aux)
aux = decorator
_l_(6429)

exit(aux)
