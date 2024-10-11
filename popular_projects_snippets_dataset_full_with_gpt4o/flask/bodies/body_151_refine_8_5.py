import sys # pragma: no cover
from itertools import chain # pragma: no cover

exc = None # pragma: no cover
_sentinel = object() # pragma: no cover
request = type('MockRequest', (object,), {'blueprints': ['blueprint1', 'blueprint2']})() # pragma: no cover
self = type('MockSelf', (object,), {'teardown_request_funcs': {'blueprint1': [lambda exc: None], 'blueprint2': [lambda exc: None], None: [lambda exc: None]}, 'ensure_sync': lambda func: func})() # pragma: no cover
request_tearing_down = type('MockSignal', (object,), {'send': lambda self, **kwargs: None})() # pragma: no cover

import sys # pragma: no cover
from itertools import chain # pragma: no cover

exc = None # pragma: no cover
_sentinel = object() # pragma: no cover
sys = type('MockSys', (object,), {'exc_info': lambda: (None, None, None)})() # pragma: no cover
request = type('MockRequest', (object,), {'blueprints': ['blueprint1', 'blueprint2']})() # pragma: no cover
self = type('MockSelf', (object,), {'teardown_request_funcs': {'blueprint1': [lambda e: print(f'Teardown func for blueprint1 with exc: {e}')], 'blueprint2': [lambda e: print(f'Teardown func for blueprint2 with exc: {e}')], None: [lambda e: print(f'Teardown func for None with exc: {e}')]}, 'ensure_sync': lambda func: func})() # pragma: no cover
request_tearing_down = type('MockSignal', (object,), {'send': lambda s, **kwargs: print(f'Signal sent with kwargs: {kwargs}')})() # pragma: no cover

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
