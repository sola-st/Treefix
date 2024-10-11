from typing import Callable, Optional # pragma: no cover

class Mock: pass # pragma: no cover
self = type('Mock', (object,), {'_find_error_handler': lambda e: None, 'ensure_sync': lambda handler: handler})() # pragma: no cover

self = type('Mock', (object,), {})() # pragma: no cover
self._find_error_handler = lambda e: None # pragma: no cover
self.ensure_sync = lambda f: f # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/app.py
from l3.Runtime import _l_
"""Handles an HTTP exception.  By default this will invoke the
        registered error handlers and fall back to returning the
        exception as response.

        .. versionchanged:: 1.0.3
            ``RoutingException``, used internally for actions such as
             slash redirects during routing, is not passed to error
             handlers.

        .. versionchanged:: 1.0
            Exceptions are looked up by code *and* by MRO, so
            ``HTTPException`` subclasses can be handled with a catch-all
            handler for the base ``HTTPException``.

        .. versionadded:: 0.3
        """
# Proxy exceptions don't have error codes.  We want to always return
# those unchanged as errors
if e.code is None:
    _l_(6210)

    aux = e
    _l_(6209)
    exit(aux)

# RoutingExceptions are used internally to trigger routing
# actions, such as slash redirects raising RequestRedirect. They
# are not raised or handled in user code.
if isinstance(e, RoutingException):
    _l_(6212)

    aux = e
    _l_(6211)
    exit(aux)

handler = self._find_error_handler(e)
_l_(6213)
if handler is None:
    _l_(6215)

    aux = e
    _l_(6214)
    exit(aux)
aux = self.ensure_sync(handler)(e)
_l_(6216)
exit(aux)
