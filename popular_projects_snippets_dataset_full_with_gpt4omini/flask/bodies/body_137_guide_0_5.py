from flask import Flask, request, jsonify # pragma: no cover
from werkzeug.exceptions import HTTPException # pragma: no cover

app = Flask(__name__) # pragma: no cover
app._got_first_request = False # pragma: no cover
app._before_request_lock = object() # pragma: no cover
app.before_first_request_funcs = [] # pragma: no cover
app.ensure_sync = lambda f: f # pragma: no cover
app.dispatch_request = lambda: jsonify({'message': 'request dispatched'}) # pragma: no cover
app.handle_user_exception = lambda e: jsonify({'error': str(e)}) # pragma: no cover
app.finalize_request = lambda rv: (rv, 200) # pragma: no cover
request_started = type('MockSignal', (object,), {'send': lambda self: None})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/app.py
from l3.Runtime import _l_
"""Dispatches the request and on top of that performs request
        pre and postprocessing as well as HTTP exception catching and
        error handling.

        .. versionadded:: 0.7
        """
# Run before_first_request functions if this is the thread's first request.
# Inlined to avoid a method call on subsequent requests.
# This is deprecated, will be removed in Flask 2.3.
if not self._got_first_request:
    _l_(6585)

    with self._before_request_lock:
        _l_(6584)

        if not self._got_first_request:
            _l_(6583)

            for func in self.before_first_request_funcs:
                _l_(6581)

                self.ensure_sync(func)()
                _l_(6580)

            self._got_first_request = True
            _l_(6582)

try:
    _l_(6592)

    request_started.send(self)
    _l_(6586)
    rv = self.preprocess_request()
    _l_(6587)
    if rv is None:
        _l_(6589)

        rv = self.dispatch_request()
        _l_(6588)
except Exception as e:
    _l_(6591)

    rv = self.handle_user_exception(e)
    _l_(6590)
aux = self.finalize_request(rv)
_l_(6593)
exit(aux)
