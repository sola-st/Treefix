import sys # pragma: no cover
from itertools import chain # pragma: no cover
from flask.signals import request_tearing_down # pragma: no cover

class MockRequest: # pragma: no cover
    blueprints = ['test_blueprint'] # pragma: no cover
 # pragma: no cover
class MockSelf: # pragma: no cover
    teardown_request_funcs = { # pragma: no cover
        None: [lambda exc: print('Teardown None')], # pragma: no cover
        'test_blueprint': [lambda exc: print('Teardown blueprint')] # pragma: no cover
    } # pragma: no cover
    def ensure_sync(self, func): # pragma: no cover
        return func # pragma: no cover
 # pragma: no cover
request = MockRequest() # pragma: no cover
self = MockSelf() # pragma: no cover
exc = type('MockSentinel', (object,), {})() # pragma: no cover
_sentinel = exc # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/app.py
from l3.Runtime import _l_
"""Called after the request is dispatched and the response is
        returned, right before the request context is popped.

        This calls all functions decorated with
        :meth:`teardown_request`, and :meth:`Blueprint.teardown_request`
        if a blueprint handled the request. Finally, the
        :data:`request_tearing_down` signal is sent.

        This is called by
        :meth:`RequestContext.pop() <flask.ctx.RequestContext.pop>`,
        which may be delayed during testing to maintain access to
        resources.

        :param exc: An unhandled exception raised while dispatching the
            request. Detected from the current exception information if
            not passed. Passed to each teardown function.

        .. versionchanged:: 0.9
            Added the ``exc`` argument.
        """
if exc is _sentinel:
    _l_(18340)

    exc = sys.exc_info()[1]
    _l_(18339)

for name in chain(request.blueprints, (None,)):
    _l_(18344)

    if name in self.teardown_request_funcs:
        _l_(18343)

        for func in reversed(self.teardown_request_funcs[name]):
            _l_(18342)

            self.ensure_sync(func)(exc)
            _l_(18341)

request_tearing_down.send(self, exc=exc)
_l_(18345)
