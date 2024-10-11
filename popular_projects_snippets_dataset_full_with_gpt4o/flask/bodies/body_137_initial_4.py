from threading import Lock # pragma: no cover

self = type('MockSelf', (object,), {# pragma: no cover
    '_got_first_request': False,# pragma: no cover
    '_before_request_lock': Lock(),# pragma: no cover
    'before_first_request_funcs': [],# pragma: no cover
    'ensure_sync': lambda self, func: func,# pragma: no cover
    'preprocess_request': lambda self: None,# pragma: no cover
    'dispatch_request': lambda self: 'response',# pragma: no cover
    'handle_user_exception': lambda self, e: f'error: {str(e)}',# pragma: no cover
    'finalize_request': lambda self, rv: f'finalized: {rv}'# pragma: no cover
})() # pragma: no cover
request_started = type('MockRequestStarted', (object,), {# pragma: no cover
    'send': lambda self, instance: None# pragma: no cover
})() # pragma: no cover

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
    _l_(18104)

    with self._before_request_lock:
        _l_(18103)

        if not self._got_first_request:
            _l_(18102)

            for func in self.before_first_request_funcs:
                _l_(18100)

                self.ensure_sync(func)()
                _l_(18099)

            self._got_first_request = True
            _l_(18101)

try:
    _l_(18111)

    request_started.send(self)
    _l_(18105)
    rv = self.preprocess_request()
    _l_(18106)
    if rv is None:
        _l_(18108)

        rv = self.dispatch_request()
        _l_(18107)
except Exception as e:
    _l_(18110)

    rv = self.handle_user_exception(e)
    _l_(18109)
aux = self.finalize_request(rv)
_l_(18112)
exit(aux)
