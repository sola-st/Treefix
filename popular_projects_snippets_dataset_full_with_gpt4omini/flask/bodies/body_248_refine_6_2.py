import ast # pragma: no cover
from flask import Flask # pragma: no cover
import inspect # pragma: no cover

app_name = 'my_flask_app' # pragma: no cover
class NoAppException(Exception): pass # pragma: no cover
_called_with_wrong_args = lambda func: False # pragma: no cover

import ast # pragma: no cover
from flask import Flask # pragma: no cover
import inspect # pragma: no cover

app_name = 'my_flask_app' # pragma: no cover
class NoAppException(Exception): pass # pragma: no cover
module = type('MockModule', (object,), {'__name__': 'mock_module', 'my_flask_app': Flask(__name__)})() # pragma: no cover
_called_with_wrong_args = lambda func: False # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/cli.py
from l3.Runtime import _l_
"""Check if the given string is a variable name or a function. Call
    a function to get the app instance, or return the variable directly.
    """
try:
    from . import Flask
    _l_(8058)

except ImportError:
    pass

# Parse app_name as a single expression to determine if it's a valid
# attribute name or function call.
try:
    _l_(8062)

    expr = ast.parse(app_name.strip(), mode="eval").body
    _l_(8059)
except SyntaxError:
    _l_(8061)

    raise NoAppException(
        f"Failed to parse {app_name!r} as an attribute name or function call."
    ) from None
    _l_(8060)

if isinstance(expr, ast.Name):
    _l_(8076)

    name = expr.id
    _l_(8063)
    args = []
    _l_(8064)
    kwargs = {}
    _l_(8065)
elif isinstance(expr, ast.Call):
    _l_(8075)

    # Ensure the function name is an attribute name only.
    if not isinstance(expr.func, ast.Name):
        _l_(8067)

        raise NoAppException(
            f"Function reference must be a simple name: {app_name!r}."
        )
        _l_(8066)

    name = expr.func.id
    _l_(8068)

    # Parse the positional and keyword arguments as literals.
    try:
        _l_(8073)

        args = [ast.literal_eval(arg) for arg in expr.args]
        _l_(8069)
        kwargs = {kw.arg: ast.literal_eval(kw.value) for kw in expr.keywords}
        _l_(8070)
    except ValueError:
        _l_(8072)

        # literal_eval gives cryptic error messages, show a generic
        # message with the full expression instead.
        raise NoAppException(
            f"Failed to parse arguments as literal values: {app_name!r}."
        ) from None
        _l_(8071)
else:
    raise NoAppException(
        f"Failed to parse {app_name!r} as an attribute name or function call."
    )
    _l_(8074)

try:
    _l_(8080)

    attr = getattr(module, name)
    _l_(8077)
except AttributeError as e:
    _l_(8079)

    raise NoAppException(
        f"Failed to find attribute {name!r} in {module.__name__!r}."
    ) from e
    _l_(8078)

# If the attribute is a function, call it with any args and kwargs
# to get the real application.
if inspect.isfunction(attr):
    _l_(8088)

    try:
        _l_(8086)

        app = attr(*args, **kwargs)
        _l_(8081)
    except TypeError as e:
        _l_(8085)

        if not _called_with_wrong_args(attr):
            _l_(8083)

            raise
            _l_(8082)

        raise NoAppException(
            f"The factory {app_name!r} in module"
            f" {module.__name__!r} could not be called with the"
            " specified arguments."
        ) from e
        _l_(8084)
else:
    app = attr
    _l_(8087)

if isinstance(app, Flask):
    _l_(8090)

    aux = app
    _l_(8089)
    exit(aux)

raise NoAppException(
    "A valid Flask application was not obtained from"
    f" '{module.__name__}:{app_name}'."
)
_l_(8091)
