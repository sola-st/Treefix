from werkzeug.exceptions import BadRequestKeyError, HTTPException # pragma: no cover
from flask import Flask, request, jsonify # pragma: no cover

app = Flask(__name__) # pragma: no cover
self = type('Mock', (object,), {})() # pragma: no cover
self.debug = True # pragma: no cover
self.config = {'TRAP_BAD_REQUEST_ERRORS': True} # pragma: no cover
self.trap_http_exception = lambda e: False # pragma: no cover
self.handle_http_exception = lambda e: jsonify({'error': str(e)}), 400 # pragma: no cover
self._find_error_handler = lambda e: None # pragma: no cover
e = BadRequestKeyError('SomeKey') # pragma: no cover
self.ensure_sync = lambda handler: handler # pragma: no cover

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
    _l_(8367)

    e.show_exception = True
    _l_(8366)

if isinstance(e, HTTPException) and not self.trap_http_exception(e):
    _l_(8369)

    aux = self.handle_http_exception(e)
    _l_(8368)
    exit(aux)

handler = self._find_error_handler(e)
_l_(8370)

if handler is None:
    _l_(8372)

    raise
    _l_(8371)
aux = self.ensure_sync(handler)(e)
_l_(8373)

exit(aux)
