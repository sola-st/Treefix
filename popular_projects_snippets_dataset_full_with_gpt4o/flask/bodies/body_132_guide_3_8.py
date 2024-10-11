from werkzeug.exceptions import BadRequestKeyError, HTTPException # pragma: no cover

class Mock: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.debug = False # pragma: no cover
        self.config = {'TRAP_BAD_REQUEST_ERRORS': False} # pragma: no cover
    def trap_http_exception(self, e): # pragma: no cover
        return False # pragma: no cover
    def handle_http_exception(self, e): # pragma: no cover
        return 'Handled HTTP Exception' # pragma: no cover
    def _find_error_handler(self, e): # pragma: no cover
        return None # pragma: no cover
    def ensure_sync(self, handler): # pragma: no cover
        return handler # pragma: no cover
self = Mock() # pragma: no cover
e = HTTPException() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/app.py
from l3.Runtime import _l_
"""This method is called whenever an exception occurs that
        should be handled. A special case is :class:`~werkzeug
        .exceptions.HTTPException` which is forwarded to the
        :meth:`handle_http_exception` method. This function will either
        return a response value or reraise the exception with the same
        traceback.

        .. versionchanged:: 1.0
            Key errors raised from request data like ``form`` show the
            bad key in debug mode rather than a generic bad request
            message.

        .. versionadded:: 0.7
        """
if isinstance(e, BadRequestKeyError) and (
    self.debug or self.config["TRAP_BAD_REQUEST_ERRORS"]
):
    _l_(19499)

    e.show_exception = True
    _l_(19498)

if isinstance(e, HTTPException) and not self.trap_http_exception(e):
    _l_(19501)

    aux = self.handle_http_exception(e)
    _l_(19500)
    exit(aux)

handler = self._find_error_handler(e)
_l_(19502)

if handler is None:
    _l_(19504)

    raise
    _l_(19503)
aux = self.ensure_sync(handler)(e)
_l_(19505)

exit(aux)
