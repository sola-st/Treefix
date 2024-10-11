from flask import Flask, request, session # pragma: no cover
from functools import wraps # pragma: no cover

app = Flask(__name__) # pragma: no cover
app.secret_key = 'supersecretkey' # pragma: no cover
f = lambda: 'function result' # pragma: no cover
_cv_request = type('Mock', (object,), {'get': lambda self, _: None})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/ctx.py
from l3.Runtime import _l_
"""A helper function that decorates a function to retain the current
    request context.  This is useful when working with greenlets.  The moment
    the function is decorated a copy of the request context is created and
    then pushed when the function is called.  The current session is also
    included in the copied request context.

    Example::

        import gevent
        from flask import copy_current_request_context

        @app.route('/')
        def index():
            @copy_current_request_context
            def do_some_work():
                # do some work here, it can access flask.request or
                # flask.session like you would otherwise in the view function.
                ...
            gevent.spawn(do_some_work)
            return 'Regular response'

    .. versionadded:: 0.10
    """
ctx = _cv_request.get(None)
_l_(6103)

if ctx is None:
    _l_(6105)

    raise RuntimeError(
        "'copy_current_request_context' can only be used when a"
        " request context is active, such as in a view function."
    )
    _l_(6104)

ctx = ctx.copy()
_l_(6106)

def wrapper(*args, **kwargs):
    _l_(6109)

    with ctx:
        _l_(6108)

        aux = ctx.app.ensure_sync(f)(*args, **kwargs)
        _l_(6107)
        exit(aux)
aux = update_wrapper(wrapper, f)
_l_(6110)

exit(aux)
