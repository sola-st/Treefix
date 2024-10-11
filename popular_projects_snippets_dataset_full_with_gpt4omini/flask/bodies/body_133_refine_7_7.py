from werkzeug.exceptions import InternalServerError # pragma: no cover
import sys # pragma: no cover
from blinker import Signal # pragma: no cover

got_request_exception = Signal('got_request_exception') # pragma: no cover
self = type('Mock', (object,), {'config': {'PROPAGATE_EXCEPTIONS': None}, 'testing': False, 'debug': True, 'log_exception': lambda exc_info: None, '_find_error_handler': lambda self: None, 'ensure_sync': lambda handler: handler, 'finalize_request': lambda self, server_error, from_error_handler: server_error})() # pragma: no cover
e = Exception('Test exception') # pragma: no cover
t = type('Mock', (object,), {'Union': lambda *args: args})() # pragma: no cover
ft = type('Mock', (object,), {'ResponseReturnValue': None})() # pragma: no cover

import sys # pragma: no cover
from werkzeug.exceptions import InternalServerError # pragma: no cover
from blinker import Signal # pragma: no cover

got_request_exception = Signal('got_request_exception') # pragma: no cover
self = type('Mock', (object,), {'config': {'PROPAGATE_EXCEPTIONS': True}, 'testing': False, 'debug': True, 'log_exception': lambda exc_info: print('Logged:', exc_info), '_find_error_handler': lambda self, error: None, 'ensure_sync': lambda handler: handler, 'finalize_request': lambda self, server_error, from_error_handler: 'Final response'})() # pragma: no cover
e = Exception('Test exception') # pragma: no cover
t = type('Mock', (object,), {'Union': lambda *args: args})() # pragma: no cover
ft = type('Mock', (object,), {'ResponseReturnValue': 'Response'})() # pragma: no cover

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
_l_(8684)
got_request_exception.send(self, exception=e)
_l_(8685)
propagate = self.config["PROPAGATE_EXCEPTIONS"]
_l_(8686)

if propagate is None:
    _l_(8688)

    propagate = self.testing or self.debug
    _l_(8687)

if propagate:
    _l_(8692)

    # Re-raise if called with an active exception, otherwise
    # raise the passed in exception.
    if exc_info[1] is e:
        _l_(8690)

        raise
        _l_(8689)

    raise e
    _l_(8691)

self.log_exception(exc_info)
_l_(8693)
server_error: t.Union[InternalServerError, ft.ResponseReturnValue]
_l_(8694)
server_error = InternalServerError(original_exception=e)
_l_(8695)
handler = self._find_error_handler(server_error)
_l_(8696)

if handler is not None:
    _l_(8698)

    server_error = self.ensure_sync(handler)(server_error)
    _l_(8697)
aux = self.finalize_request(server_error, from_error_handler=True)
_l_(8699)

exit(aux)
