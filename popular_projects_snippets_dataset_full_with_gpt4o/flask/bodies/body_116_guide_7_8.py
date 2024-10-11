from werkzeug.routing import Rule, Map # pragma: no cover

def _endpoint_from_view_func(view_func): # pragma: no cover
    return 'mock_endpoint' # pragma: no cover
class MockViewFunc: # pragma: no cover
    methods = None # pragma: no cover
    required_methods = {'GET'} # pragma: no cover
    provide_automatic_options = None # pragma: no cover
view_func = MockViewFunc() # pragma: no cover
endpoint = None # pragma: no cover
rule = '/test' # pragma: no cover
options = {} # pragma: no cover
provide_automatic_options = None # pragma: no cover
class MockRule: # pragma: no cover
    def __init__(self, rule, methods=None, **options): # pragma: no cover
        self.rule = rule # pragma: no cover
        self.methods = methods # pragma: no cover
        self.options = options # pragma: no cover
        self.provide_automatic_options = None # pragma: no cover
class MockURLMap: # pragma: no cover
    def add(self, rule): # pragma: no cover
        pass # pragma: no cover
self = type('Mock', (object,), { # pragma: no cover
    'url_rule_class': MockRule, # pragma: no cover
    'url_map': MockURLMap(), # pragma: no cover
    'view_functions': {'mock_endpoint': lambda: 'old_function'} # pragma: no cover
})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/app.py
from l3.Runtime import _l_
if endpoint is None:
    _l_(22715)

    endpoint = _endpoint_from_view_func(view_func)  # type: ignore
    _l_(22714)  # type: ignore
options["endpoint"] = endpoint
_l_(22716)
methods = options.pop("methods", None)
_l_(22717)

# if the methods are not given and the view_func object knows its
# methods we can use that instead.  If neither exists, we go with
# a tuple of only ``GET`` as default.
if methods is None:
    _l_(22719)

    methods = getattr(view_func, "methods", None) or ("GET",)
    _l_(22718)
if isinstance(methods, str):
    _l_(22721)

    raise TypeError(
        "Allowed methods must be a list of strings, for"
        ' example: @app.route(..., methods=["POST"])'
    )
    _l_(22720)
methods = {item.upper() for item in methods}
_l_(22722)

# Methods that should always be added
required_methods = set(getattr(view_func, "required_methods", ()))
_l_(22723)

# starting with Flask 0.8 the view_func object can disable and
# force-enable the automatic options handling.
if provide_automatic_options is None:
    _l_(22725)

    provide_automatic_options = getattr(
        view_func, "provide_automatic_options", None
    )
    _l_(22724)

if provide_automatic_options is None:
    _l_(22730)

    if "OPTIONS" not in methods:
        _l_(22729)

        provide_automatic_options = True
        _l_(22726)
        required_methods.add("OPTIONS")
        _l_(22727)
    else:
        provide_automatic_options = False
        _l_(22728)

        # Add the required methods now.
methods |= required_methods
_l_(22731)

rule = self.url_rule_class(rule, methods=methods, **options)
_l_(22732)
rule.provide_automatic_options = provide_automatic_options  # type: ignore
_l_(22733)  # type: ignore

self.url_map.add(rule)
_l_(22734)
if view_func is not None:
    _l_(22739)

    old_func = self.view_functions.get(endpoint)
    _l_(22735)
    if old_func is not None and old_func != view_func:
        _l_(22737)

        raise AssertionError(
            "View function mapping is overwriting an existing"
            f" endpoint function: {endpoint}"
        )
        _l_(22736)
    self.view_functions[endpoint] = view_func
    _l_(22738)
