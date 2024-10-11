from typing import Optional, Any, Callable # pragma: no cover

e = type("HTTPException", (object,), {"code": None})() # pragma: no cover
RoutingException = type("RoutingException", (object,), {}) # pragma: no cover
self = type("MockSelf", (object,), {"_find_error_handler": lambda self, e: None, "ensure_sync": lambda self, handler: handler})() # pragma: no cover

from types import SimpleNamespace # pragma: no cover

e = SimpleNamespace(code=None) # pragma: no cover
RoutingException = type('RoutingException', (BaseException,), {}) # pragma: no cover
self = type('Mock', (object,), { '_find_error_handler': lambda self, e: lambda e: 'Handled', 'ensure_sync': lambda self, handler: handler })() # pragma: no cover

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
    _l_(17709)

    aux = e
    _l_(17708)
    exit(aux)

# RoutingExceptions are used internally to trigger routing
# actions, such as slash redirects raising RequestRedirect. They
# are not raised or handled in user code.
if isinstance(e, RoutingException):
    _l_(17711)

    aux = e
    _l_(17710)
    exit(aux)

handler = self._find_error_handler(e)
_l_(17712)
if handler is None:
    _l_(17714)

    aux = e
    _l_(17713)
    exit(aux)
aux = self.ensure_sync(handler)(e)
_l_(17715)
exit(aux)
