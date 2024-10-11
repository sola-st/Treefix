from typing import Callable, Dict, Set, Tuple, Union # pragma: no cover

endpoint = None # pragma: no cover
def _endpoint_from_view_func(view_func: Callable) -> str:# pragma: no cover
    return "example_endpoint" # pragma: no cover
def view_func(*args, **kwargs):# pragma: no cover
    pass# pragma: no cover
view_func.methods = {'GET', 'POST'}# pragma: no cover
view_func.required_methods = {'HEAD'} # pragma: no cover
options = {'methods': ['GET'], 'endpoint': None} # pragma: no cover
provide_automatic_options = None # pragma: no cover
self = type('Mock', (object,), {# pragma: no cover
    'url_rule_class': lambda rule, methods, **options: type('Rule', (object,), {})(),# pragma: no cover
    'url_map': type('MockMap', (object,), {'add': lambda self, rule: None})(),# pragma: no cover
    'view_functions': {}# pragma: no cover
})() # pragma: no cover
rule = type('Rule', (object,), {'provide_automatic_options': None})() # pragma: no cover

from typing import Callable, Dict, Set, Optional, Any # pragma: no cover
from types import SimpleNamespace # pragma: no cover

endpoint = None # pragma: no cover
def _endpoint_from_view_func(view_func: Callable[..., Any]) -> str:# pragma: no cover
    return 'mock_endpoint' # pragma: no cover
def view_func() -> None:# pragma: no cover
    pass# pragma: no cover
view_func.methods = {'GET', 'POST'}# pragma: no cover
view_func.required_methods = {'HEAD'} # pragma: no cover
options: Dict[str, Any] = {} # pragma: no cover
provide_automatic_options: Optional[bool] = None # pragma: no cover
class Mock:# pragma: no cover
    url_rule_class = lambda self, rule, *args, methods=None, **kwargs: SimpleNamespace(provide_automatic_options=None)# pragma: no cover
    url_map = SimpleNamespace(add=lambda rule: None)# pragma: no cover
    view_functions: Dict[str, Callable[..., Any]] = {} # pragma: no cover
self = Mock() # pragma: no cover
rule = SimpleNamespace() # pragma: no cover

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
