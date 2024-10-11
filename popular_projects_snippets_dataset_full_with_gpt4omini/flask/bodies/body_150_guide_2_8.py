from flask import Flask, request, Response # pragma: no cover
from werkzeug.wrappers import Response as WerkzeugResponse # pragma: no cover
from itertools import chain # pragma: no cover

app = Flask(__name__) # pragma: no cover
ctx = type('MockContext', (object,), {'_after_request_functions': [lambda r: WerkzeugResponse('After Request Modified')], 'session': {}})() # pragma: no cover
request_ctx = type('MockRequestContext', (object,), {'_get_current_object': lambda self: ctx})() # pragma: no cover
self = type('MockSelf', (object,), {'ensure_sync': lambda f: f, 'after_request_funcs': {None: [lambda r: WerkzeugResponse('Final Response')]} })() # pragma: no cover
response = WerkzeugResponse('Initial Response') # pragma: no cover
ctx.session = {'is_logged_in': True} # pragma: no cover

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
_l_(9066)  # type: ignore[attr-defined]

for func in ctx._after_request_functions:
    _l_(9068)

    response = self.ensure_sync(func)(response)
    _l_(9067)

for name in chain(request.blueprints, (None,)):
    _l_(9072)

    if name in self.after_request_funcs:
        _l_(9071)

        for func in reversed(self.after_request_funcs[name]):
            _l_(9070)

            response = self.ensure_sync(func)(response)
            _l_(9069)

if not self.session_interface.is_null_session(ctx.session):
    _l_(9074)

    self.session_interface.save_session(self, ctx.session, response)
    _l_(9073)
aux = response
_l_(9075)

exit(aux)
