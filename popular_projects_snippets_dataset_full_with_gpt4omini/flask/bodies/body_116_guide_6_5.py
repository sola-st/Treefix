from flask import Flask # pragma: no cover

app = Flask(__name__) # pragma: no cover
view_func = type('MockViewFunc', (object,), {'methods': None, 'required_methods': [], 'provide_automatic_options': None})() # pragma: no cover
endpoint = None # pragma: no cover
options = {'methods': None} # pragma: no cover
provide_automatic_options = None # pragma: no cover
self = type('Mock', (object,), {'url_rule_class': lambda rule, methods, **kwargs: {'rule': rule, 'methods': methods}, 'url_map': type('MockMap', (object,), {'add': lambda self, rule: None})(), 'view_functions': {}})() # pragma: no cover
_endpoint_from_view_func = lambda func: 'mock_endpoint' # pragma: no cover
methods = None # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/app.py
from l3.Runtime import _l_
if endpoint is None:
    _l_(6629)

    endpoint = _endpoint_from_view_func(view_func)  # type: ignore
    _l_(6628)  # type: ignore
options["endpoint"] = endpoint
_l_(6630)
methods = options.pop("methods", None)
_l_(6631)

# if the methods are not given and the view_func object knows its
# methods we can use that instead.  If neither exists, we go with
# a tuple of only ``GET`` as default.
if methods is None:
    _l_(6633)

    methods = getattr(view_func, "methods", None) or ("GET",)
    _l_(6632)
if isinstance(methods, str):
    _l_(6635)

    raise TypeError(
        "Allowed methods must be a list of strings, for"
        ' example: @app.route(..., methods=["POST"])'
    )
    _l_(6634)
methods = {item.upper() for item in methods}
_l_(6636)

# Methods that should always be added
required_methods = set(getattr(view_func, "required_methods", ()))
_l_(6637)

# starting with Flask 0.8 the view_func object can disable and
# force-enable the automatic options handling.
if provide_automatic_options is None:
    _l_(6639)

    provide_automatic_options = getattr(
        view_func, "provide_automatic_options", None
    )
    _l_(6638)

if provide_automatic_options is None:
    _l_(6644)

    if "OPTIONS" not in methods:
        _l_(6643)

        provide_automatic_options = True
        _l_(6640)
        required_methods.add("OPTIONS")
        _l_(6641)
    else:
        provide_automatic_options = False
        _l_(6642)

        # Add the required methods now.
methods |= required_methods
_l_(6645)

rule = self.url_rule_class(rule, methods=methods, **options)
_l_(6646)
rule.provide_automatic_options = provide_automatic_options  # type: ignore
_l_(6647)  # type: ignore

self.url_map.add(rule)
_l_(6648)
if view_func is not None:
    _l_(6653)

    old_func = self.view_functions.get(endpoint)
    _l_(6649)
    if old_func is not None and old_func != view_func:
        _l_(6651)

        raise AssertionError(
            "View function mapping is overwriting an existing"
            f" endpoint function: {endpoint}"
        )
        _l_(6650)
    self.view_functions[endpoint] = view_func
    _l_(6652)
