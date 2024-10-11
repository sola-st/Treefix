import sys # pragma: no cover
from werkzeug.exceptions import InternalServerError # pragma: no cover
import typing as t # pragma: no cover
from flask.signals import got_request_exception # pragma: no cover
import flask.testing as ft # pragma: no cover

sys = sys # pragma: no cover
got_request_exception = got_request_exception # pragma: no cover
e = Exception('An error occurred') # pragma: no cover
t = t # pragma: no cover
InternalServerError = InternalServerError # pragma: no cover
ft = ft # pragma: no cover
self = type('Mock', (object,), { # pragma: no cover
    'config': {'PROPAGATE_EXCEPTIONS': None}, # pragma: no cover
    'testing': False, # pragma: no cover
    'debug': False, # pragma: no cover
    'log_exception': lambda self, exc_info: print(f'Logging exception: {exc_info}'), # pragma: no cover
    '_find_error_handler': lambda self, server_error: None, # pragma: no cover
    'ensure_sync': lambda self, handler: lambda x: x, # pragma: no cover
    'finalize_request': lambda self, server_error, from_error_handler: 'Finalized request' # pragma: no cover
})() # pragma: no cover

import sys # pragma: no cover
from werkzeug.exceptions import InternalServerError # pragma: no cover
import typing as t # pragma: no cover
from flask.signals import got_request_exception # pragma: no cover
from flask import Response # pragma: no cover

sys = sys # pragma: no cover
got_request_exception = got_request_exception # pragma: no cover
e = Exception('An error occurred') # pragma: no cover
t = t # pragma: no cover
InternalServerError = InternalServerError # pragma: no cover
ft_ResponseReturnValue = Response # pragma: no cover
self = type('Mock', (object,), { # pragma: no cover
    'config': {'PROPAGATE_EXCEPTIONS': None}, # pragma: no cover
    'testing': False, # pragma: no cover
    'debug': False, # pragma: no cover
    'log_exception': lambda self, exc_info: print(f'Logging exception: {exc_info}'), # pragma: no cover
    '_find_error_handler': lambda self, server_error: None, # pragma: no cover
    'ensure_sync': lambda self, handler: lambda x: x, # pragma: no cover
    'finalize_request': lambda self, server_error, from_error_handler: 'Finalized request' # pragma: no cover
})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/app.py
from l3.Runtime import _l_
"""Handle an exception that did not have an error handler
        associated with it, or that was raised from an error handler.
        This always causes a 500 ``InternalServerError``.

        Always sends the :data:`got_request_exception` signal.

        If :attr:`propagate_exceptions` is ``True``, such as in debug
        mode, the error will be re-raised so that the debugger can
        display it. Otherwise, the original exception is logged, and
        an :exc:`~werkzeug.exceptions.InternalServerError` is returned.

        If an error handler is registered for ``InternalServerError`` or
        ``500``, it will be used. For consistency, the handler will
        always receive the ``InternalServerError``. The original
        unhandled exception is available as ``e.original_exception``.

        .. versionchanged:: 1.1.0
            Always passes the ``InternalServerError`` instance to the
            handler, setting ``original_exception`` to the unhandled
            error.

        .. versionchanged:: 1.1.0
            ``after_request`` functions and other finalization is done
            even for the default 500 response when there is no handler.

        .. versionadded:: 0.3
        """
exc_info = sys.exc_info()
_l_(22903)
got_request_exception.send(self, exception=e)
_l_(22904)
propagate = self.config["PROPAGATE_EXCEPTIONS"]
_l_(22905)

if propagate is None:
    _l_(22907)

    propagate = self.testing or self.debug
    _l_(22906)

if propagate:
    _l_(22911)

    # Re-raise if called with an active exception, otherwise
    # raise the passed in exception.
    if exc_info[1] is e:
        _l_(22909)

        raise
        _l_(22908)

    raise e
    _l_(22910)

self.log_exception(exc_info)
_l_(22912)
server_error: t.Union[InternalServerError, ft.ResponseReturnValue]
_l_(22913)
server_error = InternalServerError(original_exception=e)
_l_(22914)
handler = self._find_error_handler(server_error)
_l_(22915)

if handler is not None:
    _l_(22917)

    server_error = self.ensure_sync(handler)(server_error)
    _l_(22916)
aux = self.finalize_request(server_error, from_error_handler=True)
_l_(22918)

exit(aux)
