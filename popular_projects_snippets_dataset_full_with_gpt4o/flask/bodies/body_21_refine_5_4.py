from werkzeug.exceptions import HTTPException # pragma: no cover

self = type('Mock', (object,), {'url_adapter': type('MockAdapter', (object,), {'match': lambda return_rule: ('mock_rule', {'key': 'value'})})(), 'request': type('MockRequest', (object,), {'url_rule': None, 'view_args': {}, 'routing_exception': None})()})() # pragma: no cover

from werkzeug.exceptions import HTTPException # pragma: no cover

class MockUrlAdapter: # pragma: no cover
    def match(self, return_rule=False): # pragma: no cover
        return ('mock_rule', {'view_arg_key': 'view_arg_value'}) # pragma: no cover
 # pragma: no cover
class MockRequest: # pragma: no cover
    url_rule = None # pragma: no cover
    view_args = {} # pragma: no cover
    routing_exception = None # pragma: no cover
 # pragma: no cover
self = type('Mock', (object,), {'url_adapter': MockUrlAdapter(), 'request': MockRequest()})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/ctx.py
from l3.Runtime import _l_
"""Can be overridden by a subclass to hook into the matching
        of the request.
        """
try:
    _l_(19272)

    result = self.url_adapter.match(return_rule=True)  # type: ignore
    _l_(19268)  # type: ignore
    self.request.url_rule, self.request.view_args = result  # type: ignore
    _l_(19269)  # type: ignore
except HTTPException as e:
    _l_(19271)

    self.request.routing_exception = e
    _l_(19270)
