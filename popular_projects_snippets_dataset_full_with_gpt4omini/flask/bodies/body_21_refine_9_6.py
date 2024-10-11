from werkzeug.exceptions import HTTPException # pragma: no cover
from flask import Request # pragma: no cover
from flask import url_for # pragma: no cover

class MockURLAdapter:  # Mock of the url_adapter# pragma: no cover
    def match(self, return_rule=False):# pragma: no cover
        return (url_for('some_view'), {'arg1': 'value1'}) # pragma: no cover
class MockRequest:  # Mock of the request# pragma: no cover
    def __init__(self):# pragma: no cover
        self.url_rule = None# pragma: no cover
        self.view_args = None# pragma: no cover
        self.routing_exception = None # pragma: no cover

from werkzeug.exceptions import HTTPException # pragma: no cover
from werkzeug.routing import Map, Rule # pragma: no cover

class MockRequest:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.url_rule = None# pragma: no cover
        self.view_args = None# pragma: no cover
        self.routing_exception = None # pragma: no cover
class MockUrlAdapter:# pragma: no cover
    def match(self, return_rule=True):# pragma: no cover
        return ('/', {'arg': 'value'}) # pragma: no cover
self = type('Mock', (), {'url_adapter': MockUrlAdapter(), 'request': MockRequest()})() # pragma: no cover
HTTPException = type('MockHTTPException', (HTTPException,), {}) # pragma: no cover

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
