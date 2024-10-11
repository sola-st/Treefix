from flask import Flask, request # pragma: no cover
from flask.signals import request_started # pragma: no cover

app = Flask(__name__) # pragma: no cover
self = type('Mock', (object,), {})() # pragma: no cover
self._got_first_request = False # pragma: no cover
self._before_request_lock = object() # pragma: no cover
self.before_first_request_funcs = [lambda: print('Executing before first request function')] # pragma: no cover
self.ensure_sync = lambda func: func # pragma: no cover
self.preprocess_request = lambda: None # pragma: no cover
self.dispatch_request = lambda: 'Response from dispatch' # pragma: no cover
self.handle_user_exception = lambda e: f'Handled exception: {str(e)}' # pragma: no cover
self.finalize_request = lambda rv: rv # pragma: no cover
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
