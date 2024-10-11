from werkzeug.exceptions import HTTPException # pragma: no cover
from flask import Request # pragma: no cover
from flask import url_for # pragma: no cover

from werkzeug.exceptions import HTTPException # pragma: no cover
class MockRequest: pass # pragma: no cover

self = type('MockSelf', (), {})() # pragma: no cover
self.request = MockRequest() # pragma: no cover
self.request.url_rule = None # pragma: no cover
self.request.view_args = None # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/flask/src/flask/ctx.py
from l3.Runtime import _l_
"""Can be overridden by a subclass to hook into the matching
        of the request.
        """
try:
    _l_(8169)

    result = self.url_adapter.match(return_rule=True)  # type: ignore
    _l_(8165)  # type: ignore
    self.request.url_rule, self.request.view_args = result  # type: ignore
    _l_(8166)  # type: ignore
except HTTPException as e:
    _l_(8168)

    self.request.routing_exception = e
    _l_(8167)
