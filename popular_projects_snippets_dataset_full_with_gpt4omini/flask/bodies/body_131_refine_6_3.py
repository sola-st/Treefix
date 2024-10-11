from werkzeug.exceptions import BadRequest, BadRequestKeyError # pragma: no cover

self = type('Mock', (object,), {'config': {'TRAP_HTTP_EXCEPTIONS': True, 'TRAP_BAD_REQUEST_ERRORS': None}, 'debug': True})() # pragma: no cover
e = BadRequest() # pragma: no cover

from werkzeug.exceptions import BadRequestKeyError, BadRequest # pragma: no cover

self = type('Mock', (object,), {'config': {'TRAP_HTTP_EXCEPTIONS': True, 'TRAP_BAD_REQUEST_ERRORS': True}, 'debug': True})() # pragma: no cover
e = BadRequestKeyError('Bad request key error.') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/app.py
from l3.Runtime import _l_
"""Checks if an HTTP exception should be trapped or not.  By default
        this will return ``False`` for all exceptions except for a bad request
        key error if ``TRAP_BAD_REQUEST_ERRORS`` is set to ``True``.  It
        also returns ``True`` if ``TRAP_HTTP_EXCEPTIONS`` is set to ``True``.

        This is called for all HTTP exceptions raised by a view function.
        If it returns ``True`` for any exception the error handler for this
        exception is not called and it shows up as regular exception in the
        traceback.  This is helpful for debugging implicitly raised HTTP
        exceptions.

        .. versionchanged:: 1.0
            Bad request errors are not trapped by default in debug mode.

        .. versionadded:: 0.8
        """
if self.config["TRAP_HTTP_EXCEPTIONS"]:
    _l_(8209)

    aux = True
    _l_(8208)
    exit(aux)

trap_bad_request = self.config["TRAP_BAD_REQUEST_ERRORS"]
_l_(8210)

# if unset, trap key errors in debug mode
if (
    trap_bad_request is None
    and self.debug
    and isinstance(e, BadRequestKeyError)
):
    _l_(8212)

    aux = True
    _l_(8211)
    exit(aux)

if trap_bad_request:
    _l_(8214)

    aux = isinstance(e, BadRequest)
    _l_(8213)
    exit(aux)
aux = False
_l_(8215)

exit(aux)
