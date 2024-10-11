from werkzeug.test import EnvironBuilder # pragma: no cover
import copy # pragma: no cover

args = [{}] # pragma: no cover
werkzeug = type('MockWerkzeug', (), {'test': type('MockTest', (), {'EnvironBuilder': EnvironBuilder})})() # pragma: no cover
BaseRequest = type('MockBaseRequest', (object,), {}) # pragma: no cover
copy = copy.copy # pragma: no cover
self = type('MockSelf', (object,), {'_copy_environ': lambda self, x: x, 'application': type('MockApp', (), {'json': {}})(), '_request_from_builder_args': lambda self, a, b: 'mock_request', '_context_stack': type('MockContextStack', (), {'close': lambda self: None, 'enter_context': lambda self, x: None}), '_new_contexts': []})() # pragma: no cover
EnvironBuilder = EnvironBuilder # pragma: no cover
kwargs = {} # pragma: no cover
buffered = False # pragma: no cover
follow_redirects = True # pragma: no cover

from werkzeug.test import EnvironBuilder # pragma: no cover
from werkzeug.wrappers import Request as BaseRequest # pragma: no cover
import copy # pragma: no cover

args = [{'PATH_INFO': '/test', 'REQUEST_METHOD': 'GET', 'HTTP_USER_AGENT': 'TestAgent'}] # pragma: no cover
werkzeug = type('MockWerkzeug', (), {'test': type('MockTest', (), {'EnvironBuilder': EnvironBuilder})})() # pragma: no cover
BaseRequest = type('MockBaseRequest', (object,), {}) # pragma: no cover
copy = copy.copy # pragma: no cover
self = type('MockSelf', (object,), { # pragma: no cover
    '_copy_environ': lambda self, environ: environ, # pragma: no cover
    'application': type('MockApp', (), {'json': {}})(), # pragma: no cover
    '_request_from_builder_args': lambda self, args, kwargs: BaseRequest(), # pragma: no cover
    '_context_stack': type('MockContextStack', (object,), { # pragma: no cover
        'close': lambda self: None, # pragma: no cover
        'enter_context': lambda self, cm: None # pragma: no cover
    })(), # pragma: no cover
    '_new_contexts': [] # pragma: no cover
}) # pragma: no cover
EnvironBuilder = EnvironBuilder() # pragma: no cover
kwargs = {} # pragma: no cover
buffered = False # pragma: no cover
follow_redirects = True # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/testing.py
from l3.Runtime import _l_
if args and isinstance(
    args[0], (werkzeug.test.EnvironBuilder, dict, BaseRequest)
):
    _l_(7310)

    if isinstance(args[0], werkzeug.test.EnvironBuilder):
        _l_(7308)

        builder = copy(args[0])
        _l_(7301)
        builder.environ_base = self._copy_environ(builder.environ_base or {})
        _l_(7302)
        request = builder.get_request()
        _l_(7303)
    elif isinstance(args[0], dict):
        _l_(7307)

        request = EnvironBuilder.from_environ(
            args[0], app=self.application, environ_base=self._copy_environ({})
        ).get_request()
        _l_(7304)
    else:
        # isinstance(args[0], BaseRequest)
        request = copy(args[0])
        _l_(7305)
        request.environ = self._copy_environ(request.environ)
        _l_(7306)
else:
    # request is None
    request = self._request_from_builder_args(args, kwargs)
    _l_(7309)

# Pop any previously preserved contexts. This prevents contexts
# from being preserved across redirects or multiple requests
# within a single block.
self._context_stack.close()
_l_(7311)

response = super().open(
    request,
    buffered=buffered,
    follow_redirects=follow_redirects,
)
_l_(7312)
response.json_module = self.application.json  # type: ignore[assignment]
_l_(7313)  # type: ignore[assignment]

# Re-push contexts that were preserved during the request.
while self._new_contexts:
    _l_(7316)

    cm = self._new_contexts.pop()
    _l_(7314)
    self._context_stack.enter_context(cm)
    _l_(7315)
aux = response
_l_(7317)

exit(aux)
