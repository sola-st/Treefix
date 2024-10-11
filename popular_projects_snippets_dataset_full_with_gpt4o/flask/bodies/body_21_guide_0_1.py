from werkzeug.exceptions import HTTPException # pragma: no cover

class MockUrlAdapter:# pragma: no cover
    def match(self, return_rule):# pragma: no cover
        raise HTTPException('Mock HTTP Exception') # pragma: no cover
class MockRequest:# pragma: no cover
    pass # pragma: no cover
self = type('Mock', (object,), {# pragma: no cover
    'url_adapter': MockUrlAdapter(),# pragma: no cover
    'request': MockRequest()# pragma: no cover
})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/ctx.py
from l3.Runtime import _l_
"""Can be overridden by a subclass to hook into the matching
        of the request.
        """
try:
    _l_(19267)

    result = self.url_adapter.match(return_rule=True)  # type: ignore
    _l_(19263)  # type: ignore
    self.request.url_rule, self.request.view_args = result  # type: ignore
    _l_(19264)  # type: ignore
except HTTPException as e:
    _l_(19266)

    self.request.routing_exception = e
    _l_(19265)
