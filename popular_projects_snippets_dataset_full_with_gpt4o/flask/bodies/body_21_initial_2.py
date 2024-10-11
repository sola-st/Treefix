from werkzeug.exceptions import HTTPException # pragma: no cover
from werkzeug.routing import MapAdapter # pragma: no cover

class MockAdapter(MapAdapter): # pragma: no cover
    def match(self, return_rule=False): # pragma: no cover
        return ('/example', {'arg1': 'value1'}) # pragma: no cover

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
