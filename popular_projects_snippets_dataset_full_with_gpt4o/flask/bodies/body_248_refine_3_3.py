import ast # pragma: no cover
import inspect # pragma: no cover
from flask import Flask # pragma: no cover

app_name = 'my_function()' # pragma: no cover
class NoAppException(Exception):# pragma: no cover
    def __init__(self, message):# pragma: no cover
        super().__init__(message) # pragma: no cover
module = type('Mock', (object,), {'__name__': 'mock_module'})() # pragma: no cover
_called_with_wrong_args = lambda x: False # pragma: no cover

import ast # pragma: no cover
import inspect # pragma: no cover
from flask import Flask # pragma: no cover

app_name = 'my_function()' # pragma: no cover
class NoAppException(Exception):# pragma: no cover
    def __init__(self, message):# pragma: no cover
        super().__init__(message) # pragma: no cover
module = type('Mock', (object,), {'__name__': 'mock_module', 'my_function': lambda: Flask(__name__)})() # pragma: no cover
_called_with_wrong_args = lambda x: False # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/cli.py
from l3.Runtime import _l_
"""Check if the given string is a variable name or a function. Call
    a function to get the app instance, or return the variable directly.
    """
try:
    from . import Flask
    _l_(22840)

except ImportError:
    pass

# Parse app_name as a single expression to determine if it's a valid
# attribute name or function call.
try:
    _l_(22844)

    expr = ast.parse(app_name.strip(), mode="eval").body
    _l_(22841)
except SyntaxError:
    _l_(22843)

    raise NoAppException(
        f"Failed to parse {app_name!r} as an attribute name or function call."
    ) from None
    _l_(22842)

if isinstance(expr, ast.Name):
    _l_(22858)

    name = expr.id
    _l_(22845)
    args = []
    _l_(22846)
    kwargs = {}
    _l_(22847)
elif isinstance(expr, ast.Call):
    _l_(22857)

    # Ensure the function name is an attribute name only.
    if not isinstance(expr.func, ast.Name):
        _l_(22849)

        raise NoAppException(
            f"Function reference must be a simple name: {app_name!r}."
        )
        _l_(22848)

    name = expr.func.id
    _l_(22850)

    # Parse the positional and keyword arguments as literals.
    try:
        _l_(22855)

        args = [ast.literal_eval(arg) for arg in expr.args]
        _l_(22851)
        kwargs = {kw.arg: ast.literal_eval(kw.value) for kw in expr.keywords}
        _l_(22852)
    except ValueError:
        _l_(22854)

        # literal_eval gives cryptic error messages, show a generic
        # message with the full expression instead.
        raise NoAppException(
            f"Failed to parse arguments as literal values: {app_name!r}."
        ) from None
        _l_(22853)
else:
    raise NoAppException(
        f"Failed to parse {app_name!r} as an attribute name or function call."
    )
    _l_(22856)

try:
    _l_(22862)

    attr = getattr(module, name)
    _l_(22859)
except AttributeError as e:
    _l_(22861)

    raise NoAppException(
        f"Failed to find attribute {name!r} in {module.__name__!r}."
    ) from e
    _l_(22860)

# If the attribute is a function, call it with any args and kwargs
# to get the real application.
if inspect.isfunction(attr):
    _l_(22870)

    try:
        _l_(22868)

        app = attr(*args, **kwargs)
        _l_(22863)
    except TypeError as e:
        _l_(22867)

        if not _called_with_wrong_args(attr):
            _l_(22865)

            raise
            _l_(22864)

        raise NoAppException(
            f"The factory {app_name!r} in module"
            f" {module.__name__!r} could not be called with the"
            " specified arguments."
        ) from e
        _l_(22866)
else:
    app = attr
    _l_(22869)

if isinstance(app, Flask):
    _l_(22872)

    aux = app
    _l_(22871)
    exit(aux)

raise NoAppException(
    "A valid Flask application was not obtained from"
    f" '{module.__name__}:{app_name}'."
)
_l_(22873)
