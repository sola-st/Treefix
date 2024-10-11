from itertools import chain # pragma: no cover
from flask import request # pragma: no cover
class MockSessionInterface: # pragma: no cover
    def is_null_session(self, session): # pragma: no cover
        return False # pragma: no cover
    def save_session(self, app, session, response): # pragma: no cover
        pass # pragma: no cover
class RequestContext: # pragma: no cover
    def _get_current_object(self): # pragma: no cover
        return self # pragma: no cover
Mock = type('Mock', (object,), {'_get_current_object': RequestContext._get_current_object}) # pragma: no cover

request_ctx = Mock() # pragma: no cover
self = Mock() # pragma: no cover
response = Mock() # pragma: no cover
chain = chain # pragma: no cover
request = Mock() # pragma: no cover
self.ensure_sync = lambda func: func # pragma: no cover
request.blueprints = [] # pragma: no cover
self.after_request_funcs = {None: []} # pragma: no cover
self.session_interface = MockSessionInterface() # pragma: no cover

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
