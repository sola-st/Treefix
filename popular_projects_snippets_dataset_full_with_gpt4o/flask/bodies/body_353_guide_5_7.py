from werkzeug.test import EnvironBuilder # pragma: no cover
from werkzeug.wrappers import Request as BaseRequest # pragma: no cover
from copy import copy # pragma: no cover

args = {'REQUEST_METHOD': 'GET', 'PATH_INFO': '/'} # pragma: no cover
buffered = False # pragma: no cover
follow_redirects = False # pragma: no cover
kwargs = {} # pragma: no cover
class MockApplication: # pragma: no cover
    json = {} # pragma: no cover
class MockContextStack: # pragma: no cover
    def close(self): # pragma: no cover
        pass # pragma: no cover
    def enter_context(self, cm): # pragma: no cover
        pass # pragma: no cover
class MockSelf: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.application = MockApplication() # pragma: no cover
        self._context_stack = MockContextStack() # pragma: no cover
        self._new_contexts = [] # pragma: no cover
    def _copy_environ(self, environ): # pragma: no cover
        return environ.copy() # pragma: no cover
    def _request_from_builder_args(self, args, kwargs): # pragma: no cover
        return EnvironBuilder().get_request() # pragma: no cover
self = MockSelf() # pragma: no cover
super_open = lambda request, buffered, follow_redirects: type('MockResponse', (object,), {'json_module': self.application.json})() # pragma: no cover
super = lambda: type('MockSuper', (object,), {'open': super_open})() # pragma: no cover

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
