from itertools import chain # pragma: no cover
from flask import request # pragma: no cover

request_ctx = type('Mock', (object,), {'_get_current_object': lambda self: type('MockCtx', (object,), {'_after_request_functions': []})()})() # pragma: no cover
self = type('Mock', (object,), {'ensure_sync': lambda self, func: func, 'after_request_funcs': {}, 'session_interface': type('MockSessionInterface', (object,), {'is_null_session': lambda self, session: False, 'save_session': lambda self, app, session, response: None})()})() # pragma: no cover
response = type('MockResponse', (object,), {})() # pragma: no cover

from itertools import chain # pragma: no cover

request_ctx = type('MockRequestCtx', (object,), {'_get_current_object': lambda self: self, '_after_request_functions': [], 'session': {}})() # pragma: no cover
self = type('MockSelf', (object,), {'ensure_sync': lambda self, func: func, 'after_request_funcs': {None: []}, 'session_interface': type('MockSessionInterface', (object,), {'is_null_session': lambda self, session: False, 'save_session': lambda self, app, session, response: None})()})() # pragma: no cover
response = type('MockResponse', (object,), {})() # pragma: no cover
chain = chain # pragma: no cover
request = type('MockRequest', (object,), {'blueprints': []})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/app.py
from l3.Runtime import _l_
"""Can be overridden in order to modify the response object
        before it's sent to the WSGI server.  By default this will
        call all the :meth:`after_request` decorated functions.

        .. versionchanged:: 0.5
           As of Flask 0.5 the functions registered for after request
           execution are called in reverse order of registration.

        :param response: a :attr:`response_class` object.
        :return: a new response object or the same, has to be an
                 instance of :attr:`response_class`.
        """
ctx = request_ctx._get_current_object()  # type: ignore[attr-defined]
_l_(22947)  # type: ignore[attr-defined]

for func in ctx._after_request_functions:
    _l_(22949)

    response = self.ensure_sync(func)(response)
    _l_(22948)

for name in chain(request.blueprints, (None,)):
    _l_(22953)

    if name in self.after_request_funcs:
        _l_(22952)

        for func in reversed(self.after_request_funcs[name]):
            _l_(22951)

            response = self.ensure_sync(func)(response)
            _l_(22950)

if not self.session_interface.is_null_session(ctx.session):
    _l_(22955)

    self.session_interface.save_session(self, ctx.session, response)
    _l_(22954)
aux = response
_l_(22956)

exit(aux)
