import werkzeug # pragma: no cover
from werkzeug.test import EnvironBuilder # pragma: no cover
from copy import copy # pragma: no cover

args = [werkzeug.test.EnvironBuilder(), {}] # pragma: no cover
class MockSelfApplication:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.json = {} # pragma: no cover
class MockSelf:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.application = MockSelfApplication()# pragma: no cover
        self._context_stack = type('MockContextStack', (object,), {'close': lambda self: None, 'enter_context': lambda self, cm: None})()# pragma: no cover
        self._new_contexts = []# pragma: no cover
    def _copy_environ(self, environ):# pragma: no cover
        return environ# pragma: no cover
    def _request_from_builder_args(self, args, kwargs):# pragma: no cover
        return BaseRequest(EnvironBuilder().get_environ()) # pragma: no cover
self = MockSelf() # pragma: no cover
kwargs = {} # pragma: no cover
buffered = False # pragma: no cover
follow_redirects = False # pragma: no cover

import werkzeug # pragma: no cover
from werkzeug.test import EnvironBuilder # pragma: no cover
from werkzeug.wrappers import Request as BaseRequest # pragma: no cover
from copy import copy # pragma: no cover

args = [EnvironBuilder()] # pragma: no cover
werkzeug = type('werkzeug', (object,), {'test': werkzeug.test}) # pragma: no cover
BaseRequest = BaseRequest # pragma: no cover
copy = copy # pragma: no cover
self = type('MockSelf', (object,), {# pragma: no cover
  '_copy_environ': lambda self, environ: environ.copy() if environ else {},# pragma: no cover
  'application': type('MockApplication', (object,), {'json': {}})(),# pragma: no cover
  '_request_from_builder_args': lambda self, args, kwargs: EnvironBuilder(path='/').get_request(),# pragma: no cover
  '_context_stack': type('MockContextStack', (object,), {# pragma: no cover
    'close': lambda self: None,# pragma: no cover
    'enter_context': lambda self, cm: None# pragma: no cover
  })(),# pragma: no cover
  '_new_contexts': []# pragma: no cover
})() # pragma: no cover
kwargs = {} # pragma: no cover
buffered = False # pragma: no cover
follow_redirects = False # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/testing.py
from l3.Runtime import _l_
if args and isinstance(
    args[0], (werkzeug.test.EnvironBuilder, dict, BaseRequest)
):
    _l_(18383)

    if isinstance(args[0], werkzeug.test.EnvironBuilder):
        _l_(18381)

        builder = copy(args[0])
        _l_(18374)
        builder.environ_base = self._copy_environ(builder.environ_base or {})
        _l_(18375)
        request = builder.get_request()
        _l_(18376)
    elif isinstance(args[0], dict):
        _l_(18380)

        request = EnvironBuilder.from_environ(
            args[0], app=self.application, environ_base=self._copy_environ({})
        ).get_request()
        _l_(18377)
    else:
        # isinstance(args[0], BaseRequest)
        request = copy(args[0])
        _l_(18378)
        request.environ = self._copy_environ(request.environ)
        _l_(18379)
else:
    # request is None
    request = self._request_from_builder_args(args, kwargs)
    _l_(18382)

# Pop any previously preserved contexts. This prevents contexts
# from being preserved across redirects or multiple requests
# within a single block.
self._context_stack.close()
_l_(18384)

response = super().open(
    request,
    buffered=buffered,
    follow_redirects=follow_redirects,
)
_l_(18385)
response.json_module = self.application.json  # type: ignore[assignment]
_l_(18386)  # type: ignore[assignment]

# Re-push contexts that were preserved during the request.
while self._new_contexts:
    _l_(18389)

    cm = self._new_contexts.pop()
    _l_(18387)
    self._context_stack.enter_context(cm)
    _l_(18388)
aux = response
_l_(18390)

exit(aux)
