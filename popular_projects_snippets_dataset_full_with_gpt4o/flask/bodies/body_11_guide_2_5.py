from functools import update_wrapper # pragma: no cover

class MockApp: # pragma: no cover
    def ensure_sync(self, f): # pragma: no cover
        return f # pragma: no cover
class MockRequestContext: # pragma: no cover
    def __init__(self, app): # pragma: no cover
        self.app = app # pragma: no cover
    def copy(self): # pragma: no cover
        return self # pragma: no cover
    def __enter__(self): # pragma: no cover
        pass # pragma: no cover
    def __exit__(self, exc_type, exc_value, traceback): # pragma: no cover
        pass # pragma: no cover
context_instance = MockRequestContext(MockApp()) # pragma: no cover
f = lambda *args, **kwargs: 'Function Executed' # pragma: no cover

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
_l_(22684)

if ctx is None:
    _l_(22686)

    raise RuntimeError(
        "'copy_current_request_context' can only be used when a"
        " request context is active, such as in a view function."
    )
    _l_(22685)

ctx = ctx.copy()
_l_(22687)

def wrapper(*args, **kwargs):
    _l_(22690)

    with ctx:
        _l_(22689)

        aux = ctx.app.ensure_sync(f)(*args, **kwargs)
        _l_(22688)
        exit(aux)
aux = update_wrapper(wrapper, f)
_l_(22691)

exit(aux)
