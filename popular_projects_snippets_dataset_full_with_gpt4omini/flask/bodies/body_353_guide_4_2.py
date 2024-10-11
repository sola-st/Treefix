from werkzeug.test import EnvironBuilder # pragma: no cover
from werkzeug.wrappers import Request as BaseRequest # pragma: no cover
from copy import copy # pragma: no cover

kwargs = {} # pragma: no cover
self = type('Mock', (object,), { 'application': type('MockApp', (object,), {'json': {}})(), '_copy_environ': lambda self, env: env, '_request_from_builder_args': lambda self, args, kwargs: 'mock_request', '_context_stack': type('MockContextStack', (object,), { 'close': lambda self: None, 'enter_context': lambda self, cm: None })(), '_new_contexts': [] })() # pragma: no cover
buffered = False # pragma: no cover
follow_redirects = False # pragma: no cover

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
